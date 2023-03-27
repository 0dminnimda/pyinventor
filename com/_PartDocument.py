# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 16:47:26 2023
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

from win32com.client import CoClassBaseClass
import sys
__import__('win32com.gen_py.D98A091D-3A0F-4C3E-B36E-61F62068D488x0x1x0._VbaImplementationPartEvents')
_VbaImplementationPartEvents = sys.modules['win32com.gen_py.D98A091D-3A0F-4C3E-B36E-61F62068D488x0x1x0._VbaImplementationPartEvents']._VbaImplementationPartEvents
__import__('win32com.gen_py.D98A091D-3A0F-4C3E-B36E-61F62068D488x0x1x0.PartDocument')
PartDocument = sys.modules['win32com.gen_py.D98A091D-3A0F-4C3E-B36E-61F62068D488x0x1x0.PartDocument'].PartDocument
class _PartDocument(CoClassBaseClass): # A CoClass
	CLSID = IID('{4D29B490-49B2-11D0-93C3-7E0706000000}')
	coclass_sources = [
		_VbaImplementationPartEvents,
	]
	default_source = _VbaImplementationPartEvents
	coclass_interfaces = [
		PartDocument,
	]
	default_interface = PartDocument

win32com.client.CLSIDToClass.RegisterCLSID( "{4D29B490-49B2-11D0-93C3-7E0706000000}", _PartDocument )
