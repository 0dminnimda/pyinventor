# TODO: https://ru.wikibooks.org/wiki/Autodesk_Inventor_API._Первые_шаги/2D_эскиз

from __future__ import annotations

from enum import Enum
from pathlib import Path
from typing import Any, Protocol, Union

import win32com.client as wincom

import com
from com import constants as const


def cast_to(obj, tp: str | type) -> Any:
    if isinstance(tp, type):
        tp = tp.__name__
    return wincom.CastTo(obj, tp)


Dispatch = wincom.DispatchBaseClass


class COMBase:
    @classmethod
    def self_cast(cls, obj):
        return cast_to(obj, cls.__name__)


class DocumentBase(COMBase):
    DocumentType: int
    extention: str

    @classmethod
    def open(cls, inventor: Inventor, file: Path):
        if not file.exists():
            document = inventor.Documents.Add(cls.DocumentType, CreateVisible=False)
            document.SaveAs(str(file), SaveCopyAs=True)
        document = inventor.Documents.Open(str(file))
        return cls.self_cast(document)


# SEE: https://adndevblog.typepad.com/manufacturing/2013/01/inventor-document-sub-types.html


class Document(com.Document, DocumentBase):
    DocumentType: int


class PartDocument(com.PartDocument, DocumentBase):
    DocumentType: int = const.kPartDocumentObject
    ComponentDefinition: Any
    extention: str = ".ipt"


class DrawingDocument(com.DrawingDocument, DocumentBase):
    DocumentType: int = const.kDrawingDocumentObject
    ActiveSheet: Any
    extention: str = ".idw"


# app: Dispatch  # or wincom.CDispatch for wincom.


class Inventor(com.Application, COMBase):
    Visible: bool
    Caption: str
    Documents: Any
    ActiveDocument: Document

    @classmethod
    def make(cls, visible: bool = False) -> Inventor:
        inventor = Inventor(wincom.Dispatch("Inventor.Application"))
        inventor.Visible = visible
        return inventor

    # import traceback
    # from contextlib import contextmanager
    # @classmethod
    # @contextmanager
    # def open(cls, visible: bool = False):
    #     ui = None
    #     try:
    #         inventor = cls.make(visible=visible)
    #         # ui = inventor.UserInterfaceManager
    #         yield inventor
    #     except Exception:
    #         # if ui:
    #         #     ui.messageBox(f"Failed:\n{traceback.format_exc()}")
    #         raise


class WorkPlane(COMBase):
    @classmethod
    def YZ(cls, document: PartDocument):
        return cls.self_cast(document.ComponentDefinition.WorkPlanes.Item(1))

    @classmethod
    def XZ(cls, document: PartDocument):
        return cls.self_cast(document.ComponentDefinition.WorkPlanes.Item(2))

    @classmethod
    def XY(cls, document: PartDocument):
        return cls.self_cast(document.ComponentDefinition.WorkPlanes.Item(3))


class Sketch(COMBase):
    @classmethod
    def make(cls, document: PartDocument, plane: WorkPlane):
        return cls.self_cast(document.ComponentDefinition.Sketches.Add(plane))


class SketchImage(COMBase):
    @classmethod
    def make(cls, sketch: Sketch, path: str, point: Point2d, link: bool = False):
        return cls.self_cast(sketch.SketchImages.Add(path, point, link))


class Sketch3D(com.Sketch3D, COMBase):
    @classmethod
    def make(cls, document: PartDocument):
        return cls.self_cast(document.ComponentDefinition.Sketches3D.Add())


class Profile3D(com.Profile3D, COMBase):
    @classmethod
    def make(cls, sketch3D: Sketch3D):
        return cls.self_cast(sketch3D.Profiles3D.AddOpen())


class Point2d(COMBase):
    @classmethod
    def make(cls, inventor: Inventor, x: int, y: int):
        return inventor.TransientGeometry.CreatePoint2d(x, y)


class Point(com.Point, COMBase):
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


class ObjectCollection(com.ObjectCollection, COMBase):
    @classmethod
    def make(cls, inventor: Inventor):
        return cls.self_cast(inventor.TransientObjects.CreateObjectCollection())


class LoftDefinition(com.LoftDefinition, COMBase):
    @classmethod
    def make(
        cls, document: PartDocument, section, operation: int = const.kSurfaceOperation
    ):
        return cls.self_cast(
            document.ComponentDefinition.Features.LoftFeatures.CreateLoftDefinition(
                section, operation
            )
        )


class LoftFeature(com.LoftFeature, COMBase):
    @classmethod
    def make(cls, document: PartDocument, definition: LoftDefinition):
        return cls.self_cast(
            document.ComponentDefinition.Features.LoftFeatures.Add(definition)
        )


class ReferencedOLEFileDescriptor(COMBase):
    @classmethod
    def make(cls, document: PartDocument, path: Union[str, Path], ole_document_type: int = const.kOLEDocumentEmbeddingObject):
        return cls.self_cast(
            document.ReferencedOLEFileDescriptors.Add(path, ole_document_type)
        )


def add_file(document: Document, path: Path) -> ReferencedOLEFileDescriptor:
    """Add an (multimedia?) file to the document"""

    oleReference = ReferencedOLEFileDescriptor.make(document, path)

    oleReference.BrowserVisible = True
    # oleReference.Visible = True
    oleReference.DisplayName = path.stem

    return oleReference
