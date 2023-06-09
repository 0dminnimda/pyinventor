# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 14:15:59 2023
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
class Documents(DispatchBaseClass):
	'Documents collection Object'
	CLSID = IID('{70109AA2-63C1-11D2-B78B-0060B0EC020B}')
	coclass_clsid = None

	# Result is of type Document
	def Add(self, DocumentType=defaultNamedNotOptArg, TemplateFileName='', CreateVisible=True):
		'Creates a new Document of the specified type. Optionally, a template file can be specified instead'
		return self._ApplyTypes_(50332417, 1, (9, 32), ((3, 1), (8, 49), (11, 49)), 'Add', '{70109AA1-63C1-11D2-B78B-0060B0EC020B}',DocumentType
			, TemplateFileName, CreateVisible)

	def CloseAll(self, UnreferencedOnly=False):
		'Closes all the documents in the current Inventor session.  Changes are not saved to any of the documents. In other words, if there are dirty documents in the collection, changes made to them will be lost'
		return self._oleobj_.InvokeTypes(50332420, LCID, 1, (24, 0), ((11, 49),),UnreferencedOnly
			)

	# Result is of type Document
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'Allows integer-indexed access to items in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{70109AA1-63C1-11D2-B78B-0060B0EC020B}')
		return ret

	# Result is of type Document
	# The method ItemByName is actually a property, but must be used as a method to correctly pass the arguments
	def ItemByName(self, FullDocumentName=defaultNamedNotOptArg):
		'Allows string-indexed access to items in the collection. Usually found when this ability has been added to an pre-existing collection'
		ret = self._oleobj_.InvokeTypes(2130706471, LCID, 2, (9, 0), ((8, 1),),FullDocumentName
			)
		if ret is not None:
			ret = Dispatch(ret, 'ItemByName', '{70109AA1-63C1-11D2-B78B-0060B0EC020B}')
		return ret

	# Result is of type Document
	def Open(self, FullDocumentName=defaultNamedNotOptArg, OpenVisible=True):
		'Opens a Document of the specified file-name'
		ret = self._oleobj_.InvokeTypes(50332418, LCID, 1, (9, 0), ((8, 1), (11, 49)),FullDocumentName
			, OpenVisible)
		if ret is not None:
			ret = Dispatch(ret, 'Open', '{70109AA1-63C1-11D2-B78B-0060B0EC020B}')
		return ret

	# Result is of type Document
	def OpenWithOptions(self, FullDocumentName=defaultNamedNotOptArg, Options=defaultNamedNotOptArg, OpenVisible=True):
		'Opens a Document of the specified file-name with the specified set of options'
		ret = self._oleobj_.InvokeTypes(50332419, LCID, 1, (9, 0), ((8, 1), (9, 1), (11, 49)),FullDocumentName
			, Options, OpenVisible)
		if ret is not None:
			ret = Dispatch(ret, 'OpenWithOptions', '{70109AA1-63C1-11D2-B78B-0060B0EC020B}')
		return ret

	_prop_map_get_ = {
		"Count": (2130706438, 2, (3, 0), (), "Count", None),
		"LoadedCount": (50332422, 2, (3, 0), (), "LoadedCount", None),
		"Type": (2130706435, 2, (3, 0), (), "Type", None),
		# Method 'VisibleDocuments' returns object of type 'DocumentsEnumerator'
		"VisibleDocuments": (50332421, 2, (9, 0), (), "VisibleDocuments", '{ACE59077-7778-11D4-8DD8-0010B541CAA8}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Allows integer-indexed access to items in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{70109AA1-63C1-11D2-B78B-0060B0EC020B}')
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
		return win32com.client.util.Iterator(ob, '{70109AA1-63C1-11D2-B78B-0060B0EC020B}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2130706438, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

win32com.client.CLSIDToClass.RegisterCLSID( "{70109AA2-63C1-11D2-B78B-0060B0EC020B}", Documents )
