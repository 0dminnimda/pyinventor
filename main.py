from pathlib import Path
import win32com.client as wincom
from enum import Enum
# from dataclasses import dataclass
from typing import Any, Protocol


def cast_to(obj, type) -> Any:
    return wincom.CastTo(obj, type)


Dispatch = wincom.DispatchBaseClass
const = wincom.constants


class Document(Protocol):
    DocumentType: int
    # ActiveSheet


# app: Dispatch  # or wincom.CDispatch for wincom.

class Inventor(Protocol):
    Visible: bool
    Caption: str
    Documents: Any
    ActiveDocument: Document

    def Quit(self) -> None:
        ...


# SEE: https://adndevblog.typepad.com/manufacturing/2013/01/inventor-document-sub-types.html

class DocumentType(Enum):
    Part = 12290  # .ipt
    Assembly = 12291  # .iam
    Drawing = 12292  # .dwg, .idw
    Sceme = 12293  # .ipn (Presentation?)
    Unknown = 12298 # (Invalid?)
    # .ipn - ?


def _find_document_types(inventor: Inventor, prev: int = 0):
    # _prev = 875207
    import pywintypes
    for i in range(prev, 10**10):
        try:
                document = inventor.Documents.Add(i)
        except pywintypes.com_error:
                continue
        print(i, getattr(document, "DocumentType", None))
        document.Close(SkipSave=True)


def start_inventor(visible: bool = False) -> Inventor:
    inventor: Inventor = wincom.gencache.EnsureDispatch("Inventor.Application")
    inventor.Visible = visible
    return inventor


def open_document(inventor: Inventor, file: Path, type: DocumentType) -> Document:
    if not file.exists():
        document = inventor.Documents.Add(type.value, CreateVisible=False)
        document.SaveAs(str(file), SaveCopyAs=True)
    document = inventor.Documents.Open(str(file))
    return cast_to(document, type.name + "Document")


def add_Sketch3D(document):
    return cast_to(document.ComponentDefinition.Sketches3D.Add(), "Sketch3D")

def add_Profile3D(sketch3D):
    return cast_to(sketch3D.Profiles3D.AddOpen(), "Profile3D")

def make_point(inventor: Inventor, x: int, y: int, z: int):
    return inventor.TransientGeometry.CreatePoint(x, y, z)


def make_points(inventor: Inventor, *points: tuple[int, int, int]):
    return [make_point(inventor, *point) for point in points]


def make_wire(inventor: Inventor, sketch3D, *points):
    return [
        sketch3D.SketchLines3D.AddByTwoPoints(point1, point2)  # SketchLine3D
        for point1, point2 in zip(points, points[1:])
    ]


"""
template_version = inventor.FileManager.SoftwareVersionSaved(templatePath)
inventor_version = inventor.SoftwareVersion

if inventorVersion.Major > templateVersion.Major Then
    # Migrate drawing template before using 
    template = inventor.Documents.Open(templatePath, OpenVisible=False)
    template.Save()
    template.Close()

doc = inventor.Documents.Add(kDrawingDocumentObject, templatePath, CreateVisible=True)
"""

inventor = start_inventor(visible=True)
print(f"Running {inventor.Caption}")

file = Path().cwd() / "Test5.ipt"
document = open_document(inventor, file, DocumentType.Part)

sketch = add_Sketch3D(document)

points = make_points(inventor, (0, 0, 0), (10, 0, 0), (10, 10, 1), (0, 10, 0), (0, 0, 0))
wire = make_wire(inventor, sketch, *points)

# Declare Profile3D to regroup wires
profile1 = add_Profile3D(sketch)

# Declare another sketch to be able to catch 2 differents profiles
sketch2 = add_Sketch3D(document)

points = make_points(inventor, (0, 0, 5), (10, 0, 5), (10, 10, 5), (0, 10, 5), (0, 0, 5))
wire = make_wire(inventor, sketch2, *points)

# Declare second Profile3D to regroup wires
profile2 = add_Profile3D(sketch2)

# Create object collection need by Inventor functions
collection = cast_to(inventor.TransientObjects.CreateObjectCollection(), "ObjectCollection")

# Add profiles to collection
collection.Add(profile1)
collection.Add(profile2)

# Create loft definition needed by Loft function
loft_def = cast_to(document.ComponentDefinition.Features.LoftFeatures.CreateLoftDefinition(collection, const.kSurfaceOperation), "LoftDefinition")

# Creating loft.
loft_feat = cast_to(document.ComponentDefinition.Features.LoftFeatures.Add(loft_def), "LoftFeature")

# view = document.Views(1)

# SEE: https://ru.wikibooks.org/wiki/Autodesk_Inventor_API._Первые_шаги/Первая_программа
# SEE: https://modthemachine.typepad.com/my_weblog/drawings/
# SEE: https://ww3.cad.de/foren/ubb/uploads/invhp/VBA-INVENTOR-vba-inventor.pdf

"""
project = inventor.VBAProjects.Item(1)
module = project.InventorVBAComponents.Item(1)
module.InventorVBAMembers.Item(1)
"""

"""
project = inventor.VBAProjects.Item(1)
InvVBAModule = project.InventorVBAComponents.Item(2)
InvVBAProcedureToRun = InvVBAModule.InventorVBAMembers.Item(1)
InvVBAProcedureToRun.Execute
"""

# params = document.ComponentDefinition.Parameters
# params.Item("Name").Expression = *Value*

document.Update()
document.Save()
document.Close(SkipSave=True)

if 0:
    inventor.Quit()
