# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 18:50:13 2023
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
class Profile3D(DispatchBaseClass):
	'Profile3D Object'
	CLSID = IID('{2A8678EA-A024-469A-80DC-D1EAD67847A3}')
	coclass_clsid = None

	def Delete(self):
		'Deletes this Profile3D object.  This is only valid for Profile3D objects that do not have a dependent feature'
		return self._oleobj_.InvokeTypes(83950081, LCID, 1, (24, 0), (),)

	def GetReferenceKey(self, ReferenceKey=defaultNamedNotOptArg, KeyContext=0):
		"Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object"
		return self._ApplyTypes_(2130706454, 1, (24, 0), ((24593, 3), (3, 49)), 'GetReferenceKey', None,ReferenceKey
			, KeyContext)

	# Result is of type ProfilePath3D
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'Allows integer-indexed access to items in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{D7347916-69D8-4972-AEBE-95BE5672BED2}')
		return ret

	_prop_map_get_ = {
		"Application": (2130706433, 2, (9, 0), (), "Application", None),
		# Method 'AttributeSets' returns object of type 'AttributeSets'
		"AttributeSets": (2130706452, 2, (9, 0), (), "AttributeSets", '{790B4EB3-7947-4D08-9510-372E93A24CF1}'),
		"Count": (2130706438, 2, (3, 0), (), "Count", None),
		# Method 'Parent' returns object of type 'Sketch3D'
		"Parent": (2130706434, 2, (9, 0), (), "Parent", '{E4C09561-E779-4A00-A835-E8D43E08A290}'),
		"Type": (2130706435, 2, (3, 0), (), "Type", None),
		# Method 'Wires' returns object of type 'Wires'
		"Wires": (83950082, 2, (9, 0), (), "Wires", '{31B11F76-0E31-45DF-8BE6-409EE5416DC5}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Allows integer-indexed access to items in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{D7347916-69D8-4972-AEBE-95BE5672BED2}')
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
		return win32com.client.util.Iterator(ob, '{D7347916-69D8-4972-AEBE-95BE5672BED2}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2130706438, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

win32com.client.CLSIDToClass.RegisterCLSID( "{2A8678EA-A024-469A-80DC-D1EAD67847A3}", Profile3D )
