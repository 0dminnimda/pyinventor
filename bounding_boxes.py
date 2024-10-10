from pathlib import Path
from dataclasses import dataclass, field
from collections import deque

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


ROUND_TO_NDIGITS = 0


def get_body_size(body: com.SurfaceBody) -> BodySize:
    bounding_box: com.OrientedBox = body.OrientedMinimumRangeBox

    return tuple(sorted(
        [
            round(bounding_box.DirectionOne.Length, ROUND_TO_NDIGITS),
            round(bounding_box.DirectionTwo.Length, ROUND_TO_NDIGITS),
            round(bounding_box.DirectionThree.Length, ROUND_TO_NDIGITS),
        ],
        reverse=True,
    ))


@dataclass
class SurfaceBodyVisitor:
    predecessors: deque = field(default_factory=deque)

    def traverse_assembly(self, assembly_document):
        assembly_document = cast_to(assembly_document, com.AssemblyDocument)

        self.predecessors.append(assembly_document)
        self.traverse_occurrences(assembly_document.ComponentDefinition.Occurrences)
        self.predecessors.pop()

    def traverse_occurrences(self, occurrences):
        occurance: com.ComponentOccurrence
        for occurance in occurrences:
            self.predecessors.append(occurance)
            if occurance.DefinitionDocumentType == const.kPartDocumentObject:
                for body in occurance.SurfaceBodies:
                    self.visit_surface_body(body)

            self.traverse_occurrences(occurance.SubOccurrences)
            self.predecessors.pop()

    def visit_surface_body(self, body: com.SurfaceBody):
        pass


def get_name(obj, with_parents: bool = True, *, first: bool = True) -> str:
    result = ""
    if hasattr(obj, "Name"):
        result = obj.Name
    elif hasattr(obj, "DisplayName"):
        result = obj.DisplayName
    elif first:
        result = "<Без Имени>"

    if with_parents and hasattr(obj, "Parent"):
        parent_result = get_name(obj.Parent, first=False)
        if parent_result and result:
            parent_result += " : "
        result = parent_result + result

    return result


@dataclass
class SurfaceBodySizeTaker(SurfaceBodyVisitor):
    table: list[tuple] = field(default_factory=list)

    def visit_surface_body(self, body: com.SurfaceBody):
        predecessors = [
            get_name(it, False, first=False)
            for it in self.predecessors
        ] + [get_name(body, False)]
        self.table.append((
            get_name(body),
            " : ".join(it for it in predecessors if it),
            get_name(body, False),
            *get_body_size(body)
        ))


def dump_size_table_as_csv(table: list[tuple]) -> str:
    result = ""
    for it in table:
        result += ";".join(map(str, it)) + "\n"
    return result


inventor = Inventor.make(visible=True)
print(f"Running {inventor.Caption}")

document = inventor.ActiveDocument
print(document.DisplayName)

visitor = SurfaceBodySizeTaker()
visitor.traverse_assembly(document)

Path("table.csv").write_text(dump_size_table_as_csv(visitor.table), "utf-8")
print("Работа завершена")
