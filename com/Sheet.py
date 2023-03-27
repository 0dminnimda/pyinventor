# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 18:18:00 2023
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
class Sheet(DispatchBaseClass):
	'Drawing Sheet Object'
	CLSID = IID('{206B59AE-22A6-11D4-B7A8-0060B0F159EF}')
	coclass_clsid = None

	def Activate(self):
		'Make this sheet the currently active sheet'
		return self._oleobj_.InvokeTypes(117441294, LCID, 1, (24, 0), (),)

	# Result is of type Border
	def AddBorder(self, BorderDefinition=defaultNamedNotOptArg, PromptStrings=defaultNamedOptArg):
		'Add an instance of the specified border definition.  This method will fail if a border instance already exists on this sheet'
		ret = self._oleobj_.InvokeTypes(117441301, LCID, 1, (9, 0), ((12, 1), (12, 17)),BorderDefinition
			, PromptStrings)
		if ret is not None:
			ret = Dispatch(ret, 'AddBorder', '{A907AEAF-A78F-11D5-8DF8-0010B541CAA8}')
		return ret

	# Result is of type DefaultBorder
	def AddDefaultBorder(self, HorizontalZoneCount=defaultNamedOptArg, HorizontalZoneLabelMode=defaultNamedOptArg, VerticalZoneCount=defaultNamedOptArg, VerticalZoneLabelMode=defaultNamedOptArg
			, LabelFromBottomRight=defaultNamedOptArg, DelimitByLines=defaultNamedOptArg, Centermarks=defaultNamedOptArg, TopMargin=defaultNamedOptArg, BottomMargin=defaultNamedOptArg
			, LeftMargin=defaultNamedOptArg, RightMargin=defaultNamedOptArg, TextStyle=defaultNamedOptArg, TextLayer=defaultNamedOptArg, LineLayer=defaultNamedOptArg):
		'Add an instance of the default border template'
		ret = self._oleobj_.InvokeTypes(117441302, LCID, 1, (9, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),HorizontalZoneCount
			, HorizontalZoneLabelMode, VerticalZoneCount, VerticalZoneLabelMode, LabelFromBottomRight, DelimitByLines
			, Centermarks, TopMargin, BottomMargin, LeftMargin, RightMargin
			, TextStyle, TextLayer, LineLayer)
		if ret is not None:
			ret = Dispatch(ret, 'AddDefaultBorder', '{A907AEE3-A78F-11D5-8DF8-0010B541CAA8}')
		return ret

	# Result is of type TitleBlock
	def AddTitleBlock(self, TitleBlockDefinition=defaultNamedNotOptArg, TitleBlockLocation=defaultNamedOptArg, PromptStrings=defaultNamedOptArg):
		'Add an instance of the specified title block definition.  This method will fail if a title block instance already exists on this sheet'
		ret = self._oleobj_.InvokeTypes(117441300, LCID, 1, (9, 0), ((12, 1), (12, 17), (12, 17)),TitleBlockDefinition
			, TitleBlockLocation, PromptStrings)
		if ret is not None:
			ret = Dispatch(ret, 'AddTitleBlock', '{A907AEB9-A78F-11D5-8DF8-0010B541CAA8}')
		return ret

	def ChangeLayer(self, Objects=defaultNamedNotOptArg, Layer=defaultNamedNotOptArg):
		'Method that changes the associated layer for all the input objects'
		return self._oleobj_.InvokeTypes(117441330, LCID, 1, (24, 0), ((9, 1), (9, 1)),Objects
			, Layer)

	# Result is of type Sheet
	def CopyTo(self, TargetDocument=defaultNamedNotOptArg):
		'Copy this sheet to the specified drawing document'
		ret = self._oleobj_.InvokeTypes(117441305, LCID, 1, (9, 0), ((9, 1),),TargetDocument
			)
		if ret is not None:
			ret = Dispatch(ret, 'CopyTo', '{206B59AE-22A6-11D4-B7A8-0060B0F159EF}')
		return ret

	# Result is of type GeometryIntent
	def CreateGeometryIntent(self, Geometry=defaultNamedNotOptArg, Intent=defaultNamedOptArg):
		'Creates a GeometryIntent object for use in various annotation and view creations'
		ret = self._oleobj_.InvokeTypes(117441320, LCID, 1, (9, 0), ((9, 1), (12, 17)),Geometry
			, Intent)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGeometryIntent', '{56B990B9-D25A-436F-A652-1D21EC739C57}')
		return ret

	def Delete(self, RetainDependentViews=False):
		'Delete this sheet'
		return self._oleobj_.InvokeTypes(117441313, LCID, 1, (24, 0), ((11, 49),),RetainDependentViews
			)

	# Result is of type ObjectsEnumerator
	def FindUsingPoint(self, PointOnSheet=defaultNamedNotOptArg, ProximityTolerance=defaultNamedOptArg):
		'Method that finds drawing curve segments, entities on a sheet sketch, centerlines and centermarks that the given point lies on.'
		ret = self._oleobj_.InvokeTypes(117441325, LCID, 1, (9, 0), ((9, 1), (12, 17)),PointOnSheet
			, ProximityTolerance)
		if ret is not None:
			ret = Dispatch(ret, 'FindUsingPoint', '{A94DCF5E-90E9-4F60-BB55-F65B4618ECD5}')
		return ret

	def GetReferenceKey(self, ReferenceKey=defaultNamedNotOptArg, KeyContext=0):
		"Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object"
		return self._ApplyTypes_(2130706454, 1, (24, 0), ((24593, 3), (3, 49)), 'GetReferenceKey', None,ReferenceKey
			, KeyContext)

	def Update(self):
		'Method that updates the sheet'
		return self._oleobj_.InvokeTypes(117441329, LCID, 1, (24, 0), (),)

	def _SelectByONK(self, ObjectNameKey=defaultNamedNotOptArg):
		'(Internal method) Selects the object specified by the ONK'
		return self._oleobj_.InvokeTypes(117441304, LCID, 1, (24, 0), ((8, 1),),ObjectNameKey
			)

	_prop_map_get_ = {
		"Application": (2130706433, 2, (9, 0), (), "Application", None),
		# Method 'AttributeSets' returns object of type 'AttributeSets'
		"AttributeSets": (2130706452, 2, (9, 0), (), "AttributeSets", '{790B4EB3-7947-4D08-9510-372E93A24CF1}'),
		# Method 'AutoCADBlocks' returns object of type 'AutoCADBlocks'
		"AutoCADBlocks": (117441331, 2, (9, 0), (), "AutoCADBlocks", '{50DE4356-9814-490A-8932-18E72420930E}'),
		# Method 'Balloons' returns object of type 'Balloons'
		"Balloons": (117441316, 2, (9, 0), (), "Balloons", '{3DFE3282-5B67-431A-A890-040098957C1C}'),
		# Method 'Border' returns object of type 'Border'
		"Border": (117441298, 2, (9, 0), (), "Border", '{A907AEAF-A78F-11D5-8DF8-0010B541CAA8}'),
		# Method 'Centerlines' returns object of type 'Centerlines'
		"Centerlines": (117441324, 2, (9, 0), (), "Centerlines", '{3DC9DC2A-8A78-43BE-BDB5-E6F1162980BB}'),
		# Method 'Centermarks' returns object of type 'Centermarks'
		"Centermarks": (117441323, 2, (9, 0), (), "Centermarks", '{0945D4EC-0E81-4062-8AC1-E4DE4BB8CBF9}'),
		# Method 'ClientGraphicsCollection' returns object of type 'ClientGraphicsCollection'
		"ClientGraphicsCollection": (117441321, 2, (9, 0), (), "ClientGraphicsCollection", '{66829BB6-656B-431C-BF5C-0BF53DBA225D}'),
		# Method 'ClientViews' returns object of type 'ClientViews'
		"ClientViews": (117441303, 2, (9, 0), (), "ClientViews", '{3D218008-FA54-48CB-89BC-8EFBF3D0B6CC}'),
		# Method 'CustomTables' returns object of type 'CustomTables'
		"CustomTables": (117441315, 2, (9, 0), (), "CustomTables", '{2A6C1D0D-FAF8-4A31-A9FB-39761F36F814}'),
		# Method 'DataIO' returns object of type 'DataIO'
		"DataIO": (117441284, 2, (9, 0), (), "DataIO", '{FBCADB33-9CBE-11D3-B799-0060B0F159EF}'),
		# Method 'DrawingDimensions' returns object of type 'DrawingDimensions'
		"DrawingDimensions": (117441314, 2, (9, 0), (), "DrawingDimensions", '{FD30DCC9-A6E8-44B1-85B0-D7D8AE1580E5}'),
		# Method 'DrawingNotes' returns object of type 'DrawingNotes'
		"DrawingNotes": (117441319, 2, (9, 0), (), "DrawingNotes", '{3A4B5B27-8B78-4584-83B5-6A088C6B87FF}'),
		# Method 'DrawingViews' returns object of type 'DrawingViews'
		"DrawingViews": (117441283, 2, (9, 0), (), "DrawingViews", '{206B59B2-22A6-11D4-B7A8-0060B0F159EF}'),
		"ExcludeFromCount": (117441295, 2, (11, 0), (), "ExcludeFromCount", None),
		"ExcludeFromPrinting": (117441296, 2, (11, 0), (), "ExcludeFromPrinting", None),
		# Method 'FeatureControlFrames' returns object of type 'FeatureControlFrames'
		"FeatureControlFrames": (117441327, 2, (9, 0), (), "FeatureControlFrames", '{682CEB3B-365E-4863-B103-BCC368FBA896}'),
		# Method 'GraphicsDataSetsCollection' returns object of type 'GraphicsDataSetsCollection'
		"GraphicsDataSetsCollection": (117441322, 2, (9, 0), (), "GraphicsDataSetsCollection", '{8C2CC3CF-A455-40D6-8505-56A702F6FB77}'),
		"Height": (117441288, 2, (5, 0), (), "Height", None),
		# Method 'HoleTables' returns object of type 'HoleTables'
		"HoleTables": (117441318, 2, (9, 0), (), "HoleTables", '{8C0B72C6-CFC6-4B2D-8A89-1DE890D9F65B}'),
		"InternalName": (117441282, 2, (8, 0), (), "InternalName", None),
		"IsModelSpaceSheet": (117441326, 2, (11, 0), (), "IsModelSpaceSheet", None),
		"Name": (117441290, 2, (8, 0), (), "Name", None),
		"Orientation": (117441286, 2, (3, 0), (), "Orientation", None),
		"Parent": (2130706434, 2, (9, 0), (), "Parent", None),
		# Method 'PartsLists' returns object of type 'PartsLists'
		"PartsLists": (117441293, 2, (9, 0), (), "PartsLists", '{A907AE85-A78F-11D5-8DF8-0010B541CAA8}'),
		"Revision": (117441332, 2, (8, 0), (), "Revision", None),
		# Method 'RevisionTables' returns object of type 'RevisionTables'
		"RevisionTables": (117441317, 2, (9, 0), (), "RevisionTables", '{DB2B25D3-66F3-47CC-9DBF-D6B7468EE76E}'),
		"Size": (117441285, 2, (3, 0), (), "Size", None),
		# Method 'SketchedSymbols' returns object of type 'SketchedSymbols'
		"SketchedSymbols": (117441299, 2, (9, 0), (), "SketchedSymbols", '{A907AED9-A78F-11D5-8DF8-0010B541CAA8}'),
		# Method 'Sketches' returns object of type 'DrawingSketches'
		"Sketches": (117441292, 2, (9, 0), (), "Sketches", '{1644E1D7-9BD5-11D5-8DF7-0010B541CAA8}'),
		"Status": (117441291, 2, (3, 0), (), "Status", None),
		# Method 'SurfaceTextureSymbols' returns object of type 'SurfaceTextureSymbols'
		"SurfaceTextureSymbols": (117441328, 2, (9, 0), (), "SurfaceTextureSymbols", '{F828B7C4-4B02-4B69-8D22-8BC7BA9D6243}'),
		# Method 'TitleBlock' returns object of type 'TitleBlock'
		"TitleBlock": (117441297, 2, (9, 0), (), "TitleBlock", '{A907AEB9-A78F-11D5-8DF8-0010B541CAA8}'),
		"Type": (0, 2, (3, 0), (), "Type", None),
		"Width": (117441287, 2, (5, 0), (), "Width", None),
		"_DisplayName": (117441281, 2, (8, 0), (), "_DisplayName", None),
	}
	_prop_map_put_ = {
		"ExcludeFromCount": ((117441295, LCID, 4, 0),()),
		"ExcludeFromPrinting": ((117441296, LCID, 4, 0),()),
		"Height": ((117441288, LCID, 4, 0),()),
		"Name": ((117441290, LCID, 4, 0),()),
		"Orientation": ((117441286, LCID, 4, 0),()),
		"Revision": ((117441332, LCID, 4, 0),()),
		"Size": ((117441285, LCID, 4, 0),()),
		"Width": ((117441287, LCID, 4, 0),()),
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

win32com.client.CLSIDToClass.RegisterCLSID( "{206B59AE-22A6-11D4-B7A8-0060B0F159EF}", Sheet )
