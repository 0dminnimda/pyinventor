# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 15:46:46 2023
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
class AssemblyOptions(DispatchBaseClass):
	'Assembly Options Object'
	CLSID = IID('{C6345819-0FAA-45A0-BF96-3C946F130076}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Application": (2130706433, 2, (9, 0), (), "Application", None),
		"AssemblyExpressMinimumUniqueDocument": (50386201, 2, (3, 0), (), "AssemblyExpressMinimumUniqueDocument", None),
		"AssemblyLiteMinimumUniqueDocument": (50386199, 2, (3, 0), (), "AssemblyLiteMinimumUniqueDocument", None),
		"ConstraintAudioNotification": (50386187, 2, (11, 0), (), "ConstraintAudioNotification", None),
		"DefaultDesignView": (50386192, 2, (3, 0), (), "DefaultDesignView", None),
		"DefaultDesignViewIsAssociative": (50386193, 2, (11, 0), (), "DefaultDesignViewIsAssociative", None),
		"DefaultLevelOfDetail": (50386191, 2, (3, 0), (), "DefaultLevelOfDetail", None),
		"DeferUpdate": (50386179, 2, (11, 0), (), "DeferUpdate", None),
		"DeleteComponentPatternSources": (50386180, 2, (11, 0), (), "DeleteComponentPatternSources", None),
		"DisplayComponentNamesInConstraints": (50386195, 2, (11, 0), (), "DisplayComponentNamesInConstraints", None),
		"EnableAssemblyExpress": (50386200, 2, (11, 0), (), "EnableAssemblyExpress", None),
		"EnableAssemblyLite": (50386198, 2, (11, 0), (), "EnableAssemblyLite", None),
		"EnableConstraintRedundancyAnalysis": (50386181, 2, (11, 0), (), "EnableConstraintRedundancyAnalysis", None),
		"EnableCrossPartEdgeLoopProjection": (50386185, 2, (11, 0), (), "EnableCrossPartEdgeLoopProjection", None),
		"EnableCrossPartSketchGeometryProjection": (50386197, 2, (11, 0), (), "EnableCrossPartSketchGeometryProjection", None),
		"EnableRelatedConstraintFailureAnalysis": (50386189, 2, (11, 0), (), "EnableRelatedConstraintFailureAnalysis", None),
		"FromToExtentsAdaptFeature": (50386184, 2, (11, 0), (), "FromToExtentsAdaptFeature", None),
		"FromToExtentsMatePlane": (50386183, 2, (11, 0), (), "FromToExtentsMatePlane", None),
		"OnlyActiveComponentIsOpaque": (50386177, 2, (11, 0), (), "OnlyActiveComponentIsOpaque", None),
		"PartFeaturesInitiallyAdaptive": (50386178, 2, (11, 0), (), "PartFeaturesInitiallyAdaptive", None),
		"PlaceAndGroundFirstComponentAtOrigin": (50386208, 2, (11, 0), (), "PlaceAndGroundFirstComponentAtOrigin", None),
		"SectionAllParts": (50386182, 2, (11, 0), (), "SectionAllParts", None),
		"SkipAllUnresolvedFiles": (50386196, 2, (11, 0), (), "SkipAllUnresolvedFiles", None),
		"Type": (0, 2, (3, 0), (), "Type", None),
		"UseLastOccurrenceOrientationForPlacement": (50386194, 2, (11, 0), (), "UseLastOccurrenceOrientationForPlacement", None),
		"UseiMate": (50386188, 2, (11, 0), (), "UseiMate", None),
		"ZoomTargetComponentWithiMate": (50386186, 2, (3, 0), (), "ZoomTargetComponentWithiMate", None),
	}
	_prop_map_put_ = {
		"AssemblyExpressMinimumUniqueDocument": ((50386201, LCID, 4, 0),()),
		"AssemblyLiteMinimumUniqueDocument": ((50386199, LCID, 4, 0),()),
		"ConstraintAudioNotification": ((50386187, LCID, 4, 0),()),
		"DefaultDesignView": ((50386192, LCID, 4, 0),()),
		"DefaultDesignViewIsAssociative": ((50386193, LCID, 4, 0),()),
		"DefaultLevelOfDetail": ((50386191, LCID, 4, 0),()),
		"DeferUpdate": ((50386179, LCID, 4, 0),()),
		"DeleteComponentPatternSources": ((50386180, LCID, 4, 0),()),
		"DisplayComponentNamesInConstraints": ((50386195, LCID, 4, 0),()),
		"EnableAssemblyExpress": ((50386200, LCID, 4, 0),()),
		"EnableAssemblyLite": ((50386198, LCID, 4, 0),()),
		"EnableConstraintRedundancyAnalysis": ((50386181, LCID, 4, 0),()),
		"EnableCrossPartEdgeLoopProjection": ((50386185, LCID, 4, 0),()),
		"EnableCrossPartSketchGeometryProjection": ((50386197, LCID, 4, 0),()),
		"EnableRelatedConstraintFailureAnalysis": ((50386189, LCID, 4, 0),()),
		"FromToExtentsAdaptFeature": ((50386184, LCID, 4, 0),()),
		"FromToExtentsMatePlane": ((50386183, LCID, 4, 0),()),
		"OnlyActiveComponentIsOpaque": ((50386177, LCID, 4, 0),()),
		"PartFeaturesInitiallyAdaptive": ((50386178, LCID, 4, 0),()),
		"PlaceAndGroundFirstComponentAtOrigin": ((50386208, LCID, 4, 0),()),
		"SectionAllParts": ((50386182, LCID, 4, 0),()),
		"SkipAllUnresolvedFiles": ((50386196, LCID, 4, 0),()),
		"UseLastOccurrenceOrientationForPlacement": ((50386194, LCID, 4, 0),()),
		"UseiMate": ((50386188, LCID, 4, 0),()),
		"ZoomTargetComponentWithiMate": ((50386186, LCID, 4, 0),()),
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

win32com.client.CLSIDToClass.RegisterCLSID( "{C6345819-0FAA-45A0-BF96-3C946F130076}", AssemblyOptions )
