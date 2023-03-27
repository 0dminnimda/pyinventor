# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 18:44:31 2023
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
class Point(DispatchBaseClass):
	'The Point object. The object is a transient mathematical object and is not displayed graphically. For more information see the Transient Geometry article in the overviews section.'
	CLSID = IID('{CB69F172-558E-11D3-B793-0060B0F159EF}')
	coclass_clsid = None

	# Result is of type Point
	def Copy(self):
		'Creates a copy of this Point object'
		ret = self._oleobj_.InvokeTypes(67111227, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Copy', '{CB69F172-558E-11D3-B793-0060B0F159EF}')
		return ret

	def DistanceTo(self, Point=defaultNamedNotOptArg):
		'Determine the distance between this point and the specified point'
		return self._oleobj_.InvokeTypes(67111224, LCID, 1, (5, 0), ((9, 1),),Point
			)

	def GetPointData(self, Coords=defaultNamedNotOptArg):
		'Get the data defining this point'
		return self._ApplyTypes_(0, 1, (24, 0), ((24581, 3),), 'GetPointData', None,Coords
			)

	def IsEqualTo(self, Point=defaultNamedNotOptArg, Tolerance=0.0):
		'Compares this point for equality with the specified point'
		return self._oleobj_.InvokeTypes(67111226, LCID, 1, (11, 0), ((9, 1), (5, 49)),Point
			, Tolerance)

	def PutPointData(self, Coords=defaultNamedNotOptArg):
		'Method that sets the data defining this point.'
		return self._ApplyTypes_(67111218, 1, (24, 0), ((24581, 3),), 'PutPointData', None,Coords
			)

	def TransformBy(self, Matrix=defaultNamedNotOptArg):
		'Transform this point by the specified matrix'
		return self._oleobj_.InvokeTypes(67111222, LCID, 1, (24, 0), ((9, 1),),Matrix
			)

	def TranslateBy(self, Vector=defaultNamedNotOptArg):
		'Translate this point by the specified Vector'
		return self._oleobj_.InvokeTypes(67111223, LCID, 1, (24, 0), ((9, 1),),Vector
			)

	# Result is of type Vector
	def VectorTo(self, Point=defaultNamedNotOptArg):
		'Get the vector of translation between this point and the specified point'
		ret = self._oleobj_.InvokeTypes(67111225, LCID, 1, (9, 0), ((9, 1),),Point
			)
		if ret is not None:
			ret = Dispatch(ret, 'VectorTo', '{CB69F174-558E-11D3-B793-0060B0F159EF}')
		return ret

	_prop_map_get_ = {
		"X": (67111219, 2, (5, 0), (), "X", None),
		"Y": (67111220, 2, (5, 0), (), "Y", None),
		"Z": (67111221, 2, (5, 0), (), "Z", None),
	}
	_prop_map_put_ = {
		"X": ((67111219, LCID, 4, 0),()),
		"Y": ((67111220, LCID, 4, 0),()),
		"Z": ((67111221, LCID, 4, 0),()),
	}
	# Default method for this class is 'GetPointData'
	def __call__(self, Coords=defaultNamedNotOptArg):
		'Get the data defining this point'
		return self._ApplyTypes_(0, 1, (24, 0), ((24581, 3),), '__call__', None,Coords
			)

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

win32com.client.CLSIDToClass.RegisterCLSID( "{CB69F172-558E-11D3-B793-0060B0F159EF}", Point )
