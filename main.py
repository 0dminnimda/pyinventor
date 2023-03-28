from __future__ import annotations

from enum import Enum
from pathlib import Path
from typing import Any, Protocol

from wincom import wincom

from com import constants as const
from com.Application import Application as COM_Application
from com.Document import Document as COM_Document
from com.DrawingDocument import DrawingDocument as COM_DrawingDocument
from com.LoftDefinition import LoftDefinition as COM_LoftDefinition
from com.LoftFeature import LoftFeature as COM_LoftFeature
from com.ObjectCollection import ObjectCollection as COM_ObjectCollection
from com.PartDocument import PartDocument as COM_PartDocument
from com.Point import Point as COM_Point
from com.Profile3D import Profile3D as COM_Profile3D
from com.Sketches3D import Sketches3D as COM_Sketches3D


def cast_to(obj, type) -> Any:
    return wincom.CastTo(obj, type)


Dispatch = wincom.DispatchBaseClass


class COM_Base:
    @classmethod
    def self_cast(cls, obj):
        return cast_to(obj, cls.__name__)


class DocumentBase(COM_Base):
    DocumentType: int

    @classmethod
    def open(cls, inventor: Inventor, file: Path):
        if not file.exists():
            document = inventor.Documents.Add(cls.DocumentType, CreateVisible=False)
            document.SaveAs(str(file), SaveCopyAs=True)
        document = inventor.Documents.Open(str(file))
        return cls.self_cast(document)


# SEE: https://adndevblog.typepad.com/manufacturing/2013/01/inventor-document-sub-types.html


class Document(COM_Document, DocumentBase):
    DocumentType: int


class PartDocument(COM_PartDocument, DocumentBase):
    DocumentType: int = const.kPartDocumentObject
    ComponentDefinition: Any


class DrawingDocument(COM_DrawingDocument, DocumentBase):
    DocumentType: int = const.kDrawingDocumentObject
    ActiveSheet: Any


# app: Dispatch  # or wincom.CDispatch for wincom.


class Inventor(COM_Application, COM_Base):
    Visible: bool
    Caption: str
    Documents: Any
    ActiveDocument: Document

    @classmethod
    def make(cls, visible: bool = False) -> Inventor:
        inventor: Inventor = wincom.gencache.EnsureDispatch("Inventor.Application")
        inventor.Visible = visible
        return inventor


class Sketches3D(COM_Sketches3D, COM_Base):
    @classmethod
    def make(cls, document: PartDocument):
        return cls.self_cast(document.ComponentDefinition.Sketches3D.Add())


class Profile3D(COM_Profile3D, COM_Base):
    @classmethod
    def make(cls, sketch3D: Sketches3D):
        return cls.self_cast(sketch3D.Profiles3D.AddOpen.Add())


class Point(COM_Point, COM_Base):
    @classmethod
    def make(cls, inventor: Inventor, x: int, y: int, z: int):
        return inventor.TransientGeometry.CreatePoint(x, y, z)


def make_points(inventor: Inventor, *points: tuple[int, int, int]):
    return [Point.make(inventor, *point) for point in points]


def make_wire(inventor: Inventor, sketch3D, *points, loop: bool = False):
    return [
        sketch3D.SketchLines3D.AddByTwoPoints(point1, point2)  # SketchLine3D
        for point1, point2 in zip(points, points[1:])
    ] + [sketch3D.SketchLines3D.AddByTwoPoints(points[-1], points[0])] * int(loop)


class ObjectCollection(COM_ObjectCollection, COM_Base):
    @classmethod
    def make(cls, inventor: Inventor):
        return cls.self_cast(inventor.TransientObjects.CreateObjectCollection())


class LoftDefinition(COM_LoftDefinition, COM_Base):
    @classmethod
    def make(
        cls, document: PartDocument, section, operation: int = const.kSurfaceOperation
    ):
        return cls.self_cast(
            document.ComponentDefinition.Features.LoftFeatures.CreateLoftDefinition(
                section, operation
            )
        )


class LoftFeature(COM_LoftFeature, COM_Base):
    @classmethod
    def make(cls, document: PartDocument, definition: LoftDefinition):
        return cls.self_cast(
            document.ComponentDefinition.Features.LoftFeatures.Add(definition)
        )


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

inventor = Inventor.make(visible=True)
print(f"Running {inventor.Caption}")

file = Path().cwd() / "Test5.ipt"
document = PartDocument.open(inventor, file)

sketch = Sketches3D.make(document)
points = make_points(inventor, (0, 0, 0), (10, 0, 0), (10, 10, 1), (0, 10, 0))
wire = make_wire(inventor, sketch, *points, loop=True)
profile1 = Profile3D.make(sketch)  # regroup wires

sketch2 = Sketches3D.make(document)
points = make_points(inventor, (0, 0, 5), (10, 0, 5), (10, 10, 5), (0, 10, 5))
wire = make_wire(inventor, sketch2, *points, loop=True)
profile2 = Profile3D.make(sketch2)

# Add profiles to collection
collection = ObjectCollection.make(inventor)
collection.Add(profile1)
collection.Add(profile2)

# Create loft definition and loft itself
loft_def = LoftDefinition.make(document, collection, const.kSurfaceOperation)
loft_feat = LoftFeature.make(document, loft_def)

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
