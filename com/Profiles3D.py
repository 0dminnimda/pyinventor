# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 18:49:56 2023
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
class Profiles3D(DispatchBaseClass):
	'Profiles3D Collection Object'
	CLSID = IID('{B1340A33-EB0D-4609-BA1E-B98A3D173794}')
	coclass_clsid = None

	# Result is of type Profile3D
	def AddClosed(self):
		'Creates a new 3d profile by taking all of the entities in the sketch and creating as many closed paths as possible'
		ret = self._oleobj_.InvokeTypes(83949825, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'AddClosed', '{2A8678EA-A024-469A-80DC-D1EAD67847A3}')
		return ret

	# Result is of type Profile3D
	def AddOpen(self):
		'Creates a new 3d profile by finding a set of connected entities.  The result can be either open or closed'
		ret = self._oleobj_.InvokeTypes(83949826, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'AddOpen', '{2A8678EA-A024-469A-80DC-D1EAD67847A3}')
		return ret

	# Result is of type Profile3D
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'Allows integer-indexed access to items in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{2A8678EA-A024-469A-80DC-D1EAD67847A3}')
		return ret

	_prop_map_get_ = {
		"Application": (2130706433, 2, (9, 0), (), "Application", None),
		"Count": (2130706438, 2, (3, 0), (), "Count", None),
		"Type": (2130706435, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Allows integer-indexed access to items in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{2A8678EA-A024-469A-80DC-D1EAD67847A3}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{2A8678EA-A024-469A-80DC-D1EAD67847A3}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2130706438, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

win32com.client.CLSIDToClass.RegisterCLSID( "{B1340A33-EB0D-4609-BA1E-B98A3D173794}", Profiles3D )
