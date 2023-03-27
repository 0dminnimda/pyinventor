# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 15:12:05 2023
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
class InventorVBAProject(DispatchBaseClass):
	"Represents Inventor's VBA project"
	CLSID = IID('{95C6C576-FC7A-4B16-B565-BFABEF69B013}')
	coclass_clsid = None

	def Close(self):
		'Method that closes this project'
		return self._oleobj_.InvokeTypes(50368773, LCID, 1, (24, 0), (),)

	def Save(self):
		'Method that saves the VBA project'
		return self._oleobj_.InvokeTypes(50368771, LCID, 1, (24, 0), (),)

	def SaveAs(self, FullFileName=defaultNamedNotOptArg):
		'Method that saves the project to a specified location'
		return self._oleobj_.InvokeTypes(50368770, LCID, 1, (24, 0), ((8, 1),),FullFileName
			)

	_prop_map_get_ = {
		# Method 'InventorVBAComponents' returns object of type 'InventorVBAComponents'
		"InventorVBAComponents": (50368776, 2, (9, 0), (), "InventorVBAComponents", '{24FAC734-1A3D-404E-A28B-7CC1AD47DCA1}'),
		"Name": (50368769, 2, (8, 0), (), "Name", None),
		# Method 'Parent' returns object of type 'Application'
		"Parent": (2130706434, 2, (9, 0), (), "Parent", '{70109AA0-63C1-11D2-B78B-0060B0EC020B}'),
		"ProjectType": (50368774, 2, (3, 0), (), "ProjectType", None),
		"Saved": (50368772, 2, (11, 0), (), "Saved", None),
		"Type": (2130706435, 2, (3, 0), (), "Type", None),
		"VBProject": (50368775, 2, (9, 0), (), "VBProject", None),
	}
	_prop_map_put_ = {
		"Name": ((50368769, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{95C6C576-FC7A-4B16-B565-BFABEF69B013}", InventorVBAProject )
