from pathlib import Path

from pyinventor import (
    Inventor,
    LoftDefinition,
    LoftFeature,
    ObjectCollection,
    PartDocument,
    Profile3D,
    Sketch3D,
    const,
    make_points,
    make_wire,
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

sketch = Sketch3D.make(document)
points = make_points(inventor, (0, 0, 0), (10, 0, 0), (10, 10, 1), (0, 10, 0))
wire = make_wire(inventor, sketch, *points, loop=True)
profile1 = Profile3D.make(sketch)  # regroup wires

sketch2 = Sketch3D.make(document)
points = make_points(inventor, (0, 0, 5), (10, 0, 5), (10, 10, 5), (0, 10, 5))
wire = make_wire(inventor, sketch2, *points, loop=True)
profile2 = Profile3D.make(sketch2)

# Add profiles to collection
collection = ObjectCollection.make(inventor)
collection.Add(profile1)
collection.Add(profile2)

# Create loft definition and loft itself
loft_def = LoftDefinition.make(document, collection, const.kNewBodyOperation)  # const.kSurfaceOperation)
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

if 0:
    document.Close(SkipSave=True)

if 0:
    inventor.Quit()
