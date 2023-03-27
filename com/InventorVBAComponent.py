# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 16:36:26 2023
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
class InventorVBAComponent(DispatchBaseClass):
	'The InventorVBAComponent object represents a code, class or form module'
	CLSID = IID('{611EDF7B-009C-4871-B3F9-69E1B4A61C1E}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'InventorVBAMembers' returns object of type 'InventorVBAMembers'
		"InventorVBAMembers": (50369282, 2, (9, 0), (), "InventorVBAMembers", '{E83434B4-B12D-4A6F-A2DC-BFA52D3C5FA7}'),
		"Name": (50369281, 2, (8, 0), (), "Name", None),
		# Method 'Parent' returns object of type 'InventorVBAProject'
		"Parent": (2130706434, 2, (9, 0), (), "Parent", '{95C6C576-FC7A-4B16-B565-BFABEF69B013}'),
		"Type": (2130706435, 2, (3, 0), (), "Type", None),
		"VBComponent": (50369283, 2, (9, 0), (), "VBComponent", None),
	}
	_prop_map_put_ = {
		"Name": ((50369281, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{611EDF7B-009C-4871-B3F9-69E1B4A61C1E}", InventorVBAComponent )
