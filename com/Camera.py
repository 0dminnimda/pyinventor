# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 15:22:26 2023
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
class Camera(DispatchBaseClass):
	'Camera Object that encapsulates all of the viewing parameters into a Scene for a particular View'
	CLSID = IID('{9C88D3AD-C3EB-11D3-B79E-0060B0F159EF}')
	coclass_clsid = None

	def Apply(self):
		'Applies the current camera to the View'
		return self._oleobj_.InvokeTypes(50345481, LCID, 1, (24, 0), (),)

	def ApplyWithoutTransition(self):
		'Applies the current camera to the View without transition'
		return self._oleobj_.InvokeTypes(50345493, LCID, 1, (24, 0), (),)

	def ComputeWithMouseInput(self, FromPoint=defaultNamedNotOptArg, ToPoint=defaultNamedNotOptArg, WheelDelta=defaultNamedNotOptArg, ViewOperation=defaultNamedNotOptArg):
		'Change the view according mouse movement and view operation'
		return self._oleobj_.InvokeTypes(50345491, LCID, 1, (24, 0), ((9, 1), (9, 1), (3, 1), (3, 1)),FromPoint
			, ToPoint, WheelDelta, ViewOperation)

	# Result is of type Picture
	def CreateImage(self, Width=defaultNamedNotOptArg, Height=defaultNamedNotOptArg, topColor=defaultNamedOptArg, bottomColor=defaultNamedOptArg):
		'Creates an image based on the current camera view'
		ret = self._oleobj_.InvokeTypes(50345497, LCID, 1, (9, 0), ((3, 1), (3, 1), (12, 17), (12, 17)),Width
			, Height, topColor, bottomColor)
		if ret is not None:
			ret = Dispatch(ret, 'CreateImage', '{7BF80981-BF32-101A-8BBB-00AA00300CAB}')
		return ret

	# Result is of type Picture
	def CreateImageWithOptions(self, Width=defaultNamedNotOptArg, Height=defaultNamedNotOptArg, Options=defaultNamedNotOptArg):
		'Creates an image based on the current camera view with options'
		ret = self._oleobj_.InvokeTypes(50345499, LCID, 1, (9, 0), ((3, 1), (3, 1), (9, 1)),Width
			, Height, Options)
		if ret is not None:
			ret = Dispatch(ret, 'CreateImageWithOptions', '{7BF80981-BF32-101A-8BBB-00AA00300CAB}')
		return ret

	def Fit(self):
		'Fits all the contents of the Document into the view'
		return self._oleobj_.InvokeTypes(50345492, LCID, 1, (24, 0), (),)

	def GetExtents(self, Width=pythoncom.Missing, Height=pythoncom.Missing):
		'Gets the view extents'
		return self._ApplyTypes_(50345490, 1, (24, 0), ((16389, 2), (16389, 2)), 'GetExtents', None,Width
			, Height)

	# Result is of type Point2d
	def ModelToViewSpace(self, ModelCoordinate=defaultNamedNotOptArg):
		'Converts a point in model space to the equivalent point on the view'
		ret = self._oleobj_.InvokeTypes(50345494, LCID, 1, (9, 0), ((9, 1),),ModelCoordinate
			)
		if ret is not None:
			ret = Dispatch(ret, 'ModelToViewSpace', '{CB69F173-558E-11D3-B793-0060B0F159EF}')
		return ret

	def SaveAsBitmap(self, FullFileName=defaultNamedNotOptArg, Width=defaultNamedNotOptArg, Height=defaultNamedNotOptArg, topColor=defaultNamedOptArg
			, bottomColor=defaultNamedOptArg):
		'Saves the current camera view to the specified file'
		return self._oleobj_.InvokeTypes(50345496, LCID, 1, (24, 0), ((8, 1), (3, 1), (3, 1), (12, 17), (12, 17)),FullFileName
			, Width, Height, topColor, bottomColor)

	def SetExtents(self, Width=defaultNamedNotOptArg, Height=defaultNamedNotOptArg):
		'Sets the view extents'
		return self._oleobj_.InvokeTypes(50345489, LCID, 1, (24, 0), ((5, 1), (5, 1)),Width
			, Height)

	# Result is of type Point
	def ViewToModelSpace(self, ViewCoordinate=defaultNamedNotOptArg):
		'Converts a point in view space to the equivalent point in the model'
		ret = self._oleobj_.InvokeTypes(50345495, LCID, 1, (9, 0), ((9, 1),),ViewCoordinate
			)
		if ret is not None:
			ret = Dispatch(ret, 'ViewToModelSpace', '{CB69F172-558E-11D3-B793-0060B0F159EF}')
		return ret

	_prop_map_get_ = {
		# Method 'Eye' returns object of type 'Point'
		"Eye": (50345483, 2, (9, 0), (), "Eye", '{CB69F172-558E-11D3-B793-0060B0F159EF}'),
		# Method 'ModelToViewTransformation' returns object of type 'Matrix'
		"ModelToViewTransformation": (50345500, 2, (9, 0), (), "ModelToViewTransformation", '{CB69F171-558E-11D3-B793-0060B0F159EF}'),
		"Parent": (2130706434, 2, (9, 0), (), "Parent", None),
		"Perspective": (50345486, 2, (11, 0), (), "Perspective", None),
		"PerspectiveAngle": (50345487, 2, (5, 0), (), "PerspectiveAngle", None),
		"SceneObject": (50345498, 2, (9, 0), (), "SceneObject", None),
		# Method 'Target' returns object of type 'Point'
		"Target": (50345484, 2, (9, 0), (), "Target", '{CB69F172-558E-11D3-B793-0060B0F159EF}'),
		"Type": (0, 2, (3, 0), (), "Type", None),
		# Method 'UpVector' returns object of type 'UnitVector'
		"UpVector": (50345485, 2, (9, 0), (), "UpVector", '{CB69F176-558E-11D3-B793-0060B0F159EF}'),
		"ViewOrientationType": (50345482, 2, (3, 0), (), "ViewOrientationType", None),
		# Method 'ViewToWorld' returns object of type 'Matrix'
		"ViewToWorld": (50345474, 2, (9, 0), (), "ViewToWorld", '{CB69F171-558E-11D3-B793-0060B0F159EF}'),
		# Method 'WorldToView' returns object of type 'Matrix'
		"WorldToView": (50345473, 2, (9, 0), (), "WorldToView", '{CB69F171-558E-11D3-B793-0060B0F159EF}'),
	}
	_prop_map_put_ = {
		"Animating": ((50345501, LCID, 4, 0),()),
		"DumpingNodeCount": ((50345502, LCID, 4, 0),()),
		"Eye": ((50345483, LCID, 4, 0),()),
		"Perspective": ((50345486, LCID, 4, 0),()),
		"PerspectiveAngle": ((50345487, LCID, 4, 0),()),
		"SceneObject": ((50345498, LCID, 4, 0),()),
		"Target": ((50345484, LCID, 4, 0),()),
		"UpVector": ((50345485, LCID, 4, 0),()),
		"ViewOrientationType": ((50345482, LCID, 4, 0),()),
		"ViewToWorld": ((50345474, LCID, 4, 0),()),
		"WorldToView": ((50345473, LCID, 4, 0),()),
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

win32com.client.CLSIDToClass.RegisterCLSID( "{9C88D3AD-C3EB-11D3-B79E-0060B0F159EF}", Camera )
