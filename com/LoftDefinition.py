# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 19:09:29 2023
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
class LoftDefinition(DispatchBaseClass):
	'Loft definition object'
	CLSID = IID('{FBEBA281-9346-4AC6-B324-6CEB7318BEBE}')
	coclass_clsid = None

	# Result is of type LoftDefinition
	def Copy(self):
		'Method that creates and returns a copy of this LoftDefinition'
		ret = self._oleobj_.InvokeTypes(83988242, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Copy', '{FBEBA281-9346-4AC6-B324-6CEB7318BEBE}')
		return ret

	_prop_map_get_ = {
		"Centerline": (83988225, 2, (9, 0), (), "Centerline", None),
		"Closed": (83988226, 2, (11, 0), (), "Closed", None),
		"FirstSectionAngle": (83988227, 2, (12, 0), (), "FirstSectionAngle", None),
		"FirstSectionCondition": (83988228, 2, (3, 0), (), "FirstSectionCondition", None),
		"FirstSectionDirectionReversed": (83988230, 2, (11, 0), (), "FirstSectionDirectionReversed", None),
		"FirstSectionImpact": (83988229, 2, (12, 0), (), "FirstSectionImpact", None),
		"FirstSectionTangentPlane": (83988231, 2, (9, 0), (), "FirstSectionTangentPlane", None),
		"LastSectionAngle": (83988232, 2, (12, 0), (), "LastSectionAngle", None),
		"LastSectionCondition": (83988233, 2, (3, 0), (), "LastSectionCondition", None),
		"LastSectionDirectionReversed": (83988235, 2, (11, 0), (), "LastSectionDirectionReversed", None),
		"LastSectionImpact": (83988234, 2, (12, 0), (), "LastSectionImpact", None),
		"LastSectionTangentPlane": (83988236, 2, (9, 0), (), "LastSectionTangentPlane", None),
		# Method 'LoftRails' returns object of type 'LoftRails'
		"LoftRails": (83988237, 2, (9, 0), (), "LoftRails", '{3E43E559-0053-402D-BE5F-4AC170C11A04}'),
		# Method 'LoftSectionDimensions' returns object of type 'LoftSectionDimensions'
		"LoftSectionDimensions": (83988244, 2, (9, 0), (), "LoftSectionDimensions", '{F8FBACE4-75A7-4493-B2D8-492AC937F3E5}'),
		"LoftType": (83988243, 2, (3, 0), (), "LoftType", None),
		# Method 'MapPointCurves' returns object of type 'MapPointCurves'
		"MapPointCurves": (83988238, 2, (9, 0), (), "MapPointCurves", '{E405BACE-0EE8-4427-B6BE-82CC11F9CC35}'),
		"MergeTangentFaces": (83988239, 2, (11, 0), (), "MergeTangentFaces", None),
		"Operation": (83988240, 2, (3, 0), (), "Operation", None),
		# Method 'Sections' returns object of type 'ObjectCollection'
		"Sections": (83988241, 2, (9, 0), (), "Sections", '{6939FFDD-BA10-11D2-B779-0060B0F159EF}'),
	}
	_prop_map_put_ = {
		"Centerline": ((83988225, LCID, 4, 0),()),
		"Closed": ((83988226, LCID, 4, 0),()),
		"FirstSectionAngle": ((83988227, LCID, 4, 0),()),
		"FirstSectionCondition": ((83988228, LCID, 4, 0),()),
		"FirstSectionDirectionReversed": ((83988230, LCID, 4, 0),()),
		"FirstSectionImpact": ((83988229, LCID, 4, 0),()),
		"FirstSectionTangentPlane": ((83988231, LCID, 4, 0),()),
		"LastSectionAngle": ((83988232, LCID, 4, 0),()),
		"LastSectionCondition": ((83988233, LCID, 4, 0),()),
		"LastSectionDirectionReversed": ((83988235, LCID, 4, 0),()),
		"LastSectionImpact": ((83988234, LCID, 4, 0),()),
		"LastSectionTangentPlane": ((83988236, LCID, 4, 0),()),
		"MapPointCurves": ((83988238, LCID, 4, 0),()),
		"MergeTangentFaces": ((83988239, LCID, 4, 0),()),
		"Operation": ((83988240, LCID, 4, 0),()),
		"Sections": ((83988241, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{FBEBA281-9346-4AC6-B324-6CEB7318BEBE}", LoftDefinition )
