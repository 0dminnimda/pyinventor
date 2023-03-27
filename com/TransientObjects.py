# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 19:06:09 2023
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
class TransientObjects(DispatchBaseClass):
	'Transient Object Factory Object'
	CLSID = IID('{6BA435D7-BBD6-11D4-8DE6-0010B541CAA8}')
	coclass_clsid = None

	# Result is of type Camera
	def CreateCamera(self):
		'Constructs a new Camera object.'
		ret = self._oleobj_.InvokeTypes(50350347, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CreateCamera', '{9C88D3AD-C3EB-11D3-B79E-0060B0F159EF}')
		return ret

	# Result is of type Color
	def CreateColor(self, Red=defaultNamedNotOptArg, Green=defaultNamedNotOptArg, Blue=defaultNamedNotOptArg, Opacity=1.0):
		'Constructs a new Color object.'
		ret = self._oleobj_.InvokeTypes(50350343, LCID, 1, (9, 0), ((17, 1), (17, 1), (17, 1), (5, 49)),Red
			, Green, Blue, Opacity)
		if ret is not None:
			ret = Dispatch(ret, 'CreateColor', '{0D084DAB-C766-4595-A449-7625772E88D2}')
		return ret

	# Result is of type DataMedium
	def CreateDataMedium(self):
		'Constructs a new DataMedium object'
		ret = self._oleobj_.InvokeTypes(50350338, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CreateDataMedium', '{6BA435DB-BBD6-11D4-8DE6-0010B541CAA8}')
		return ret

	# Result is of type EdgeCollection
	def CreateEdgeCollection(self, ObjectsEnumerator=defaultNamedOptArg):
		'Constructs a new EdgeCollection object. If an ObjectsEnumerator is passed in, the collection starts off containing the enumerated objects'
		ret = self._oleobj_.InvokeTypes(50350342, LCID, 1, (9, 0), ((12, 17),),ObjectsEnumerator
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateEdgeCollection', '{8DC730F1-A15F-4547-A279-69B7A9FAE657}')
		return ret

	# Result is of type FaceCollection
	def CreateFaceCollection(self, ObjectsEnumerator=defaultNamedOptArg):
		'Constructs a new FaceCollection object. If an ObjectsEnumerator is passed in, the collection starts off containing the enumerated objects'
		ret = self._oleobj_.InvokeTypes(50350344, LCID, 1, (9, 0), ((12, 17),),ObjectsEnumerator
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateFaceCollection', '{24B7B991-46D9-45F8-82CD-05212ECFC6DD}')
		return ret

	# Result is of type FileMetadata
	def CreateFileMetadata(self, FullFileName=defaultNamedOptArg):
		'Constructs a new FileMetadata object.'
		ret = self._oleobj_.InvokeTypes(50350346, LCID, 1, (9, 0), ((12, 17),),FullFileName
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateFileMetadata', '{BEE271DA-318F-471D-AF24-296B6F59B392}')
		return ret

	# Result is of type NameValueMap
	def CreateNameValueMap(self):
		'Constructs a new NameValueMap object'
		ret = self._oleobj_.InvokeTypes(50350339, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CreateNameValueMap', '{6BA435DD-BBD6-11D4-8DE6-0010B541CAA8}')
		return ret

	# Result is of type ObjectCollection
	def CreateObjectCollection(self, ObjectsEnumerator=defaultNamedOptArg):
		'Constructs a new ObjectCollection object. If an ObjectsEnumerator is passed in, the collection starts off containing the enumerated objects'
		ret = self._oleobj_.InvokeTypes(50350340, LCID, 1, (9, 0), ((12, 17),),ObjectsEnumerator
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateObjectCollection', '{6939FFDD-BA10-11D2-B779-0060B0F159EF}')
		return ret

	# Result is of type ObjectCollectionByVariant
	def CreateObjectCollectionByVariant(self, ObjectsEnumeratorByVariant=defaultNamedOptArg):
		'Constructs a new ObjectCollectionByVariant object. If an ObjectsEnumeratorByVariant is passed in, the collection starts off containing the enumerated objects'
		ret = self._oleobj_.InvokeTypes(50350341, LCID, 1, (9, 0), ((12, 17),),ObjectsEnumeratorByVariant
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateObjectCollectionByVariant', '{FD9487E1-57A9-419B-A365-14323D1B1CD9}')
		return ret

	def CreateSignatureString(self, StringToSign=defaultNamedNotOptArg):
		'Constructs a unique signature for a string'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(50350345, LCID, 1, (8, 0), ((8, 1),),StringToSign
			)

	# Result is of type TranslationContext
	def CreateTranslationContext(self):
		'Constructs a new TranslationContext object'
		ret = self._oleobj_.InvokeTypes(50350337, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CreateTranslationContext', '{6BA435D9-BBD6-11D4-8DE6-0010B541CAA8}')
		return ret

	_prop_map_get_ = {
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

win32com.client.CLSIDToClass.RegisterCLSID( "{6BA435D7-BBD6-11D4-8DE6-0010B541CAA8}", TransientObjects )
