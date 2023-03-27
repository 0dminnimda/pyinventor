# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 18:45:37 2023
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
class SketchLine3D(DispatchBaseClass):
	'SketchLine3D Object'
	CLSID = IID('{87056D9A-B0B2-4BD0-A6EC-51E9D893A502}')
	coclass_clsid = None

	def Delete(self):
		'Deletes this object'
		return self._oleobj_.InvokeTypes(83936772, LCID, 1, (24, 0), (),)

	def GetReferenceKey(self, ReferenceKey=defaultNamedNotOptArg, KeyContext=0):
		"Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object"
		return self._ApplyTypes_(2130706454, 1, (24, 0), ((24593, 3), (3, 49)), 'GetReferenceKey', None,ReferenceKey
			, KeyContext)

	_prop_map_get_ = {
		"Application": (2130706433, 2, (9, 0), (), "Application", None),
		"AssociativeID": (83936780, 2, (3, 0), (), "AssociativeID", None),
		# Method 'AttributeSets' returns object of type 'AttributeSets'
		"AttributeSets": (2130706452, 2, (9, 0), (), "AttributeSets", '{790B4EB3-7947-4D08-9510-372E93A24CF1}'),
		"ConstraintStatus": (83936778, 2, (3, 0), (), "ConstraintStatus", None),
		# Method 'Constraints3D' returns object of type 'SketchConstraints3DEnumerator'
		"Constraints3D": (83936775, 2, (9, 0), (), "Constraints3D", '{85C83167-947D-46E2-A802-92D529B48E37}'),
		"Construction": (83936776, 2, (11, 0), (), "Construction", None),
		"EndPoint": (83937281, 2, (9, 0), (), "EndPoint", None),
		# Method 'EndSketchPoint' returns object of type 'SketchPoint3D'
		"EndSketchPoint": (83937285, 2, (9, 0), (), "EndSketchPoint", '{2307500B-D075-4F5D-815D-7A1B8E90B20C}'),
		# Method 'Geometry' returns object of type 'LineSegment'
		"Geometry": (83937283, 2, (9, 0), (), "Geometry", '{607CC753-5796-4409-85F4-9EA576EAA417}'),
		"HasReferenceComponent": (83936773, 2, (11, 0), (), "HasReferenceComponent", None),
		"Length": (83937284, 2, (5, 0), (), "Length", None),
		# Method 'OwnedBy' returns object of type 'SketchEntities3DEnumerator'
		"OwnedBy": (83936777, 2, (9, 0), (), "OwnedBy", '{6CBA9E79-C13B-46ED-BB14-6541A63B1A16}'),
		# Method 'Parent' returns object of type 'Sketch3D'
		"Parent": (2130706434, 2, (9, 0), (), "Parent", '{E4C09561-E779-4A00-A835-E8D43E08A290}'),
		# Method 'RangeBox' returns object of type 'Box'
		"RangeBox": (83936770, 2, (9, 0), (), "RangeBox", '{5DF86062-6B16-11D3-B794-0060B0F159EF}'),
		"Reference": (83936771, 2, (11, 0), (), "Reference", None),
		# Method 'ReferenceComponent' returns object of type 'ReferenceComponent'
		"ReferenceComponent": (83936774, 2, (9, 0), (), "ReferenceComponent", '{DD8AB7FC-77D4-4EA8-83A9-A0C868DABFC0}'),
		"ReferencedEntity": (83936769, 2, (9, 0), (), "ReferencedEntity", None),
		"StartPoint": (83937282, 2, (9, 0), (), "StartPoint", None),
		# Method 'StartSketchPoint' returns object of type 'SketchPoint3D'
		"StartSketchPoint": (83937286, 2, (9, 0), (), "StartSketchPoint", '{2307500B-D075-4F5D-815D-7A1B8E90B20C}'),
		"Type": (2130706435, 2, (3, 0), (), "Type", None),
		"_GeometryMoveableStatus": (83936779, 2, (3, 0), (), "_GeometryMoveableStatus", None),
	}
	_prop_map_put_ = {
		"Construction": ((83936776, LCID, 4, 0),()),
		"Geometry": ((83937283, LCID, 4, 0),()),
		"Reference": ((83936771, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{87056D9A-B0B2-4BD0-A6EC-51E9D893A502}", SketchLine3D )
