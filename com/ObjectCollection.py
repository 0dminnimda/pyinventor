# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 19:06:44 2023
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
class ObjectCollection(DispatchBaseClass):
	'Generic collection of weakly-typed Object (IDispatch)'
	CLSID = IID('{6939FFDD-BA10-11D2-B779-0060B0F159EF}')
	coclass_clsid = None

	def Add(self, Object=defaultNamedNotOptArg):
		'Adds an object to the generic collection'
		return self._oleobj_.InvokeTypes(2130706446, LCID, 1, (24, 0), ((9, 1),),Object
			)

	def Clear(self):
		'Removes all objects from the generic collection'
		return self._oleobj_.InvokeTypes(2130706456, LCID, 1, (24, 0), (),)

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'Allows integer-indexed access to items in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', None)
		return ret

	def Remove(self, Index=defaultNamedNotOptArg):
		'Removes the specified object from the generic collection'
		return self._oleobj_.InvokeTypes(2130706447, LCID, 1, (24, 0), ((3, 1),),Index
			)

	def RemoveByObject(self, Object=defaultNamedNotOptArg):
		'Removes the specified object from the generic collection'
		return self._oleobj_.InvokeTypes(2130706473, LCID, 1, (24, 0), ((9, 1),),Object
			)

	_prop_map_get_ = {
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
			ret = Dispatch(ret, '__call__', None)
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
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2130706438, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

win32com.client.CLSIDToClass.RegisterCLSID( "{6939FFDD-BA10-11D2-B779-0060B0F159EF}", ObjectCollection )
