# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 18:30:11 2023
'Autodesk Inventor Object Library'
makepy_version = '0.5.01'
python_version = 0x30b02f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{D98A091D-3A0F-4C3E-B36E-61F62068D488}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class TransientGeometry(DispatchBaseClass):
	'Object through which all transient geometry objects are constructed. For more information, see the Transient Geometry overview.'
	CLSID = IID('{97ECB3AE-6C6E-4D8A-A91E-564314494EB8}')
	coclass_clsid = None

	# Result is of type Arc2d
	def CreateArc2d(self, Center=defaultNamedNotOptArg, Radius=defaultNamedNotOptArg, StartAngle=defaultNamedNotOptArg, SweepAngle=defaultNamedNotOptArg):
		'Method that creates a Arc2d object'
		ret = self._oleobj_.InvokeTypes(67126944, LCID, 1, (9, 0), ((9, 1), (5, 1), (5, 1), (5, 1)),Center
			, Radius, StartAngle, SweepAngle)
		if ret is not None:
			ret = Dispatch(ret, 'CreateArc2d', '{C173A091-012F-11D5-8DEA-0010B541CAA8}')
		return ret

	# Result is of type Arc2d
	def CreateArc2dByThreePoints(self, PointOne=defaultNamedNotOptArg, PointTwo=defaultNamedNotOptArg, PointThree=defaultNamedNotOptArg):
		'Method that creates an Arc2d object by three points'
		ret = self._oleobj_.InvokeTypes(67126952, LCID, 1, (9, 0), ((9, 1), (9, 1), (9, 1)),PointOne
			, PointTwo, PointThree)
		if ret is not None:
			ret = Dispatch(ret, 'CreateArc2dByThreePoints', '{C173A091-012F-11D5-8DEA-0010B541CAA8}')
		return ret

	# Result is of type Arc3d
	def CreateArc3d(self, Center=defaultNamedNotOptArg, Normal=defaultNamedNotOptArg, ReferenceVector=defaultNamedNotOptArg, Radius=defaultNamedNotOptArg
			, StartAngle=defaultNamedNotOptArg, SweepAngle=defaultNamedNotOptArg):
		'Method that creates a Arc3d object'
		ret = self._oleobj_.InvokeTypes(67126945, LCID, 1, (9, 0), ((9, 1), (9, 1), (9, 1), (5, 1), (5, 1), (5, 1)),Center
			, Normal, ReferenceVector, Radius, StartAngle, SweepAngle
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateArc3d', '{744FFECE-189A-4ACC-8BCF-8F959D5E4EAE}')
		return ret

	# Result is of type Arc3d
	def CreateArc3dByThreePoints(self, PointOne=defaultNamedNotOptArg, PointTwo=defaultNamedNotOptArg, PointThree=defaultNamedNotOptArg):
		'Method that creates an Arc3d object by three points'
		ret = self._oleobj_.InvokeTypes(67126953, LCID, 1, (9, 0), ((9, 1), (9, 1), (9, 1)),PointOne
			, PointTwo, PointThree)
		if ret is not None:
			ret = Dispatch(ret, 'CreateArc3dByThreePoints', '{744FFECE-189A-4ACC-8BCF-8F959D5E4EAE}')
		return ret

	# Result is of type BSplineCurve
	def CreateBSplineCurve(self, Order=defaultNamedNotOptArg, Poles=defaultNamedNotOptArg, Knots=defaultNamedNotOptArg, Weights=defaultNamedNotOptArg
			, IsPeriodic=defaultNamedNotOptArg):
		'Method that creates a BSplineCurve object'
		return self._ApplyTypes_(67126927, 1, (9, 0), ((3, 1), (24581, 3), (24581, 3), (24581, 3), (11, 1)), 'CreateBSplineCurve', '{49CB4BB9-872A-11D3-8524-0060B0F0B5B7}',Order
			, Poles, Knots, Weights, IsPeriodic)

	# Result is of type BSplineCurve2d
	def CreateBSplineCurve2d(self, Order=defaultNamedNotOptArg, Poles=defaultNamedNotOptArg, Knots=defaultNamedNotOptArg, Weights=defaultNamedNotOptArg
			, IsPeriodic=defaultNamedNotOptArg):
		'Method that creates a BSplineCurve2d object'
		return self._ApplyTypes_(67126928, 1, (9, 0), ((3, 1), (24581, 3), (24581, 3), (24581, 3), (11, 1)), 'CreateBSplineCurve2d', '{49CB4BBA-872A-11D3-8524-0060B0F0B5B7}',Order
			, Poles, Knots, Weights, IsPeriodic)

	# Result is of type BSplineCurve2dDefinition
	def CreateBSplineCurve2dDefinition(self):
		'Method that creates a new BSplineCurve2dDefinition object. This method creates an empty object. Use the methods/properties on this object to populate it and then use it as the argument in the CreateFittedBSplineCurve2d method.'
		ret = self._oleobj_.InvokeTypes(67126941, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBSplineCurve2dDefinition', '{E3B2EB5A-FE46-4DA6-8DDD-6135E2120CB2}')
		return ret

	# Result is of type BSplineCurveDefinition
	def CreateBSplineCurveDefinition(self):
		'Method that creates a new BSplineCurveDefinition object. This method creates an empty object. Use the methods/properties on this object to populate it and then use it as the argument in the CreateFittedBSplineCurve method.'
		ret = self._oleobj_.InvokeTypes(67126940, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBSplineCurveDefinition', '{30630D32-6807-4D69-8E77-224FD90A21BF}')
		return ret

	# Result is of type BSplineSurface
	def CreateBSplineSurface(self, Order=defaultNamedNotOptArg, Poles=defaultNamedNotOptArg, KnotsU=defaultNamedNotOptArg, KnotsV=defaultNamedNotOptArg
			, Weights=defaultNamedNotOptArg, IsPeriodic=defaultNamedNotOptArg):
		'Method that creates a BSplineSurface object'
		ret = self._oleobj_.InvokeTypes(67126936, LCID, 1, (9, 0), ((24579, 1), (24581, 1), (24581, 1), (24581, 1), (24581, 1), (24587, 1)),Order
			, Poles, KnotsU, KnotsV, Weights, IsPeriodic
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBSplineSurface', '{5DF860A6-6B16-11D3-B794-0060B0F159EF}')
		return ret

	# Result is of type Box
	def CreateBox(self):
		'Method that creates a new Box object. The min and max points of the box are initialized to (0,0,0) . The object created is a transient mathematical object and is not displayed graphically.'
		ret = self._oleobj_.InvokeTypes(67126915, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBox', '{5DF86062-6B16-11D3-B794-0060B0F159EF}')
		return ret

	# Result is of type Box2d
	def CreateBox2d(self):
		'Method that creates a new Box2d object. The min and max points of the box are initialized to (0,0) . The object created is a transient mathematical object and is not displayed graphically.'
		ret = self._oleobj_.InvokeTypes(67126916, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBox2d', '{5DF86063-6B16-11D3-B794-0060B0F159EF}')
		return ret

	# Result is of type Circle
	def CreateCircle(self, Center=defaultNamedNotOptArg, Normal=defaultNamedNotOptArg, Radius=defaultNamedNotOptArg):
		'Method that creates a Circle object'
		ret = self._oleobj_.InvokeTypes(67126925, LCID, 1, (9, 0), ((9, 1), (9, 1), (5, 1)),Center
			, Normal, Radius)
		if ret is not None:
			ret = Dispatch(ret, 'CreateCircle', '{49CB4BB5-872A-11D3-8524-0060B0F0B5B7}')
		return ret

	# Result is of type Circle2d
	def CreateCircle2d(self, Center=defaultNamedNotOptArg, Radius=defaultNamedNotOptArg):
		'Method that creates a Circle2d object'
		ret = self._oleobj_.InvokeTypes(67126926, LCID, 1, (9, 0), ((9, 1), (5, 1)),Center
			, Radius)
		if ret is not None:
			ret = Dispatch(ret, 'CreateCircle2d', '{49CB4BB6-872A-11D3-8524-0060B0F0B5B7}')
		return ret

	# Result is of type Circle2d
	def CreateCircle2dByThreePoints(self, PointOne=defaultNamedNotOptArg, PointTwo=defaultNamedNotOptArg, PointThree=defaultNamedNotOptArg):
		'Method that creates a Circle2d object by three points'
		ret = self._oleobj_.InvokeTypes(67126954, LCID, 1, (9, 0), ((9, 1), (9, 1), (9, 1)),PointOne
			, PointTwo, PointThree)
		if ret is not None:
			ret = Dispatch(ret, 'CreateCircle2dByThreePoints', '{49CB4BB6-872A-11D3-8524-0060B0F0B5B7}')
		return ret

	# Result is of type Circle
	def CreateCircleByThreePoints(self, PointOne=defaultNamedNotOptArg, PointTwo=defaultNamedNotOptArg, PointThree=defaultNamedNotOptArg):
		'Method that creates a Circle object by three points'
		ret = self._oleobj_.InvokeTypes(67126955, LCID, 1, (9, 0), ((9, 1), (9, 1), (9, 1)),PointOne
			, PointTwo, PointThree)
		if ret is not None:
			ret = Dispatch(ret, 'CreateCircleByThreePoints', '{49CB4BB5-872A-11D3-8524-0060B0F0B5B7}')
		return ret

	# Result is of type Cone
	def CreateCone(self, RootPoint=defaultNamedNotOptArg, Axis=defaultNamedNotOptArg, Radius=defaultNamedNotOptArg, HalfAngle=defaultNamedNotOptArg
			, IsExpanding=defaultNamedNotOptArg):
		'Method that creates a Cone object'
		ret = self._oleobj_.InvokeTypes(67126932, LCID, 1, (9, 0), ((9, 1), (9, 1), (5, 1), (5, 1), (11, 1)),RootPoint
			, Axis, Radius, HalfAngle, IsExpanding)
		if ret is not None:
			ret = Dispatch(ret, 'CreateCone', '{5DF860A3-6B16-11D3-B794-0060B0F159EF}')
		return ret

	# Result is of type Cylinder
	def CreateCylinder(self, RootPoint=defaultNamedNotOptArg, Axis=defaultNamedNotOptArg, Radius=defaultNamedNotOptArg):
		'Method that creates a Cylinder object'
		ret = self._oleobj_.InvokeTypes(67126930, LCID, 1, (9, 0), ((9, 1), (9, 1), (5, 1)),RootPoint
			, Axis, Radius)
		if ret is not None:
			ret = Dispatch(ret, 'CreateCylinder', '{5DF860A2-6B16-11D3-B794-0060B0F159EF}')
		return ret

	# Result is of type EllipseFull
	def CreateEllipseFull(self, Center=defaultNamedNotOptArg, Normal=defaultNamedNotOptArg, MajorAxisVector=defaultNamedNotOptArg, MinorMajorRatio=defaultNamedNotOptArg):
		'Method that creates an EllipseFull object'
		ret = self._oleobj_.InvokeTypes(67126946, LCID, 1, (9, 0), ((9, 1), (9, 1), (9, 1), (5, 1)),Center
			, Normal, MajorAxisVector, MinorMajorRatio)
		if ret is not None:
			ret = Dispatch(ret, 'CreateEllipseFull', '{49CB4BB7-872A-11D3-8524-0060B0F0B5B7}')
		return ret

	# Result is of type EllipseFull2d
	def CreateEllipseFull2d(self, Center=defaultNamedNotOptArg, MajorAxisVector=defaultNamedNotOptArg, MinorMajorRatio=defaultNamedNotOptArg):
		'Method that creates an ElliseFull2d object'
		ret = self._oleobj_.InvokeTypes(67126949, LCID, 1, (9, 0), ((9, 1), (9, 1), (5, 1)),Center
			, MajorAxisVector, MinorMajorRatio)
		if ret is not None:
			ret = Dispatch(ret, 'CreateEllipseFull2d', '{49CB4BB8-872A-11D3-8524-0060B0F0B5B7}')
		return ret

	# Result is of type EllipticalArc
	def CreateEllipticalArc(self, Center=defaultNamedNotOptArg, MajorAxis=defaultNamedNotOptArg, MinorAxis=defaultNamedNotOptArg, MajorRadius=defaultNamedNotOptArg
			, MinorRadius=defaultNamedNotOptArg, StartAngle=defaultNamedNotOptArg, SweepAngle=defaultNamedNotOptArg):
		'Method that creates an EllipticalArc object'
		ret = self._oleobj_.InvokeTypes(67126950, LCID, 1, (9, 0), ((9, 1), (9, 1), (9, 1), (5, 1), (5, 1), (5, 1), (5, 1)),Center
			, MajorAxis, MinorAxis, MajorRadius, MinorRadius, StartAngle
			, SweepAngle)
		if ret is not None:
			ret = Dispatch(ret, 'CreateEllipticalArc', '{C1066E40-4E2F-45C2-A5AB-E2B4D1B84A1E}')
		return ret

	# Result is of type EllipticalArc2d
	def CreateEllipticalArc2d(self, Center=defaultNamedNotOptArg, MajorAxis=defaultNamedNotOptArg, MajorRadius=defaultNamedNotOptArg, MinorRadius=defaultNamedNotOptArg
			, StartAngle=defaultNamedNotOptArg, SweepAngle=defaultNamedNotOptArg):
		'Method that creates an EllipticalArc2d object'
		ret = self._oleobj_.InvokeTypes(67126951, LCID, 1, (9, 0), ((9, 1), (9, 1), (5, 1), (5, 1), (5, 1), (5, 1)),Center
			, MajorAxis, MajorRadius, MinorRadius, StartAngle, SweepAngle
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateEllipticalArc2d', '{C173A095-012F-11D5-8DEA-0010B541CAA8}')
		return ret

	# Result is of type EllipticalCone
	def CreateEllipticalCone(self, BasePoint=defaultNamedNotOptArg, AxisVector=defaultNamedNotOptArg, MajorAxisVector=defaultNamedNotOptArg, MinorMajorRatio=defaultNamedNotOptArg
			, HalfAngle=defaultNamedNotOptArg, IsExpanding=defaultNamedNotOptArg):
		'Method that creates an EllipticalCone object'
		ret = self._oleobj_.InvokeTypes(67126933, LCID, 1, (9, 0), ((9, 1), (9, 1), (9, 1), (5, 1), (5, 1), (11, 1)),BasePoint
			, AxisVector, MajorAxisVector, MinorMajorRatio, HalfAngle, IsExpanding
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateEllipticalCone', '{FA34A402-F063-11D3-B7A2-0060B0F159EF}')
		return ret

	# Result is of type EllipticalCylinder
	def CreateEllipticalCylinder(self, BasePoint=defaultNamedNotOptArg, AxisVector=defaultNamedNotOptArg, MajorAxisVector=defaultNamedNotOptArg, MinorMajorRatio=defaultNamedNotOptArg):
		'Method that creates an EllipticalCylinder object'
		ret = self._oleobj_.InvokeTypes(67126931, LCID, 1, (9, 0), ((9, 1), (9, 1), (9, 1), (5, 1)),BasePoint
			, AxisVector, MajorAxisVector, MinorMajorRatio)
		if ret is not None:
			ret = Dispatch(ret, 'CreateEllipticalCylinder', '{FA34A401-F063-11D3-B7A2-0060B0F159EF}')
		return ret

	# Result is of type BSplineCurve
	def CreateFittedBSplineCurve(self, Definition=defaultNamedNotOptArg):
		'Method that creates a new object using fit points. The definition of the curve is supplied using the input definition object. If an invalid curve is defined the method will fail. The object created is a transient mathematical object and is not displayed graphi'
		ret = self._oleobj_.InvokeTypes(67126942, LCID, 1, (9, 0), ((9, 1),),Definition
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateFittedBSplineCurve', '{49CB4BB9-872A-11D3-8524-0060B0F0B5B7}')
		return ret

	# Result is of type BSplineCurve2d
	def CreateFittedBSplineCurve2d(self, Definition=defaultNamedNotOptArg):
		'Method that creates a new object using fit points. The definition of the curve is supplied using the input definition object. If an invalid curve is defined the method will fail. The object created is a transient mathematical object and is not displayed graphi'
		ret = self._oleobj_.InvokeTypes(67126943, LCID, 1, (9, 0), ((9, 1),),Definition
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateFittedBSplineCurve2d', '{49CB4BBA-872A-11D3-8524-0060B0F0B5B7}')
		return ret

	# Result is of type Line
	def CreateLine(self, RootPoint=defaultNamedNotOptArg, Direction=defaultNamedNotOptArg):
		'Method that creates a Line object'
		ret = self._oleobj_.InvokeTypes(67126923, LCID, 1, (9, 0), ((9, 1), (9, 1)),RootPoint
			, Direction)
		if ret is not None:
			ret = Dispatch(ret, 'CreateLine', '{CB69F178-558E-11D3-B793-0060B0F159EF}')
		return ret

	# Result is of type Line2d
	def CreateLine2d(self, RootPoint=defaultNamedNotOptArg, Direction=defaultNamedNotOptArg):
		'Method that creates a Line2d object'
		ret = self._oleobj_.InvokeTypes(67126924, LCID, 1, (9, 0), ((9, 1), (9, 1)),RootPoint
			, Direction)
		if ret is not None:
			ret = Dispatch(ret, 'CreateLine2d', '{CB69F179-558E-11D3-B793-0060B0F159EF}')
		return ret

	# Result is of type LineSegment
	def CreateLineSegment(self, StartPoint=defaultNamedNotOptArg, EndPoint=defaultNamedNotOptArg):
		'Method that creates a LineSegment object'
		ret = self._oleobj_.InvokeTypes(67126947, LCID, 1, (9, 0), ((9, 1), (9, 1)),StartPoint
			, EndPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateLineSegment', '{607CC753-5796-4409-85F4-9EA576EAA417}')
		return ret

	# Result is of type LineSegment2d
	def CreateLineSegment2d(self, StartPoint=defaultNamedNotOptArg, EndPoint=defaultNamedNotOptArg):
		'Method that creates a LineSegment2d object'
		ret = self._oleobj_.InvokeTypes(67126948, LCID, 1, (9, 0), ((9, 1), (9, 1)),StartPoint
			, EndPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateLineSegment2d', '{C173A08D-012F-11D5-8DEA-0010B541CAA8}')
		return ret

	# Result is of type Matrix
	def CreateMatrix(self):
		'Method that creates a new 4x4 Matrix object. The matrix is initialized with an identity matrix.'
		ret = self._oleobj_.InvokeTypes(67126913, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CreateMatrix', '{CB69F171-558E-11D3-B793-0060B0F159EF}')
		return ret

	# Result is of type Matrix2d
	def CreateMatrix2d(self):
		'Method that creates a new 3x3 Matrix object. The matrix is initialized with an identity matrix.'
		ret = self._oleobj_.InvokeTypes(67126914, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CreateMatrix2d', '{DA33F19F-7C3F-11D3-B794-0060B0F159EF}')
		return ret

	# Result is of type OrientedBox
	def CreateOrientedBox(self, CornerPoint=defaultNamedOptArg, DirectionOne=defaultNamedOptArg, DirectionTwo=defaultNamedOptArg, DirectionThree=defaultNamedOptArg):
		'Method that creates a new oriented box object'
		ret = self._oleobj_.InvokeTypes(67126967, LCID, 1, (9, 0), ((12, 17), (12, 17), (12, 17), (12, 17)),CornerPoint
			, DirectionOne, DirectionTwo, DirectionThree)
		if ret is not None:
			ret = Dispatch(ret, 'CreateOrientedBox', '{556DCFA3-BD63-4B13-9C12-D99113AEAEFB}')
		return ret

	# Result is of type Plane
	def CreatePlane(self, RootPoint=defaultNamedNotOptArg, Normal=defaultNamedNotOptArg):
		'Method that creates a Plane object'
		ret = self._oleobj_.InvokeTypes(67126929, LCID, 1, (9, 0), ((9, 1), (9, 1)),RootPoint
			, Normal)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePlane', '{CB69F17A-558E-11D3-B793-0060B0F159EF}')
		return ret

	# Result is of type Plane
	def CreatePlaneByThreePoints(self, PointOne=defaultNamedNotOptArg, PointTwo=defaultNamedNotOptArg, PointThree=defaultNamedNotOptArg):
		'Method that creates a Plane object by three points'
		ret = self._oleobj_.InvokeTypes(67126956, LCID, 1, (9, 0), ((9, 1), (9, 1), (9, 1)),PointOne
			, PointTwo, PointThree)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePlaneByThreePoints', '{CB69F17A-558E-11D3-B793-0060B0F159EF}')
		return ret

	# Result is of type Point
	def CreatePoint(self, XCoord=0.0, YCoord=0.0, ZCoord=0.0):
		'Method that creates a new Point object.'
		ret = self._oleobj_.InvokeTypes(67126917, LCID, 1, (9, 0), ((5, 49), (5, 49), (5, 49)),XCoord
			, YCoord, ZCoord)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePoint', '{CB69F172-558E-11D3-B793-0060B0F159EF}')
		return ret

	# Result is of type Point2d
	def CreatePoint2d(self, XCoord=0.0, YCoord=0.0):
		'Method that creates a new Point2d object.'
		ret = self._oleobj_.InvokeTypes(67126918, LCID, 1, (9, 0), ((5, 49), (5, 49)),XCoord
			, YCoord)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePoint2d', '{CB69F173-558E-11D3-B793-0060B0F159EF}')
		return ret

	# Result is of type Polyline2d
	def CreatePolyline2d(self, Points=defaultNamedNotOptArg):
		'Creates a new Polyline2d object.  The object created is a transient mathematical object and is not displayed graphically'
		ret = self._oleobj_.InvokeTypes(67126959, LCID, 1, (9, 0), ((12, 1),),Points
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePolyline2d', '{2A1047EF-0B48-413B-92FD-6CA45A488DA6}')
		return ret

	# Result is of type Polyline2d
	def CreatePolyline2dFromCurve(self, Curve=defaultNamedNotOptArg, Tolerance=defaultNamedNotOptArg):
		'Creates a new Polyline2d object by approximating the input curve within the specified tolerance.  The object created is a transient mathematical object and is not displayed graphically'
		ret = self._oleobj_.InvokeTypes(67126961, LCID, 1, (9, 0), ((9, 1), (5, 1)),Curve
			, Tolerance)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePolyline2dFromCurve', '{2A1047EF-0B48-413B-92FD-6CA45A488DA6}')
		return ret

	# Result is of type Polyline3d
	def CreatePolyline3d(self, Points=defaultNamedNotOptArg):
		'Creates a new Polyline3d object.  The object created is a transient mathematical object and is not displayed graphically'
		ret = self._oleobj_.InvokeTypes(67126958, LCID, 1, (9, 0), ((12, 1),),Points
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePolyline3d', '{C9EBE756-798A-4E78-8CC4-DA91D7737321}')
		return ret

	# Result is of type Polyline3d
	def CreatePolyline3dFromCurve(self, Curve=defaultNamedNotOptArg, Tolerance=defaultNamedNotOptArg):
		'Creates a new Polyline3d object by approximating the input curve within the specified tolerance.  The object created is a transient mathematical object and is not displayed graphically'
		ret = self._oleobj_.InvokeTypes(67126960, LCID, 1, (9, 0), ((9, 1), (5, 1)),Curve
			, Tolerance)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePolyline3dFromCurve', '{C9EBE756-798A-4E78-8CC4-DA91D7737321}')
		return ret

	# Result is of type Sphere
	def CreateSphere(self, CenterPoint=defaultNamedNotOptArg, Radius=defaultNamedNotOptArg):
		'Method that creates a Sphere object'
		ret = self._oleobj_.InvokeTypes(67126934, LCID, 1, (9, 0), ((9, 1), (5, 1)),CenterPoint
			, Radius)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSphere', '{5DF860A5-6B16-11D3-B794-0060B0F159EF}')
		return ret

	# Result is of type Torus
	def CreateTorus(self, CenterPoint=defaultNamedNotOptArg, AxisVector=defaultNamedNotOptArg, MajorRadius=defaultNamedNotOptArg, MinorRadius=defaultNamedNotOptArg):
		'Method that creates a Torus object'
		ret = self._oleobj_.InvokeTypes(67126935, LCID, 1, (9, 0), ((9, 1), (9, 1), (5, 1), (5, 1)),CenterPoint
			, AxisVector, MajorRadius, MinorRadius)
		if ret is not None:
			ret = Dispatch(ret, 'CreateTorus', '{5DF860A4-6B16-11D3-B794-0060B0F159EF}')
		return ret

	# Result is of type UnitVector
	def CreateUnitVector(self, XCoord=0.0, YCoord=0.0, ZCoord=1.0):
		'Method that creates a new UnitVector object.'
		ret = self._oleobj_.InvokeTypes(67126921, LCID, 1, (9, 0), ((5, 49), (5, 49), (5, 49)),XCoord
			, YCoord, ZCoord)
		if ret is not None:
			ret = Dispatch(ret, 'CreateUnitVector', '{CB69F176-558E-11D3-B793-0060B0F159EF}')
		return ret

	# Result is of type UnitVector2d
	def CreateUnitVector2d(self, XCoord=0.0, YCoord=1.0):
		'Method that creates a new UnitVector2d object.'
		ret = self._oleobj_.InvokeTypes(67126922, LCID, 1, (9, 0), ((5, 49), (5, 49)),XCoord
			, YCoord)
		if ret is not None:
			ret = Dispatch(ret, 'CreateUnitVector2d', '{CB69F177-558E-11D3-B793-0060B0F159EF}')
		return ret

	# Result is of type Vector
	def CreateVector(self, XCoord=0.0, YCoord=0.0, ZCoord=0.0):
		'Method that creates a new Vector object.'
		ret = self._oleobj_.InvokeTypes(67126919, LCID, 1, (9, 0), ((5, 49), (5, 49), (5, 49)),XCoord
			, YCoord, ZCoord)
		if ret is not None:
			ret = Dispatch(ret, 'CreateVector', '{CB69F174-558E-11D3-B793-0060B0F159EF}')
		return ret

	# Result is of type Vector2d
	def CreateVector2d(self, XCoord=0.0, YCoord=0.0):
		'Method that creates a new Vector2d object.'
		ret = self._oleobj_.InvokeTypes(67126920, LCID, 1, (9, 0), ((5, 49), (5, 49)),XCoord
			, YCoord)
		if ret is not None:
			ret = Dispatch(ret, 'CreateVector2d', '{CB69F175-558E-11D3-B793-0060B0F159EF}')
		return ret

	# Result is of type ObjectsEnumerator
	def CurveCurveIntersection(self, CurveOne=defaultNamedNotOptArg, CurveTwo=defaultNamedNotOptArg, Tolerance=0.0):
		'Gets the intersection between the input curves'
		ret = self._oleobj_.InvokeTypes(67126962, LCID, 1, (9, 0), ((9, 1), (9, 1), (5, 49)),CurveOne
			, CurveTwo, Tolerance)
		if ret is not None:
			ret = Dispatch(ret, 'CurveCurveIntersection', '{A94DCF5E-90E9-4F60-BB55-F65B4618ECD5}')
		return ret

	# Result is of type ObjectsEnumerator
	def CurveSurfaceIntersection(self, Curve=defaultNamedNotOptArg, Surface=defaultNamedNotOptArg, Tolerance=0.0):
		'Gets the intersection between the input curve and the input surface'
		ret = self._oleobj_.InvokeTypes(67126963, LCID, 1, (9, 0), ((9, 1), (9, 1), (5, 49)),Curve
			, Surface, Tolerance)
		if ret is not None:
			ret = Dispatch(ret, 'CurveSurfaceIntersection', '{A94DCF5E-90E9-4F60-BB55-F65B4618ECD5}')
		return ret

	# Result is of type Point
	def GetFarmostPoint(self, Entity=defaultNamedNotOptArg, Direction=defaultNamedNotOptArg):
		'Gets the farmost point along the direction'
		ret = self._oleobj_.InvokeTypes(67126966, LCID, 1, (9, 0), ((9, 1), (9, 1)),Entity
			, Direction)
		if ret is not None:
			ret = Dispatch(ret, 'GetFarmostPoint', '{CB69F172-558E-11D3-B793-0060B0F159EF}')
		return ret

	# Result is of type ObjectsEnumerator
	def SurfaceSurfaceIntersection(self, SurfaceOne=defaultNamedNotOptArg, SurfaceTwo=defaultNamedNotOptArg, Tolerance=0.0):
		'Gets the intersection between the input surfaces'
		ret = self._oleobj_.InvokeTypes(67126964, LCID, 1, (9, 0), ((9, 1), (9, 1), (5, 49)),SurfaceOne
			, SurfaceTwo, Tolerance)
		if ret is not None:
			ret = Dispatch(ret, 'SurfaceSurfaceIntersection', '{A94DCF5E-90E9-4F60-BB55-F65B4618ECD5}')
		return ret

	_prop_map_get_ = {
		"PointTolerance": (67126957, 2, (5, 0), (), "PointTolerance", None),
		"Type": (2130706435, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{97ECB3AE-6C6E-4D8A-A91E-564314494EB8}", TransientGeometry )
