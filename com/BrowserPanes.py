# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 16:19:01 2023
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
class BrowserPanes(DispatchBaseClass):
	'Browser Panes object'
	CLSID = IID('{1EBEC999-3A4D-4A4C-A35A-3F2E773DD56D}')
	coclass_clsid = None

	# Result is of type BrowserPane
	def Add(self, Name=defaultNamedNotOptArg, InternalName=defaultNamedNotOptArg):
		'Creates and returns a new BrowserPane object given an ActiveX control'
		ret = self._oleobj_.InvokeTypes(50362881, LCID, 1, (13, 0), ((8, 1), (8, 1)),Name
			, InternalName)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'Add', '{D99ADCF5-8187-4381-979E-499E017C7C0C}')
		return ret

	# Result is of type BrowserPane
	def AddByManifest(self, Name=defaultNamedNotOptArg, InternalName=defaultNamedNotOptArg, ManifestFileName=defaultNamedNotOptArg):
		'Method that creates and returns a new BrowserPane object. The BrowserPane created is one that is explicitly used to house un-registered ActiveX Controls.'
		ret = self._oleobj_.InvokeTypes(50362890, LCID, 1, (13, 0), ((8, 1), (8, 1), (8, 1)),Name
			, InternalName, ManifestFileName)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'AddByManifest', '{D99ADCF5-8187-4381-979E-499E017C7C0C}')
		return ret

	# Result is of type BrowserPane
	def AddTransientTreeBrowserPane(self, Name=defaultNamedNotOptArg, InternalName=defaultNamedNotOptArg, TopNodeDefinition=defaultNamedNotOptArg):
		'Creates and returns a new BrowserPane object that will NOT be saved with the document'
		ret = self._oleobj_.InvokeTypes(50362887, LCID, 1, (13, 0), ((8, 1), (8, 1), (9, 1)),Name
			, InternalName, TopNodeDefinition)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'AddTransientTreeBrowserPane', '{D99ADCF5-8187-4381-979E-499E017C7C0C}')
		return ret

	# Result is of type BrowserPane
	def AddTreeBrowserPane(self, Name=defaultNamedNotOptArg, InternalName=defaultNamedNotOptArg, TopNodeDefinition=defaultNamedNotOptArg):
		'Creates and returns a new customized Inventor style BrowserPane object'
		ret = self._oleobj_.InvokeTypes(50362883, LCID, 1, (13, 0), ((8, 1), (8, 1), (9, 1)),Name
			, InternalName, TopNodeDefinition)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'AddTreeBrowserPane', '{D99ADCF5-8187-4381-979E-499E017C7C0C}')
		return ret

	# Result is of type ClientBrowserNodeDefinition
	def CreateBrowserNodeDefinition(self, Label=defaultNamedNotOptArg, Id=defaultNamedNotOptArg, Icon=defaultNamedNotOptArg, ToolTipText=defaultNamedOptArg
			, ExpandedIcon=defaultNamedOptArg, DisplayState=defaultNamedOptArg, StateIconToolTipText=defaultNamedOptArg):
		'Method that creates a new ClientBrowserNodeDefinition'
		ret = self._oleobj_.InvokeTypes(50362885, LCID, 1, (13, 0), ((8, 1), (3, 1), (9, 1), (12, 17), (12, 17), (12, 17), (12, 17)),Label
			, Id, Icon, ToolTipText, ExpandedIcon, DisplayState
			, StateIconToolTipText)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'CreateBrowserNodeDefinition', '{53318B1D-70C7-4BB0-9103-73ABFA0B3094}')
		return ret

	# Result is of type ClientBrowserNodeDefinition
	def GetClientBrowserNodeDefinition(self, ClientId=defaultNamedNotOptArg, Id=defaultNamedNotOptArg):
		'Gets a ClientBrowserNodeDefinition given a ClientId and Id combination'
		ret = self._oleobj_.InvokeTypes(50362889, LCID, 1, (13, 0), ((8, 1), (3, 1)),ClientId
			, Id)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetClientBrowserNodeDefinition', '{53318B1D-70C7-4BB0-9103-73ABFA0B3094}')
		return ret

	# Result is of type NativeBrowserNodeDefinition
	def GetNativeBrowserNodeDefinition(self, NativeObject=defaultNamedNotOptArg):
		'Gets the NativeBrowserNodeDefinition object corresponding to a data model object'
		ret = self._oleobj_.InvokeTypes(50362888, LCID, 1, (13, 0), ((9, 1),),NativeObject
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetNativeBrowserNodeDefinition', '{CF10C244-F350-4155-97FD-34A35D996272}')
		return ret

	# Result is of type NativeBrowserNodeDefinition
	def GetNativeBrowserNodeDefinitionWithOptions(self, NativeObject=defaultNamedNotOptArg, Options=defaultNamedOptArg):
		'Method that returns the NativeBrowserNodeDefinition that corresponds to the input object'
		ret = self._oleobj_.InvokeTypes(50362891, LCID, 1, (13, 0), ((9, 1), (12, 17)),NativeObject
			, Options)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetNativeBrowserNodeDefinitionWithOptions', '{CF10C244-F350-4155-97FD-34A35D996272}')
		return ret

	# Result is of type BrowserPane
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 1),),Index
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'Item', '{D99ADCF5-8187-4381-979E-499E017C7C0C}')
		return ret

	_prop_map_get_ = {
		# Method 'ActivePane' returns object of type 'BrowserPane'
		"ActivePane": (50362882, 2, (13, 0), (), "ActivePane", '{D99ADCF5-8187-4381-979E-499E017C7C0C}'),
		"Application": (2130706433, 2, (9, 0), (), "Application", None),
		# Method 'BrowserPanesEvents' returns object of type 'BrowserPanesEvents'
		"BrowserPanesEvents": (50362886, 2, (13, 0), (), "BrowserPanesEvents", '{F1B96719-11ED-44A6-9AAB-34BC6D05F8EF}'),
		# Method 'ClientNodeResources' returns object of type 'ClientNodeResources'
		"ClientNodeResources": (50362884, 2, (9, 0), (), "ClientNodeResources", '{9C8B2909-8C33-481E-8CF5-9C269B4E54DC}'),
		"Count": (2130706438, 2, (3, 0), (), "Count", None),
		"Type": (2130706435, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 1),),Index
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, '__call__', '{D99ADCF5-8187-4381-979E-499E017C7C0C}')
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
		return win32com.client.util.Iterator(ob, '{D99ADCF5-8187-4381-979E-499E017C7C0C}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2130706438, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

win32com.client.CLSIDToClass.RegisterCLSID( "{1EBEC999-3A4D-4A4C-A35A-3F2E773DD56D}", BrowserPanes )
