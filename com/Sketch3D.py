# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 18:41:00 2023
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
class Sketch3D(DispatchBaseClass):
	'3D Sketch Object'
	CLSID = IID('{E4C09561-E779-4A00-A835-E8D43E08A290}')
	coclass_clsid = None

	def Delete(self):
		'Deletes the sketch. This method is only valid for sketches that are not used by a feature'
		return self._oleobj_.InvokeTypes(83936265, LCID, 1, (24, 0), (),)

	def Edit(self):
		'Causes the 3D Sketch environment to be invoked with this sketch available for interactive edit'
		return self._oleobj_.InvokeTypes(83936264, LCID, 1, (24, 0), (),)

	def ExitEdit(self):
		'Causes the 3D Sketch environment to be closed and the user interface to return to the previous environment.  This is equivalent to the Return command.  This method is only valid in the case where this sketch is open for edit within the user interface'
		return self._oleobj_.InvokeTypes(83936266, LCID, 1, (24, 0), (),)

	def GetReferenceKey(self, ReferenceKey=defaultNamedNotOptArg, KeyContext=0):
		"Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object"
		return self._ApplyTypes_(2130706454, 1, (24, 0), ((24593, 3), (3, 49)), 'GetReferenceKey', None,ReferenceKey
			, KeyContext)

	# Result is of type SketchEntity3D
	def Include(self, Entity=defaultNamedNotOptArg):
		'Creates new reference sketch geometry by including the input entity onto the sketch'
		ret = self._oleobj_.InvokeTypes(83936261, LCID, 1, (9, 0), ((9, 1),),Entity
			)
		if ret is not None:
			ret = Dispatch(ret, 'Include', '{FD1878BB-56AD-44CD-9186-11BC84E584A4}')
		return ret

	def SetEndOfPart(self, Before=defaultNamedNotOptArg):
		'Method that repositions the end of part marker relative to the object'
		return self._oleobj_.InvokeTypes(2130706472, LCID, 1, (24, 0), ((11, 1),),Before
			)

	def Solve(self):
		'Method that causes the sketch to solve'
		return self._oleobj_.InvokeTypes(83936285, LCID, 1, (24, 0), (),)

	# Result is of type SketchEntity3D
	def _CrossPartInclude(self, Entity=defaultNamedNotOptArg, DestinationOccurrence=defaultNamedNotOptArg):
		'Creates new reference sketch geometry by including an input entity from another part onto the sketch'
		ret = self._oleobj_.InvokeTypes(83936275, LCID, 1, (9, 0), ((9, 1), (9, 1)),Entity
			, DestinationOccurrence)
		if ret is not None:
			ret = Dispatch(ret, '_CrossPartInclude', '{FD1878BB-56AD-44CD-9186-11BC84E584A4}')
		return ret

	_prop_map_get_ = {
		"Application": (2130706433, 2, (9, 0), (), "Application", None),
		# Method 'AttributeSets' returns object of type 'AttributeSets'
		"AttributeSets": (2130706452, 2, (9, 0), (), "AttributeSets", '{790B4EB3-7947-4D08-9510-372E93A24CF1}'),
		"CheckSumValue": (83936297, 2, (3, 0), (), "CheckSumValue", None),
		"Consumed": (83936278, 2, (11, 0), (), "Consumed", None),
		"DeferUpdates": (83936284, 2, (11, 0), (), "DeferUpdates", None),
		# Method 'Dependents' returns object of type 'ObjectsEnumerator'
		"Dependents": (83936267, 2, (9, 0), (), "Dependents", '{A94DCF5E-90E9-4F60-BB55-F65B4618ECD5}'),
		# Method 'DimensionConstraints3D' returns object of type 'DimensionConstraints3D'
		"DimensionConstraints3D": (83936286, 2, (9, 0), (), "DimensionConstraints3D", '{3C934EFD-E26A-4940-BA5A-66908C16AA92}'),
		"DimensionsVisible": (83936282, 2, (11, 0), (), "DimensionsVisible", None),
		"DisabledActionTypes": (83936281, 2, (3, 0), (), "DisabledActionTypes", None),
		"Exported": (83936290, 2, (11, 0), (), "Exported", None),
		# Method 'GeometricConstraints3D' returns object of type 'GeometricConstraints3D'
		"GeometricConstraints3D": (83936276, 2, (9, 0), (), "GeometricConstraints3D", '{85A24FF2-F0E9-4BC4-9A69-34F8C683B41A}'),
		"HasReferenceComponent": (83936269, 2, (11, 0), (), "HasReferenceComponent", None),
		"HealthStatus": (83936287, 2, (3, 0), (), "HealthStatus", None),
		# Method 'HelicalCurves' returns object of type 'HelicalCurves'
		"HelicalCurves": (83936296, 2, (9, 0), (), "HelicalCurves", '{B88938D1-2BE1-42D5-BD17-B4A7498C1B60}'),
		# Method 'IntersectionCurves' returns object of type 'IntersectionCurves'
		"IntersectionCurves": (83936294, 2, (9, 0), (), "IntersectionCurves", '{9F672C49-E28B-4239-8F7B-BF3FA7FD5071}'),
		"IsOwnedByFeature": (83936288, 2, (11, 0), (), "IsOwnedByFeature", None),
		"Name": (83936260, 2, (8, 0), (), "Name", None),
		# Method 'OnFaceCurves' returns object of type 'OnFaceCurves'
		"OnFaceCurves": (83936295, 2, (9, 0), (), "OnFaceCurves", '{A5620F8C-EEF1-4BD5-8C45-2C2327EFD42F}'),
		# Method 'OverrideColor' returns object of type 'Color'
		"OverrideColor": (83936279, 2, (9, 0), (), "OverrideColor", '{0D084DAB-C766-4595-A449-7625772E88D2}'),
		# Method 'OwnedBy' returns object of type 'PartFeature'
		"OwnedBy": (83936289, 2, (9, 0), (), "OwnedBy", '{DA33F1A4-7C3F-11D3-B794-0060B0F159EF}'),
		"Parent": (2130706434, 2, (9, 0), (), "Parent", None),
		# Method 'Profiles3D' returns object of type 'Profiles3D'
		"Profiles3D": (83936277, 2, (9, 0), (), "Profiles3D", '{B1340A33-EB0D-4609-BA1E-B98A3D173794}'),
		# Method 'ReferenceComponent' returns object of type 'ReferenceComponent'
		"ReferenceComponent": (83936270, 2, (9, 0), (), "ReferenceComponent", '{DD8AB7FC-77D4-4EA8-83A9-A0C868DABFC0}'),
		# Method 'ReferencedEntity' returns object of type 'Sketch3D'
		"ReferencedEntity": (83936268, 2, (9, 0), (), "ReferencedEntity", '{E4C09561-E779-4A00-A835-E8D43E08A290}'),
		"Shared": (83936283, 2, (11, 0), (), "Shared", None),
		# Method 'SilhouetteCurves' returns object of type 'SilhouetteCurves'
		"SilhouetteCurves": (83936291, 2, (9, 0), (), "SilhouetteCurves", '{B4F71C8B-BC8D-47F1-A327-9275F5FB443D}'),
		# Method 'SketchArcs3D' returns object of type 'SketchArcs3D'
		"SketchArcs3D": (83936259, 2, (9, 0), (), "SketchArcs3D", '{4AF3870E-AB8B-4567-94B5-C1850D292111}'),
		# Method 'SketchCircles3D' returns object of type 'SketchCircles3D'
		"SketchCircles3D": (83936271, 2, (9, 0), (), "SketchCircles3D", '{FA48B024-CC3B-458F-B0EB-6FE4CBEC35DD}'),
		# Method 'SketchControlPointSplines3D' returns object of type 'SketchControlPointSplines3D'
		"SketchControlPointSplines3D": (83936292, 2, (9, 0), (), "SketchControlPointSplines3D", '{745A04C4-8445-412A-AFA7-33E778DA3059}'),
		# Method 'SketchEllipses3D' returns object of type 'SketchEllipses3D'
		"SketchEllipses3D": (83936272, 2, (9, 0), (), "SketchEllipses3D", '{7A7BD889-E944-41FC-A34F-474465F0894E}'),
		# Method 'SketchEllipticalArcs3D' returns object of type 'SketchEllipticalArcs3D'
		"SketchEllipticalArcs3D": (83936273, 2, (9, 0), (), "SketchEllipticalArcs3D", '{08C74C78-5F8D-40B3-9D57-4507D5CEA79C}'),
		# Method 'SketchEntities3D' returns object of type 'SketchEntities3DEnumerator'
		"SketchEntities3D": (83936263, 2, (9, 0), (), "SketchEntities3D", '{6CBA9E79-C13B-46ED-BB14-6541A63B1A16}'),
		# Method 'SketchEquationCurves3D' returns object of type 'SketchEquationCurves3D'
		"SketchEquationCurves3D": (83936293, 2, (9, 0), (), "SketchEquationCurves3D", '{01BAC9F1-F900-4E57-9FDB-F12232AEC9D2}'),
		# Method 'SketchFixedSplines3D' returns object of type 'SketchFixedSplines3D'
		"SketchFixedSplines3D": (83936280, 2, (9, 0), (), "SketchFixedSplines3D", '{80DBF4D7-FEC3-454C-BF1C-65BCDB27188C}'),
		# Method 'SketchLines3D' returns object of type 'SketchLines3D'
		"SketchLines3D": (83936257, 2, (9, 0), (), "SketchLines3D", '{3A62D311-C21A-4DD3-83C0-A23507CA385E}'),
		# Method 'SketchPoints3D' returns object of type 'SketchPoints3D'
		"SketchPoints3D": (83936258, 2, (9, 0), (), "SketchPoints3D", '{3BCDEC54-2F73-4114-A7CB-ACF5E823B67D}'),
		# Method 'SketchSplines3D' returns object of type 'SketchSplines3D'
		"SketchSplines3D": (83936274, 2, (9, 0), (), "SketchSplines3D", '{611271CA-48EE-4EBF-9ACD-CCD081142400}'),
		"Type": (0, 2, (3, 0), (), "Type", None),
		"Visible": (83936262, 2, (11, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"DeferUpdates": ((83936284, LCID, 4, 0),()),
		"DimensionsVisible": ((83936282, LCID, 4, 0),()),
		"DisabledActionTypes": ((83936281, LCID, 4, 0),()),
		"Exported": ((83936290, LCID, 4, 0),()),
		"Name": ((83936260, LCID, 4, 0),()),
		"OverrideColor": ((83936279, LCID, 4, 0),()),
		"Shared": ((83936283, LCID, 4, 0),()),
		"Visible": ((83936262, LCID, 4, 0),()),
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

win32com.client.CLSIDToClass.RegisterCLSID( "{E4C09561-E779-4A00-A835-E8D43E08A290}", Sketch3D )
