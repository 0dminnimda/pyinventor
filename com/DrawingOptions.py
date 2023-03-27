# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 15:14:21 2023
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
class DrawingOptions(DispatchBaseClass):
	'Drawing Options Object'
	CLSID = IID('{221277C1-7963-4539-B2E5-E7E16D3C75AA}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Application": (2130706433, 2, (9, 0), (), "Application", None),
		"ArcDimensionType": (50415107, 2, (3, 0), (), "ArcDimensionType", None),
		"CenterDimensionText": (50415106, 2, (11, 0), (), "CenterDimensionText", None),
		"CircleDimensionType": (50415108, 2, (3, 0), (), "CircleDimensionType", None),
		"DefaultDrawingFileType": (50415119, 2, (3, 0), (), "DefaultDrawingFileType", None),
		"DefaultLayerStyle": (50415120, 2, (3, 0), (), "DefaultLayerStyle", None),
		"DefaultNonInventorDWGFileOpenBehavior": (50415121, 2, (3, 0), (), "DefaultNonInventorDWGFileOpenBehavior", None),
		"DefaultObjectStyle": (50415122, 2, (3, 0), (), "DefaultObjectStyle", None),
		"DisplayLineWeights": (50415105, 2, (11, 0), (), "DisplayLineWeights", None),
		"EditDimensionWhenCreated": (50415127, 2, (11, 0), (), "EditDimensionWhenCreated", None),
		"EnableBackgroundUpdates": (50415131, 2, (11, 0), (), "EnableBackgroundUpdates", None),
		"EnableOrdinateDimGeomSelection": (50415126, 2, (11, 0), (), "EnableOrdinateDimGeomSelection", None),
		"EnablePartModificationFromDrawing": (50415132, 2, (11, 0), (), "EnablePartModificationFromDrawing", None),
		"GetModelDimensions": (50415111, 2, (11, 0), (), "GetModelDimensions", None),
		"InventorDWGFileVersion": (50415128, 2, (3, 0), (), "InventorDWGFileVersion", None),
		"LineWeightType": (50415109, 2, (3, 0), (), "LineWeightType", None),
		"LinearDimensionType": (50415112, 2, (3, 0), (), "LinearDimensionType", None),
		"MemorySavingMode": (50415123, 2, (11, 0), (), "MemorySavingMode", None),
		"ShowUncutSectionViewPreview": (50415124, 2, (11, 0), (), "ShowUncutSectionViewPreview", None),
		"SkipAllUnresolvedFiles": (50415130, 2, (11, 0), (), "SkipAllUnresolvedFiles", None),
		"StandardPartsSectionBehavior": (50415113, 2, (3, 0), (), "StandardPartsSectionBehavior", None),
		"TitleBlockAlignment": (50415114, 2, (3, 0), (), "TitleBlockAlignment", None),
		"Type": (0, 2, (3, 0), (), "Type", None),
		"UpperLimitForFirstRangeOfLineWeights": (50415115, 2, (5, 0), (), "UpperLimitForFirstRangeOfLineWeights", None),
		"UpperLimitForSecondRangeOfLineWeights": (50415116, 2, (5, 0), (), "UpperLimitForSecondRangeOfLineWeights", None),
		"UpperLimitForThirdRangeOfLineWeights": (50415117, 2, (5, 0), (), "UpperLimitForThirdRangeOfLineWeights", None),
		"ViewBlockInsertionPoint": (50415129, 2, (3, 0), (), "ViewBlockInsertionPoint", None),
		"ViewJustification": (50415118, 2, (3, 0), (), "ViewJustification", None),
		"ViewPreview": (50415125, 2, (3, 0), (), "ViewPreview", None),
	}
	_prop_map_put_ = {
		"ArcDimensionType": ((50415107, LCID, 4, 0),()),
		"CenterDimensionText": ((50415106, LCID, 4, 0),()),
		"CircleDimensionType": ((50415108, LCID, 4, 0),()),
		"DefaultDrawingFileType": ((50415119, LCID, 4, 0),()),
		"DefaultLayerStyle": ((50415120, LCID, 4, 0),()),
		"DefaultNonInventorDWGFileOpenBehavior": ((50415121, LCID, 4, 0),()),
		"DefaultObjectStyle": ((50415122, LCID, 4, 0),()),
		"DisplayLineWeights": ((50415105, LCID, 4, 0),()),
		"EditDimensionWhenCreated": ((50415127, LCID, 4, 0),()),
		"EnableBackgroundUpdates": ((50415131, LCID, 4, 0),()),
		"EnableOrdinateDimGeomSelection": ((50415126, LCID, 4, 0),()),
		"EnablePartModificationFromDrawing": ((50415132, LCID, 4, 0),()),
		"GetModelDimensions": ((50415111, LCID, 4, 0),()),
		"InventorDWGFileVersion": ((50415128, LCID, 4, 0),()),
		"LineWeightType": ((50415109, LCID, 4, 0),()),
		"LinearDimensionType": ((50415112, LCID, 4, 0),()),
		"MemorySavingMode": ((50415123, LCID, 4, 0),()),
		"ShowUncutSectionViewPreview": ((50415124, LCID, 4, 0),()),
		"SkipAllUnresolvedFiles": ((50415130, LCID, 4, 0),()),
		"StandardPartsSectionBehavior": ((50415113, LCID, 4, 0),()),
		"TitleBlockAlignment": ((50415114, LCID, 4, 0),()),
		"UpperLimitForFirstRangeOfLineWeights": ((50415115, LCID, 4, 0),()),
		"UpperLimitForSecondRangeOfLineWeights": ((50415116, LCID, 4, 0),()),
		"UpperLimitForThirdRangeOfLineWeights": ((50415117, LCID, 4, 0),()),
		"ViewBlockInsertionPoint": ((50415129, LCID, 4, 0),()),
		"ViewJustification": ((50415118, LCID, 4, 0),()),
		"ViewPreview": ((50415125, LCID, 4, 0),()),
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

win32com.client.CLSIDToClass.RegisterCLSID( "{221277C1-7963-4539-B2E5-E7E16D3C75AA}", DrawingOptions )
