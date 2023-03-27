# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 15:21:12 2023
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
class View(DispatchBaseClass):
	'View Object'
	CLSID = IID('{70109AA3-63C1-11D2-B78B-0060B0EC020B}')
	coclass_clsid = None

	def Activate(self):
		'Makes this View the active one (receives user-focus)'
		return self._oleobj_.InvokeTypes(50332674, LCID, 1, (24, 0), (),)

	def Close(self):
		'Closes this View'
		return self._oleobj_.InvokeTypes(50332675, LCID, 1, (24, 0), (),)

	def Fit(self, DoUpdate=True):
		'Fits all the contents of the Document into this View'
		return self._oleobj_.InvokeTypes(50332677, LCID, 1, (24, 0), ((11, 49),),DoUpdate
			)

	def GetWindowExtents(self, Top=pythoncom.Missing, Left=pythoncom.Missing, Height=pythoncom.Missing, Width=pythoncom.Missing):
		"Obtains the View's client area's position and size"
		return self._ApplyTypes_(50332681, 1, (24, 0), ((16387, 2), (16387, 2), (16387, 2), (16387, 2)), 'GetWindowExtents', None,Top
			, Left, Height, Width)

	def GoHome(self):
		'Method that sets the view to the default view of the model'
		return self._oleobj_.InvokeTypes(50332705, LCID, 1, (24, 0), (),)

	def Move(self, Top=defaultNamedNotOptArg, Left=defaultNamedNotOptArg, Height=defaultNamedNotOptArg, Width=defaultNamedNotOptArg):
		'Moves this views window'
		return self._oleobj_.InvokeTypes(50332695, LCID, 1, (24, 0), ((16387, 1), (16387, 1), (16387, 1), (16387, 1)),Top
			, Left, Height, Width)

	def ResetFront(self):
		'Method that resets the front view to the factory default'
		return self._oleobj_.InvokeTypes(50332706, LCID, 1, (24, 0), (),)

	def SaveAsBitmap(self, FullFileName=defaultNamedNotOptArg, Width=defaultNamedNotOptArg, Height=defaultNamedNotOptArg):
		'Saves the view as a bitmap'
		return self._oleobj_.InvokeTypes(50332697, LCID, 1, (24, 0), ((8, 1), (3, 1), (3, 1)),FullFileName
			, Width, Height)

	def SaveAsBitmapWithOptions(self, FullFileName=defaultNamedNotOptArg, Width=defaultNamedNotOptArg, Height=defaultNamedNotOptArg, Options=defaultNamedNotOptArg):
		'Method that saves the view as a bitmap with more options. The width and height arguments define the aspect ratio and the number of pixels in the output image. The Options argument allow you to define more effects for the bitmap.'
		return self._oleobj_.InvokeTypes(50332720, LCID, 1, (24, 0), ((8, 1), (3, 1), (3, 1), (9, 1)),FullFileName
			, Width, Height, Options)

	def SaveAsBitmapWithRayTracing(self, FullFileName=defaultNamedNotOptArg):
		'Method that saves the view with ray tracing on as a bitmap in one of the following types; bmp, jpg, png, tiff, and gif.'
		return self._oleobj_.InvokeTypes(50332716, LCID, 1, (24, 0), ((8, 1),),FullFileName
			)

	def SetCurrentAsFront(self):
		'Method that sets the current view as the front view'
		return self._oleobj_.InvokeTypes(50332707, LCID, 1, (24, 0), (),)

	def SetCurrentAsHome(self, FitToView=True):
		'Method that sets the current view as the home view'
		return self._oleobj_.InvokeTypes(50332709, LCID, 1, (24, 0), ((11, 49),),FitToView
			)

	def SetCurrentAsTop(self):
		'Method that sets the current view as the top view'
		return self._oleobj_.InvokeTypes(50332708, LCID, 1, (24, 0), (),)

	def Update(self):
		'Repaints this View'
		return self._oleobj_.InvokeTypes(50332676, LCID, 1, (24, 0), (),)

	def _GraphicsCollectionEndDump(self, action=defaultNamedNotOptArg, FilePath=defaultNamedNotOptArg):
		'Hidden property.  Not for public use.  Ends collection of graphics performance data and saves results'
		return self._oleobj_.InvokeTypes(50332689, LCID, 1, (24, 0), ((8, 1), (8, 1)),action
			, FilePath)

	def _GraphicsCollectionStart(self, maxFrames=defaultNamedNotOptArg):
		'Hidden property.  Not for public use.  Begins collection of graphics performance data.'
		return self._oleobj_.InvokeTypes(50332688, LCID, 1, (24, 0), ((3, 1),),maxFrames
			)

	def _GraphicsFrameRate(self, iteration=defaultNamedNotOptArg, frames=defaultNamedNotOptArg, frameRateType=defaultNamedNotOptArg, FilePath=defaultNamedNotOptArg):
		'Hidden property.  Not for public use.  dump graphics pan/rotate/zoom frame rate.'
		return self._oleobj_.InvokeTypes(50332719, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (8, 1)),iteration
			, frames, frameRateType, FilePath)

	_prop_map_get_ = {
		"Application": (2130706433, 2, (9, 0), (), "Application", None),
		"AreTexturesOn": (50332715, 2, (11, 0), (), "AreTexturesOn", None),
		# Method 'Camera' returns object of type 'Camera'
		"Camera": (50332686, 2, (9, 0), (), "Camera", '{9C88D3AD-C3EB-11D3-B79E-0060B0F159EF}'),
		"Caption": (50332680, 2, (8, 0), (), "Caption", None),
		"DisplayMode": (50332685, 2, (3, 0), (), "DisplayMode", None),
		# Method 'Document' returns object of type 'Document'
		"Document": (50332673, 2, (9, 0), (), "Document", '{70109AA1-63C1-11D2-B78B-0060B0EC020B}'),
		"GroundShadow": (50332698, 2, (3, 0), (), "GroundShadow", None),
		"HWND": (50332687, 2, (3, 0), (), "HWND", None),
		"Height": (50332692, 2, (3, 0), (), "Height", None),
		"IsRayTracingPaused": (50332717, 2, (11, 0), (), "IsRayTracingPaused", None),
		"Left": (50332691, 2, (3, 0), (), "Left", None),
		"NavigationBarEnabled": (50332701, 2, (11, 0), (), "NavigationBarEnabled", None),
		# Method 'Parent' returns object of type 'Document'
		"Parent": (2130706434, 2, (9, 0), (), "Parent", '{70109AA1-63C1-11D2-B78B-0060B0EC020B}'),
		"RayTracing": (50332713, 2, (11, 0), (), "RayTracing", None),
		"RayTracingProgress": (50332718, 2, (5, 0), (), "RayTracingProgress", None),
		"RayTracingQuality": (50332714, 2, (3, 0), (), "RayTracingQuality", None),
		"ShowAmbientShadows": (50332710, 2, (11, 0), (), "ShowAmbientShadows", None),
		"ShowGroundPlane": (50332703, 2, (11, 0), (), "ShowGroundPlane", None),
		"ShowGroundReflections": (50332704, 2, (11, 0), (), "ShowGroundReflections", None),
		"ShowGroundShadows": (50332711, 2, (11, 0), (), "ShowGroundShadows", None),
		"ShowObjectShadows": (50332712, 2, (11, 0), (), "ShowObjectShadows", None),
		"SteeringWheelEnabled": (50332700, 2, (11, 0), (), "SteeringWheelEnabled", None),
		"Top": (50332690, 2, (3, 0), (), "Top", None),
		"Type": (0, 2, (3, 0), (), "Type", None),
		"ViewCubeEnabled": (50332699, 2, (11, 0), (), "ViewCubeEnabled", None),
		"Visible": (50332682, 2, (11, 0), (), "Visible", None),
		"Width": (50332694, 2, (3, 0), (), "Width", None),
		"WindowState": (50332696, 2, (3, 0), (), "WindowState", None),
	}
	_prop_map_put_ = {
		"AreTexturesOn": ((50332715, LCID, 4, 0),()),
		"Caption": ((50332680, LCID, 4, 0),()),
		"DisplayMode": ((50332685, LCID, 4, 0),()),
		"GroundShadow": ((50332698, LCID, 4, 0),()),
		"Height": ((50332692, LCID, 4, 0),()),
		"IsRayTracingPaused": ((50332717, LCID, 4, 0),()),
		"Left": ((50332691, LCID, 4, 0),()),
		"NavigationBarEnabled": ((50332701, LCID, 4, 0),()),
		"RayTracing": ((50332713, LCID, 4, 0),()),
		"RayTracingQuality": ((50332714, LCID, 4, 0),()),
		"ShowAmbientShadows": ((50332710, LCID, 4, 0),()),
		"ShowGroundPlane": ((50332703, LCID, 4, 0),()),
		"ShowGroundReflections": ((50332704, LCID, 4, 0),()),
		"ShowGroundShadows": ((50332711, LCID, 4, 0),()),
		"ShowObjectShadows": ((50332712, LCID, 4, 0),()),
		"SteeringWheelEnabled": ((50332700, LCID, 4, 0),()),
		"Top": ((50332690, LCID, 4, 0),()),
		"ViewCubeEnabled": ((50332699, LCID, 4, 0),()),
		"Visible": ((50332682, LCID, 4, 0),()),
		"Width": ((50332694, LCID, 4, 0),()),
		"WindowState": ((50332696, LCID, 4, 0),()),
	}
	# Default property for this class is 'Type'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (3, 0), (), "Type", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{70109AA3-63C1-11D2-B78B-0060B0EC020B}", View )
