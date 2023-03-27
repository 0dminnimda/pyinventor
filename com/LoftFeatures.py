# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 19:09:29 2023
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
class LoftFeatures(DispatchBaseClass):
	'Part Loft Features Collection Object'
	CLSID = IID('{24A0170B-C253-4A3C-9639-5DE9818A8F31}')
	coclass_clsid = None

	# Result is of type LoftFeature
	def Add(self, Definition=defaultNamedNotOptArg):
		'Creates a new loft feature'
		ret = self._oleobj_.InvokeTypes(83912963, LCID, 1, (9, 0), ((9, 1),),Definition
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{F7DDBE1D-2C8E-48B9-9E52-FC0BFB7D59A6}')
		return ret

	# Result is of type LoftDefinition
	def CreateLoftDefinition(self, Sections=defaultNamedNotOptArg, Operation=defaultNamedNotOptArg):
		'Creates a LoftDefinition object'
		ret = self._oleobj_.InvokeTypes(83912964, LCID, 1, (9, 0), ((9, 1), (3, 1)),Sections
			, Operation)
		if ret is not None:
			ret = Dispatch(ret, 'CreateLoftDefinition', '{FBEBA281-9346-4AC6-B324-6CEB7318BEBE}')
		return ret

	# Result is of type MapPointCurves
	def CreateMapCurves(self, Sections=defaultNamedNotOptArg):
		'Creates a MapPointCurves object'
		ret = self._oleobj_.InvokeTypes(83912962, LCID, 1, (9, 0), ((9, 1),),Sections
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateMapCurves', '{E405BACE-0EE8-4427-B6BE-82CC11F9CC35}')
		return ret

	# Result is of type LoftFeature
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{F7DDBE1D-2C8E-48B9-9E52-FC0BFB7D59A6}')
		return ret

	# Result is of type LoftFeature
	def _Add(self, Sections=defaultNamedNotOptArg, Operation=defaultNamedNotOptArg, StartSectionCondition=34305, StartSectionImpact=defaultNamedNotOptArg
			, StartSectionAngle=defaultNamedNotOptArg, EndSectionCondition=34305, EndSectionImpact=defaultNamedNotOptArg, EndSectionAngle=defaultNamedNotOptArg, Closed=False
			, Rails=defaultNamedOptArg, MapPointCurves=defaultNamedOptArg):
		'Creates a new loft feature'
		ret = self._oleobj_.InvokeTypes(83912961, LCID, 1, (9, 0), ((9, 1), (3, 1), (3, 49), (12, 17), (12, 17), (3, 49), (12, 17), (12, 17), (11, 49), (12, 17), (12, 17)),Sections
			, Operation, StartSectionCondition, StartSectionImpact, StartSectionAngle, EndSectionCondition
			, EndSectionImpact, EndSectionAngle, Closed, Rails, MapPointCurves
			)
		if ret is not None:
			ret = Dispatch(ret, '_Add', '{F7DDBE1D-2C8E-48B9-9E52-FC0BFB7D59A6}')
		return ret

	_prop_map_get_ = {
		"Application": (2130706433, 2, (9, 0), (), "Application", None),
		"Count": (2130706438, 2, (3, 0), (), "Count", None),
		"Type": (2130706435, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{F7DDBE1D-2C8E-48B9-9E52-FC0BFB7D59A6}')
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
		return win32com.client.util.Iterator(ob, '{F7DDBE1D-2C8E-48B9-9E52-FC0BFB7D59A6}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2130706438, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

win32com.client.CLSIDToClass.RegisterCLSID( "{24A0170B-C253-4A3C-9639-5DE9818A8F31}", LoftFeatures )
