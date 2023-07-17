# TODO: https://ru.wikibooks.org/wiki/Autodesk_Inventor_API._Первые_шаги/2D_эскиз

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
from com.Sketch3D import Sketch3D as COM_Sketch3D


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


class WorkPlane(COM_Base):
    @classmethod
    def YZ(cls, document: PartDocument):
        return cls.self_cast(document.ComponentDefinition.WorkPlanes.Item(1))

    @classmethod
    def XZ(cls, document: PartDocument):
        return cls.self_cast(document.ComponentDefinition.WorkPlanes.Item(2))

    @classmethod
    def XY(cls, document: PartDocument):
        return cls.self_cast(document.ComponentDefinition.WorkPlanes.Item(3))


class Sketch(COM_Base):
    @classmethod
    def make(cls, document: PartDocument, plane: WorkPlane):
        return cls.self_cast(document.ComponentDefinition.Sketches.Add(plane))


class SketchImage(COM_Base):
    @classmethod
    def make(cls, sketch: Sketch, path: str, point: Point2d, link: bool = True):
        return cls.self_cast(sketch.SketchImages.Add(path, point, link))


class Sketch3D(COM_Sketch3D, COM_Base):
    @classmethod
    def make(cls, document: PartDocument):
        return cls.self_cast(document.ComponentDefinition.Sketches3D.Add())


class Profile3D(COM_Profile3D, COM_Base):
    @classmethod
    def make(cls, sketch3D: Sketch3D):
        return cls.self_cast(sketch3D.Profiles3D.AddOpen())


class Point2d(COM_Base):
    @classmethod
    def make(cls, inventor: Inventor, x: int, y: int):
        return inventor.TransientGeometry.CreatePoint2d(x, y)


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


def add_image(document: Document):
    """Add an image to the document"""

    file_name = "sampe.png"
    image_path = Path(__file__).parent.parent / file_name

    oleReference = document.ReferencedOLEFileDescriptors.Add(image_path, const.kOLEDocumentEmbeddingObject)
    oleReference = cast_to(oleReference, "ReferencedOLEFileDescriptor")

    oleReference.BrowserVisible = True
    # oleReference.Visible = True
    oleReference.DisplayName = file_name
