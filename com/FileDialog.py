# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 14:58:53 2023
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
class FileDialog(DispatchBaseClass):
	'File Dialog Object'
	CLSID = IID('{BA80AE34-5BB2-4C90-BFDE-64DA56286813}')
	coclass_clsid = None

	def SetHelpContext(self, FileName=defaultNamedNotOptArg, Context=defaultNamedNotOptArg):
		'Sets the HTML Help Context to display when the help button is pressed in the FileDialog.'
		return self._oleobj_.InvokeTypes(50377737, LCID, 1, (24, 0), ((8, 1), (3, 1)),FileName
			, Context)

	def SetHelpTopic(self, FileName=defaultNamedNotOptArg, TopicName=defaultNamedNotOptArg):
		'Sets the HTML Help Topic to display when the help button is pressed in the FileDialog.'
		return self._oleobj_.InvokeTypes(50377738, LCID, 1, (24, 0), ((8, 1), (8, 1)),FileName
			, TopicName)

	def ShowOpen(self):
		'Displays an open dialog.'
		return self._oleobj_.InvokeTypes(50377736, LCID, 1, (24, 0), (),)

	def ShowSave(self):
		'Displays a save as dialog.'
		return self._oleobj_.InvokeTypes(50377735, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"CancelError": (50377729, 2, (11, 0), (), "CancelError", None),
		"DesignViewAssociative": (50377748, 2, (11, 0), (), "DesignViewAssociative", None),
		"DialogTitle": (50377730, 2, (8, 0), (), "DialogTitle", None),
		"EnableLODRepresentationOption": (50377747, 2, (11, 0), (), "EnableLODRepresentationOption", None),
		"EnableSkipAllUnresolvedFilesOption": (50377746, 2, (11, 0), (), "EnableSkipAllUnresolvedFilesOption", None),
		# Method 'FileDialogEvents' returns object of type 'FileDialogEvents'
		"FileDialogEvents": (50377741, 2, (13, 0), (), "FileDialogEvents", '{8CBEA17E-7987-4C21-B3AA-429602F6BAA8}'),
		"FileName": (50377731, 2, (8, 0), (), "FileName", None),
		"Filter": (50377732, 2, (8, 0), (), "Filter", None),
		"FilterIndex": (50377733, 2, (3, 0), (), "FilterIndex", None),
		"InitialDirectory": (50377734, 2, (8, 0), (), "InitialDirectory", None),
		"InsertMode": (50377743, 2, (11, 0), (), "InsertMode", None),
		"MultiSelectEnabled": (50377742, 2, (11, 0), (), "MultiSelectEnabled", None),
		# Method 'OptionValues' returns object of type 'NameValueMap'
		"OptionValues": (50377744, 2, (9, 0), (), "OptionValues", '{6BA435DD-BBD6-11D4-8DE6-0010B541CAA8}'),
		"OptionsEnabled": (50377740, 2, (11, 0), (), "OptionsEnabled", None),
		"ShowExistingDesignViewsOnlyInDropdown": (50377749, 2, (11, 0), (), "ShowExistingDesignViewsOnlyInDropdown", None),
		"ShowQuickLaunch": (50377745, 2, (11, 0), (), "ShowQuickLaunch", None),
		"SuppressResolutionWarnings": (50377739, 2, (11, 0), (), "SuppressResolutionWarnings", None),
	}
	_prop_map_put_ = {
		"CancelError": ((50377729, LCID, 4, 0),()),
		"DesignViewAssociative": ((50377748, LCID, 4, 0),()),
		"DialogTitle": ((50377730, LCID, 4, 0),()),
		"EnableLODRepresentationOption": ((50377747, LCID, 4, 0),()),
		"EnableSkipAllUnresolvedFilesOption": ((50377746, LCID, 4, 0),()),
		"FileName": ((50377731, LCID, 4, 0),()),
		"Filter": ((50377732, LCID, 4, 0),()),
		"FilterIndex": ((50377733, LCID, 4, 0),()),
		"InitialDirectory": ((50377734, LCID, 4, 0),()),
		"InsertMode": ((50377743, LCID, 4, 0),()),
		"MultiSelectEnabled": ((50377742, LCID, 4, 0),()),
		"OptionsEnabled": ((50377740, LCID, 4, 0),()),
		"ShowExistingDesignViewsOnlyInDropdown": ((50377749, LCID, 4, 0),()),
		"ShowQuickLaunch": ((50377745, LCID, 4, 0),()),
		"SuppressResolutionWarnings": ((50377739, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{BA80AE34-5BB2-4C90-BFDE-64DA56286813}", FileDialog )
