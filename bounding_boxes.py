from pathlib import Path
from dataclasses import dataclass, field

from pyinventor import (
    Inventor,
    LoftDefinition,
    LoftFeature,
    ObjectCollection,
    Document,
    DrawingDocument,
    PartDocument,
    SketchImage,
    WorkPlane,
    Profile3D,
    Sketch3D,
    Sketch,
    Point2d,
    const,
    make_points,
    make_wire,
    cast_to,
    add_file,
    const,
    com,
)


BodySize = tuple[float, float, float]


def get_body_size(body: com.SurfaceBody) -> BodySize:
    bounding_box: com.OrientedBox = body.OrientedMinimumRangeBox

    return tuple(sorted(
        [
            round(bounding_box.DirectionOne.Length, 3),
            round(bounding_box.DirectionTwo.Length, 3),
            round(bounding_box.DirectionThree.Length, 3),
        ],
        reverse=True,
    ))


class PartVisitor:
    def visit(self, obj):
        if obj.DocumentType == const.kAssemblyDocumentObject:
            self.visit_AssemblyDocument(obj)
        elif obj.DocumentType == const.kPartDocumentObject:
            self.visit_PartDocument(obj)
        else:
            raise Exception(f"Unsupported document type {obj.File.FullFileName}")

    def visit_AssemblyDocument(self, obj):
        document = cast_to(obj, com.AssemblyDocument)

        referenced = document.ReferencedDocuments
        for i in range(1, referenced.Count + 1):
            self.visit(referenced.Item(i))

    def visit_PartDocument(self, obj):
        document = cast_to(obj, com.PartDocument)
        print(document.DisplayName)
        # print(doc.SubComponents)
        for it in document.ComponentDefinition.Occurrences:
            print("    ", it)

    # def visit_part(self, obj):
    #     pass


class SurfaceBodyVisitor:
    def traverse_assembly(self, assembly_document):
        assembly_document = cast_to(assembly_document, com.AssemblyDocument)
        self.traverse_occurrences(assembly_document.ComponentDefinition.Occurrences)

    def traverse_occurrences(self, occurrences):
        occurance: com.ComponentOccurrence
        for occurance in occurrences:
            if occurance.DefinitionDocumentType == const.kPartDocumentObject:
                for body in occurance.SurfaceBodies:
                    self.visit_surface_body(body)

            self.traverse_occurrences(occurance.SubOccurrences)

    def visit_surface_body(self, body: com.SurfaceBody):
        pass


_get_name_cache = {}


def get_name(obj) -> str:
    key = hash((69, id(obj)))
    if key in _get_name_cache:
        return _get_name_cache[key]

    result = ""
    if hasattr(obj, "Name"):
        result = obj.Name
    elif hasattr(obj, "DisplayName"):
        result = obj.DisplayName
    # elif not result:
    #     result = "<Без Имени>"

    if hasattr(obj, "Parent"):
        parent_result = get_name(obj.Parent)
        if parent_result and result:
            parent_result += " : "
        result = parent_result + result

    _get_name_cache[key] = result
    return result


@dataclass
class SurfaceBodySizeTaker(SurfaceBodyVisitor):
    table: list[tuple[str, BodySize]] = field(default_factory=list)

    def visit_surface_body(self, body: com.SurfaceBody):
        self.table.append((get_name(body), get_body_size(body)))


def dump_size_table_as_csv(table: list[tuple[str, BodySize]]) -> str:
    result = ""
    for name, size in table:
        result += f"{name};" + ";".join(map(str, size)) + "\n"
    return result


inventor = Inventor.make(visible=True)
print(f"Running {inventor.Caption}")

file = Path(__file__).parent / "test" / "detail.iam"
document = Document.open(inventor, file)

visitor = SurfaceBodySizeTaker()
visitor.traverse_assembly(document)

# for it in visitor.table:
#     print(it)

Path("table.csv").write_text(dump_size_table_as_csv(visitor.table), "utf-8")

# referenced = document.ReferencedDocuments
# for i in range(1, referenced.Count + 1):
#     # doc = cast_to(referenced.Item(i), com.AssemblyDocument)
#     doc = referenced.Item(i)
#     print(doc, repr(doc), doc.DisplayName, dir(doc))
#     # print(doc.SubComponents)
#     # for it in doc.ComponentDefinition.Occurrences:
#     #     print("    ", it.Name)

# body = inventor.CommandManager.Pick(const.kPartBodyFilter, "Выбери тело")
# print(body.Name)
