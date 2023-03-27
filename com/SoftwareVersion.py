# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 15:31:30 2023
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
class SoftwareVersion(DispatchBaseClass):
	'Object that encapsulates a given Software Version. Used in various contexts'
	CLSID = IID('{076C16D1-4994-11D4-9E0F-0010A4C72F07}')
	coclass_clsid = None

	_prop_map_get_ = {
		"BetaVersion": (50345733, 2, (3, 0), (), "BetaVersion", None),
		"BuildIdentifier": (50345735, 2, (3, 0), (), "BuildIdentifier", None),
		"DisplayName": (50345732, 2, (8, 0), (), "DisplayName", None),
		"DisplayVersion": (50345741, 2, (8, 0), (), "DisplayVersion", None),
		"Is64BitVersion": (50345739, 2, (11, 0), (), "Is64BitVersion", None),
		"IsEducationVersion": (50345742, 2, (11, 0), (), "IsEducationVersion", None),
		"Major": (50345729, 2, (3, 0), (), "Major", None),
		"Minor": (50345730, 2, (3, 0), (), "Minor", None),
		"NotProduction": (50345734, 2, (11, 0), (), "NotProduction", None),
		"ProductEdition": (50345740, 2, (3, 0), (), "ProductEdition", None),
		"ProductName": (50345743, 2, (8, 0), (), "ProductName", None),
		"ServicePack": (50345731, 2, (3, 0), (), "ServicePack", None),
		"Type": (0, 2, (3, 0), (), "Type", None),
		"_DebugBuildIdentifier": (50345737, 2, (3, 0), (), "_DebugBuildIdentifier", None),
		"_InternalBuildIdentifier": (50345736, 2, (3, 0), (), "_InternalBuildIdentifier", None),
		"_PatchBuildIdentifier": (50345738, 2, (3, 0), (), "_PatchBuildIdentifier", None),
	}
	_prop_map_put_ = {
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

win32com.client.CLSIDToClass.RegisterCLSID( "{076C16D1-4994-11D4-9E0F-0010A4C72F07}", SoftwareVersion )
