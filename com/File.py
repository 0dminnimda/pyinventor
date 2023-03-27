# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 14:51:13 2023
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
class File(DispatchBaseClass):
	'File Object'
	CLSID = IID('{6E5CDAB2-6BA5-4EAD-B357-78646BE0A813}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'AllReferencedFiles' returns object of type 'FilesEnumerator'
		"AllReferencedFiles": (50407174, 2, (9, 0), (), "AllReferencedFiles", '{4771DB69-A789-4BA4-A35C-56BFCC6AECFA}'),
		"Application": (2130706433, 2, (9, 0), (), "Application", None),
		"AvailableDocuments": (50407169, 2, (9, 0), (), "AvailableDocuments", None),
		"FileSaveCounter": (50407176, 2, (3, 0), (), "FileSaveCounter", None),
		"FullFileName": (50407170, 2, (8, 0), (), "FullFileName", None),
		"InternalName": (50407173, 2, (8, 0), (), "InternalName", None),
		"OwnershipType": (50407177, 2, (3, 0), (), "OwnershipType", None),
		# Method 'ReferencedFileDescriptors' returns object of type 'FileDescriptorsEnumerator'
		"ReferencedFileDescriptors": (50407171, 2, (9, 0), (), "ReferencedFileDescriptors", '{C64DD969-DCB0-4FA9-AD0A-E09744466D61}'),
		# Method 'ReferencedFiles' returns object of type 'FilesEnumerator'
		"ReferencedFiles": (50407172, 2, (9, 0), (), "ReferencedFiles", '{4771DB69-A789-4BA4-A35C-56BFCC6AECFA}'),
		# Method 'ReferencingFiles' returns object of type 'FilesEnumerator'
		"ReferencingFiles": (50407175, 2, (9, 0), (), "ReferencingFiles", '{4771DB69-A789-4BA4-A35C-56BFCC6AECFA}'),
		"Type": (2130706435, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"FullFileName": ((50407170, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{6E5CDAB2-6BA5-4EAD-B357-78646BE0A813}", File )
