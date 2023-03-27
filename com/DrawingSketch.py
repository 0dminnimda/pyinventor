# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 18:22:36 2023
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
class DrawingSketch(DispatchBaseClass):
	'Drawing Sketch Object'
	CLSID = IID('{1644E1D5-9BD5-11D5-8DF7-0010B541CAA8}')
	coclass_clsid = None

	# Result is of type SketchEntitiesEnumerator
	def AddArcSlotByCenterPointArc(self, CenterPoint=defaultNamedNotOptArg, StartPoint=defaultNamedNotOptArg, SweepAngle=defaultNamedNotOptArg, Width=defaultNamedNotOptArg):
		'Method that creates an arc slot. The sketch entities represent the sketch slot are returned.'
		ret = self._oleobj_.InvokeTypes(83890736, LCID, 1, (9, 0), ((9, 1), (9, 1), (5, 1), (5, 1)),CenterPoint
			, StartPoint, SweepAngle, Width)
		if ret is not None:
			ret = Dispatch(ret, 'AddArcSlotByCenterPointArc', '{B546124B-09AA-11D5-8DEC-0010B541CAA8}')
		return ret

	# Result is of type SketchEntitiesEnumerator
	def AddArcSlotByThreePointArc(self, StartPoint=defaultNamedNotOptArg, MidPoint=defaultNamedNotOptArg, EndPoint=defaultNamedNotOptArg, Width=defaultNamedNotOptArg):
		'Method that creates an arc slot. The sketch entities represent the sketch slot are returned.'
		ret = self._oleobj_.InvokeTypes(83890735, LCID, 1, (9, 0), ((9, 1), (9, 1), (9, 1), (5, 1)),StartPoint
			, MidPoint, EndPoint, Width)
		if ret is not None:
			ret = Dispatch(ret, 'AddArcSlotByThreePointArc', '{B546124B-09AA-11D5-8DEC-0010B541CAA8}')
		return ret

	# Result is of type SketchEntity
	def AddByProjectingEntity(self, Entity=defaultNamedNotOptArg):
		'Creates new reference sketch geometry by projecting the input entity onto the sketch plane'
		ret = self._oleobj_.InvokeTypes(83890723, LCID, 1, (9, 0), ((9, 1),),Entity
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddByProjectingEntity', '{B546124D-09AA-11D5-8DEC-0010B541CAA8}')
		return ret

	# Result is of type SketchEntitiesEnumerator
	def AddStraightSlotByCenterToCenter(self, StartPoint=defaultNamedNotOptArg, EndPoint=defaultNamedNotOptArg, Width=defaultNamedNotOptArg):
		'Method that creates a straight slot. The sketch entities represent the sketch slot are returned.'
		ret = self._oleobj_.InvokeTypes(83890732, LCID, 1, (9, 0), ((9, 1), (9, 1), (5, 1)),StartPoint
			, EndPoint, Width)
		if ret is not None:
			ret = Dispatch(ret, 'AddStraightSlotByCenterToCenter', '{B546124B-09AA-11D5-8DEC-0010B541CAA8}')
		return ret

	# Result is of type SketchEntitiesEnumerator
	def AddStraightSlotByOverall(self, StartPoint=defaultNamedNotOptArg, EndPoint=defaultNamedNotOptArg, Width=defaultNamedNotOptArg):
		'Method that creates a straight slot. The sketch entities represent the sketch slot are returned.'
		ret = self._oleobj_.InvokeTypes(83890733, LCID, 1, (9, 0), ((9, 1), (9, 1), (5, 1)),StartPoint
			, EndPoint, Width)
		if ret is not None:
			ret = Dispatch(ret, 'AddStraightSlotByOverall', '{B546124B-09AA-11D5-8DEC-0010B541CAA8}')
		return ret

	# Result is of type SketchEntitiesEnumerator
	def AddStraightSlotBySlotCenter(self, CenterPoint=defaultNamedNotOptArg, EndPoint=defaultNamedNotOptArg, Width=defaultNamedNotOptArg):
		'Method that creates a straight slot. The sketch entities represent the sketch slot are returned.'
		ret = self._oleobj_.InvokeTypes(83890734, LCID, 1, (9, 0), ((9, 1), (9, 1), (5, 1)),CenterPoint
			, EndPoint, Width)
		if ret is not None:
			ret = Dispatch(ret, 'AddStraightSlotBySlotCenter', '{B546124B-09AA-11D5-8DEC-0010B541CAA8}')
		return ret

	def CopyContentsTo(self, TargetSketch=defaultNamedNotOptArg):
		'Method that copies all the contents of the sketch to the input target sketch'
		return self._oleobj_.InvokeTypes(83890729, LCID, 1, (24, 0), ((9, 1),),TargetSketch
			)

	def Delete(self):
		'Deletes the sketch. This method is only valid for sketches that are not used by a feature'
		return self._oleobj_.InvokeTypes(83890710, LCID, 1, (24, 0), (),)

	def Edit(self):
		'Causes the Sketch environment to be invoked with this sketch available for interactive edit'
		return self._oleobj_.InvokeTypes(83890709, LCID, 1, (24, 0), (),)

	def ExitEdit(self):
		'Causes the Sketch environment to be closed and the user interface to return to the previous environment.  This is equivalent to the Return command.  This method is only valid in the case where this sketch is open for edit within the user interface'
		return self._oleobj_.InvokeTypes(83890711, LCID, 1, (24, 0), (),)

	def GetAutomatedCenterlineSettings(self, AutomatedCenterlineSettings=pythoncom.Missing):
		'Gets the settings that define how automatic center lines and center marks are to be calculated for this sketch'
		return self._ApplyTypes_(117443334, 1, (24, 0), ((16393, 2),), 'GetAutomatedCenterlineSettings', None,AutomatedCenterlineSettings
			)

	def GetCustomLineType(self, LineTypeName=pythoncom.Missing, LineTypeDescription=pythoncom.Missing):
		'Method that returns information regarding the custom line type in use'
		return self._ApplyTypes_(83890727, 1, (24, 0), ((16392, 2), (16392, 2)), 'GetCustomLineType', None,LineTypeName
			, LineTypeDescription)

	def GetReferenceKey(self, ReferenceKey=defaultNamedNotOptArg, KeyContext=0):
		"Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object"
		return self._ApplyTypes_(2130706454, 1, (24, 0), ((24593, 3), (3, 49)), 'GetReferenceKey', None,ReferenceKey
			, KeyContext)

	# Result is of type ObjectsEnumerator
	def MoveSketchObjects(self, SketchObjects=defaultNamedNotOptArg, Vector=defaultNamedNotOptArg, Copy=False, RemoveConstraints=False):
		'Moves a collection of sketch objects'
		ret = self._oleobj_.InvokeTypes(83890714, LCID, 1, (9, 0), ((9, 1), (9, 1), (11, 49), (11, 49)),SketchObjects
			, Vector, Copy, RemoveConstraints)
		if ret is not None:
			ret = Dispatch(ret, 'MoveSketchObjects', '{A94DCF5E-90E9-4F60-BB55-F65B4618ECD5}')
		return ret

	# Result is of type SketchEntitiesEnumerator
	def OffsetSketchEntitiesUsingDistance(self, SketchEntities=defaultNamedNotOptArg, OffsetDistance=defaultNamedNotOptArg, NaturalOffsetDirection=defaultNamedNotOptArg, IncludeConnectedEntities=False
			, CreateOffsetConstraints=True):
		'Offsets a collection of sketch objects'
		ret = self._oleobj_.InvokeTypes(83890721, LCID, 1, (9, 0), ((9, 1), (5, 1), (11, 1), (11, 49), (11, 49)),SketchEntities
			, OffsetDistance, NaturalOffsetDirection, IncludeConnectedEntities, CreateOffsetConstraints)
		if ret is not None:
			ret = Dispatch(ret, 'OffsetSketchEntitiesUsingDistance', '{B546124B-09AA-11D5-8DEC-0010B541CAA8}')
		return ret

	# Result is of type SketchEntitiesEnumerator
	def OffsetSketchEntitiesUsingPoint(self, SketchEntities=defaultNamedNotOptArg, OffsetPoint=defaultNamedNotOptArg, IncludeConnectedEntities=False, CreateOffsetConstraints=True):
		'Offsets a collection of sketch objects'
		ret = self._oleobj_.InvokeTypes(83890722, LCID, 1, (9, 0), ((9, 1), (9, 1), (11, 49), (11, 49)),SketchEntities
			, OffsetPoint, IncludeConnectedEntities, CreateOffsetConstraints)
		if ret is not None:
			ret = Dispatch(ret, 'OffsetSketchEntitiesUsingPoint', '{B546124B-09AA-11D5-8DEC-0010B541CAA8}')
		return ret

	# Result is of type ObjectsEnumerator
	def RotateSketchObjects(self, SketchObjects=defaultNamedNotOptArg, CenterPoint=defaultNamedNotOptArg, Angle=defaultNamedNotOptArg, Copy=False
			, RemoveConstraints=False):
		'Rotates a collection of sketch objects'
		ret = self._oleobj_.InvokeTypes(83890715, LCID, 1, (9, 0), ((9, 1), (9, 1), (5, 1), (11, 49), (11, 49)),SketchObjects
			, CenterPoint, Angle, Copy, RemoveConstraints)
		if ret is not None:
			ret = Dispatch(ret, 'RotateSketchObjects', '{A94DCF5E-90E9-4F60-BB55-F65B4618ECD5}')
		return ret

	# Result is of type ObjectsEnumerator
	def SetAutomatedCenterlineSettings(self, AutomatedCenterlineSettings=defaultNamedOptArg):
		'Sets the automatic centerline and center mark settings for this sketch and creates the centerlines and center marks defined by the settings'
		ret = self._oleobj_.InvokeTypes(117443335, LCID, 1, (9, 0), ((12, 17),),AutomatedCenterlineSettings
			)
		if ret is not None:
			ret = Dispatch(ret, 'SetAutomatedCenterlineSettings', '{A94DCF5E-90E9-4F60-BB55-F65B4618ECD5}')
		return ret

	def SetCustomLineType(self, FullFileName=defaultNamedNotOptArg, LineTypeName=defaultNamedNotOptArg, ReplaceExisting=defaultNamedNotOptArg):
		'Method that sets a custom line type to the curve from the specified .lin file'
		return self._oleobj_.InvokeTypes(83890728, LCID, 1, (24, 0), ((8, 1), (8, 1), (11, 1)),FullFileName
			, LineTypeName, ReplaceExisting)

	# Result is of type Point2d
	def SheetToSketchSpace(self, SheetCoordinate=defaultNamedNotOptArg):
		'Method that takes a coordinate in sheet space returns a Point2d object containing the resulting coordinate point in sketch space'
		ret = self._oleobj_.InvokeTypes(117443330, LCID, 1, (9, 0), ((9, 1),),SheetCoordinate
			)
		if ret is not None:
			ret = Dispatch(ret, 'SheetToSketchSpace', '{CB69F173-558E-11D3-B793-0060B0F159EF}')
		return ret

	# Result is of type Point2d
	def SketchToSheetSpace(self, SketchCoordinate=defaultNamedNotOptArg):
		'Method that takes a coordinate in sketch space, and returns a Point2d object containing the coordinates of the point in sheet space'
		ret = self._oleobj_.InvokeTypes(117443331, LCID, 1, (9, 0), ((9, 1),),SketchCoordinate
			)
		if ret is not None:
			ret = Dispatch(ret, 'SketchToSheetSpace', '{CB69F173-558E-11D3-B793-0060B0F159EF}')
		return ret

	def Solve(self):
		'Method that causes the sketch to solve'
		return self._oleobj_.InvokeTypes(83890719, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Application": (2130706433, 2, (9, 0), (), "Application", None),
		# Method 'AttributeSets' returns object of type 'AttributeSets'
		"AttributeSets": (2130706452, 2, (9, 0), (), "AttributeSets", '{790B4EB3-7947-4D08-9510-372E93A24CF1}'),
		# Method 'Color' returns object of type 'Color'
		"Color": (83890724, 2, (9, 0), (), "Color", '{0D084DAB-C766-4595-A449-7625772E88D2}'),
		"ConstraintStatus": (83890717, 2, (3, 0), (), "ConstraintStatus", None),
		# Method 'DataIO' returns object of type 'DataIO'
		"DataIO": (83890689, 2, (9, 0), (), "DataIO", '{FBCADB33-9CBE-11D3-B799-0060B0F159EF}'),
		"DeferUpdates": (83890718, 2, (11, 0), (), "DeferUpdates", None),
		# Method 'DimensionConstraints' returns object of type 'DimensionConstraints'
		"DimensionConstraints": (83890697, 2, (9, 0), (), "DimensionConstraints", '{C173A075-012F-11D5-8DEA-0010B541CAA8}'),
		"DisabledActionTypes": (83890713, 2, (3, 0), (), "DisabledActionTypes", None),
		# Method 'GeometricConstraints' returns object of type 'GeometricConstraints'
		"GeometricConstraints": (83890696, 2, (9, 0), (), "GeometricConstraints", '{8006A072-ECC4-11D4-8DE9-0010B541CAA8}'),
		"LineType": (83890725, 2, (3, 0), (), "LineType", None),
		"LineWeight": (83890726, 2, (5, 0), (), "LineWeight", None),
		"Name": (83890694, 2, (8, 0), (), "Name", None),
		"Parent": (2130706434, 2, (9, 0), (), "Parent", None),
		# Method 'Profiles' returns object of type 'Profiles'
		"Profiles": (117443332, 2, (9, 0), (), "Profiles", '{523EF757-245A-11D5-8DEC-0010B541CAA8}'),
		# Method 'SketchArcs' returns object of type 'SketchArcs'
		"SketchArcs": (83890699, 2, (9, 0), (), "SketchArcs", '{8006A032-ECC4-11D4-8DE9-0010B541CAA8}'),
		# Method 'SketchCircles' returns object of type 'SketchCircles'
		"SketchCircles": (83890703, 2, (9, 0), (), "SketchCircles", '{8006A038-ECC4-11D4-8DE9-0010B541CAA8}'),
		# Method 'SketchControlPointSplines' returns object of type 'SketchControlPointSplines'
		"SketchControlPointSplines": (83890730, 2, (9, 0), (), "SketchControlPointSplines", '{135F0952-BF41-444D-A962-8A7805AB2E78}'),
		# Method 'SketchEllipses' returns object of type 'SketchEllipses'
		"SketchEllipses": (83890701, 2, (9, 0), (), "SketchEllipses", '{8006A036-ECC4-11D4-8DE9-0010B541CAA8}'),
		# Method 'SketchEllipticalArcs' returns object of type 'SketchEllipticalArcs'
		"SketchEllipticalArcs": (83890702, 2, (9, 0), (), "SketchEllipticalArcs", '{C173A089-012F-11D5-8DEA-0010B541CAA8}'),
		# Method 'SketchEntities' returns object of type 'SketchEntitiesEnumerator'
		"SketchEntities": (83890698, 2, (9, 0), (), "SketchEntities", '{B546124B-09AA-11D5-8DEC-0010B541CAA8}'),
		# Method 'SketchEquationCurves' returns object of type 'SketchEquationCurves'
		"SketchEquationCurves": (83890731, 2, (9, 0), (), "SketchEquationCurves", '{C38DE680-2374-487B-86F8-E3DA8012DE66}'),
		# Method 'SketchFillRegions' returns object of type 'SketchFillRegions'
		"SketchFillRegions": (117443333, 2, (9, 0), (), "SketchFillRegions", '{A7993C2A-CFCA-4455-BC79-B15952DBF102}'),
		# Method 'SketchFixedSplines' returns object of type 'SketchFixedSplines'
		"SketchFixedSplines": (83890712, 2, (9, 0), (), "SketchFixedSplines", '{6359FE67-0814-4847-9F33-72E0BB9EB688}'),
		# Method 'SketchImages' returns object of type 'SketchImages'
		"SketchImages": (83890720, 2, (9, 0), (), "SketchImages", '{64D6BFDF-5B47-48C1-AC74-1BE2C24757B2}'),
		# Method 'SketchLines' returns object of type 'SketchLines'
		"SketchLines": (83890690, 2, (9, 0), (), "SketchLines", '{8006A018-ECC4-11D4-8DE9-0010B541CAA8}'),
		# Method 'SketchOffsetSplines' returns object of type 'SketchOffsetSplines'
		"SketchOffsetSplines": (83890704, 2, (9, 0), (), "SketchOffsetSplines", '{16372AAE-1133-4C4C-9A48-D9305D8358F3}'),
		# Method 'SketchPoints' returns object of type 'SketchPoints'
		"SketchPoints": (83890691, 2, (9, 0), (), "SketchPoints", '{8006A024-ECC4-11D4-8DE9-0010B541CAA8}'),
		# Method 'SketchSplines' returns object of type 'SketchSplines'
		"SketchSplines": (83890700, 2, (9, 0), (), "SketchSplines", '{8006A034-ECC4-11D4-8DE9-0010B541CAA8}'),
		# Method 'TextBoxes' returns object of type 'TextBoxes'
		"TextBoxes": (83890716, 2, (9, 0), (), "TextBoxes", '{A907AE97-A78F-11D5-8DF8-0010B541CAA8}'),
		"Type": (0, 2, (3, 0), (), "Type", None),
		"Visible": (83890695, 2, (11, 0), (), "Visible", None),
		# Method '_TextBoxes' returns object of type 'TextBoxes'
		"_TextBoxes": (117443329, 2, (9, 0), (), "_TextBoxes", '{A907AE97-A78F-11D5-8DF8-0010B541CAA8}'),
	}
	_prop_map_put_ = {
		"Color": ((83890724, LCID, 4, 0),()),
		"DeferUpdates": ((83890718, LCID, 4, 0),()),
		"DisabledActionTypes": ((83890713, LCID, 4, 0),()),
		"LineType": ((83890725, LCID, 4, 0),()),
		"LineWeight": ((83890726, LCID, 4, 0),()),
		"Name": ((83890694, LCID, 4, 0),()),
		"Visible": ((83890695, LCID, 4, 0),()),
	}
	# Default property for this class is 'Type'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (3, 0), (), "Type", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{1644E1D5-9BD5-11D5-8DF7-0010B541CAA8}", DrawingSketch )
