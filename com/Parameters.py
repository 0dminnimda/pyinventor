# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 18:03:55 2023
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
class Parameters(DispatchBaseClass):
	'Parameters Collection Object (abstract base class)'
	CLSID = IID('{528C9A32-4173-420A-AD05-B6FBF8382212}')
	coclass_clsid = None

	# The method AngularStandardTolerance is actually a property, but must be used as a method to correctly pass the arguments
	def AngularStandardTolerance(self, Precision=defaultNamedNotOptArg):
		'Gets/Sets the standard tolerance for angular dimensions in this document'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(50347015, LCID, 2, (8, 0), ((3, 1),),Precision
			)

	def GetValueFromExpression(self, Expression=defaultNamedNotOptArg, UnitsSpecifier=defaultNamedNotOptArg):
		'Obtains the value the given expression evaluates to'
		return self._ApplyTypes_(50347029, 1, (12, 0), ((8, 1), (12, 1)), 'GetValueFromExpression', None,Expression
			, UnitsSpecifier)

	def IsExpressionValid(self, Expression=defaultNamedNotOptArg, UnitsSpecifier=defaultNamedNotOptArg):
		'Returns whether the input expression is valid or not'
		return self._oleobj_.InvokeTypes(50347026, LCID, 1, (11, 0), ((8, 1), (12, 1)),Expression
			, UnitsSpecifier)

	# Result is of type Parameter
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'Allows integer-indexed access to items in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{44E517BC-D882-4AFE-A300-B3DAC6B8DB58}')
		return ret

	# The method LinearStandardTolerance is actually a property, but must be used as a method to correctly pass the arguments
	def LinearStandardTolerance(self, Precision=defaultNamedNotOptArg):
		'Gets/Sets the standard tolerance for linear dimensions in this document'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(50347017, LCID, 2, (8, 0), ((3, 1),),Precision
			)

	def SetAllToMax(self):
		"Sets the values of all parameters to be the maximum value as defined by the parameter's tolerance"
		return self._oleobj_.InvokeTypes(50347020, LCID, 1, (24, 0), (),)

	def SetAllToMedian(self):
		"Sets the values of all parameters to be the median value as defined by the parameter's tolerance"
		return self._oleobj_.InvokeTypes(50347024, LCID, 1, (24, 0), (),)

	def SetAllToMin(self):
		"Sets the values of all parameters to be the minimum value as defined by the parameter's tolerance"
		return self._oleobj_.InvokeTypes(50347021, LCID, 1, (24, 0), (),)

	def SetAllToNominal(self):
		"Sets the values of all parameters to be the nominal  value as defined by the parameter's tolerance"
		return self._oleobj_.InvokeTypes(50347022, LCID, 1, (24, 0), (),)

	# The method SetAngularStandardTolerance is actually a property, but must be used as a method to correctly pass the arguments
	def SetAngularStandardTolerance(self, Precision=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'Gets/Sets the standard tolerance for angular dimensions in this document'
		return self._oleobj_.InvokeTypes(50347015, LCID, 4, (24, 0), ((3, 1), (8, 1)),Precision
			, arg1)

	# The method SetLinearStandardTolerance is actually a property, but must be used as a method to correctly pass the arguments
	def SetLinearStandardTolerance(self, Precision=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'Gets/Sets the standard tolerance for linear dimensions in this document'
		return self._oleobj_.InvokeTypes(50347017, LCID, 4, (24, 0), ((3, 1), (8, 1)),Precision
			, arg1)

	def _GetValueFromExpression(self, Expression=defaultNamedNotOptArg, UnitsSpecifier=defaultNamedNotOptArg):
		'Obtains the value the given expression evaluates to'
		return self._oleobj_.InvokeTypes(50347013, LCID, 1, (5, 0), ((8, 1), (12, 1)),Expression
			, UnitsSpecifier)

	_prop_map_get_ = {
		"AngularDimensionPrecision": (50347014, 2, (3, 0), (), "AngularDimensionPrecision", None),
		"Count": (2130706438, 2, (3, 0), (), "Count", None),
		# Method 'CustomParameterGroups' returns object of type 'CustomParameterGroups'
		"CustomParameterGroups": (50347023, 2, (9, 0), (), "CustomParameterGroups", '{ADE1D7A7-3CF2-49E7-8476-79677765D850}'),
		# Method 'DerivedParameterTables' returns object of type 'DerivedParameterTables'
		"DerivedParameterTables": (50347025, 2, (9, 0), (), "DerivedParameterTables", '{321D3FD9-A57F-4CDE-AD39-FD1EEE22543C}'),
		"DimensionDisplayType": (50347018, 2, (3, 0), (), "DimensionDisplayType", None),
		"DisplayParameterAsExpression": (50347028, 2, (11, 0), (), "DisplayParameterAsExpression", None),
		"ExportStandardTolerances": (50347027, 2, (11, 0), (), "ExportStandardTolerances", None),
		"LinearDimensionPrecision": (50347016, 2, (3, 0), (), "LinearDimensionPrecision", None),
		# Method 'ModelParameters' returns object of type 'ModelParameters'
		"ModelParameters": (50347009, 2, (9, 0), (), "ModelParameters", '{652F6A52-8B8A-4CEF-B1DC-C78751914993}'),
		# Method 'ParameterTables' returns object of type 'ParameterTables'
		"ParameterTables": (50347012, 2, (9, 0), (), "ParameterTables", '{53D15C9C-4920-4B58-8804-8567A94D1643}'),
		# Method 'ReferenceParameters' returns object of type 'ReferenceParameters'
		"ReferenceParameters": (50347010, 2, (9, 0), (), "ReferenceParameters", '{1304BB1D-95AE-4738-80F8-CCCA1ABCFF6B}'),
		"Type": (2130706435, 2, (3, 0), (), "Type", None),
		"UseStandardTolerances": (50347019, 2, (11, 0), (), "UseStandardTolerances", None),
		# Method 'UserParameters' returns object of type 'UserParameters'
		"UserParameters": (50347011, 2, (9, 0), (), "UserParameters", '{2FF370FA-BB1C-4C92-BB10-06D94CC8F8F3}'),
	}
	_prop_map_put_ = {
		"AngularDimensionPrecision": ((50347014, LCID, 4, 0),()),
		"DimensionDisplayType": ((50347018, LCID, 4, 0),()),
		"DisplayParameterAsExpression": ((50347028, LCID, 4, 0),()),
		"ExportStandardTolerances": ((50347027, LCID, 4, 0),()),
		"LinearDimensionPrecision": ((50347016, LCID, 4, 0),()),
		"UseStandardTolerances": ((50347019, LCID, 4, 0),()),
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Allows integer-indexed access to items in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{44E517BC-D882-4AFE-A300-B3DAC6B8DB58}')
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
		return win32com.client.util.Iterator(ob, '{44E517BC-D882-4AFE-A300-B3DAC6B8DB58}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2130706438, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

win32com.client.CLSIDToClass.RegisterCLSID( "{528C9A32-4173-420A-AD05-B6FBF8382212}", Parameters )
