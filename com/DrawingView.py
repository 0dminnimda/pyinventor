# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 18:23:31 2023
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
class DrawingView(DispatchBaseClass):
	'Drawing View Object'
	CLSID = IID('{206B59B1-22A6-11D4-B7A8-0060B0F159EF}')
	coclass_clsid = None

	def Align(self, DrawingView=defaultNamedNotOptArg, AlignmentType=defaultNamedNotOptArg):
		'Aligns this view with the input drawing view'
		return self._oleobj_.InvokeTypes(117441613, LCID, 1, (24, 0), ((9, 1), (3, 1)),DrawingView
			, AlignmentType)

	def AlignAuxiliary(self, DrawingCurve=defaultNamedNotOptArg, Position=defaultNamedNotOptArg):
		'Re-aligns an auxiliary view'
		return self._oleobj_.InvokeTypes(117441614, LCID, 1, (24, 0), ((9, 1), (9, 1)),DrawingCurve
			, Position)

	# Result is of type DrawingView
	def CopyTo(self, TargetSheet=defaultNamedNotOptArg):
		'Copy this view to the specified sheet'
		ret = self._oleobj_.InvokeTypes(117441556, LCID, 1, (9, 0), ((9, 1),),TargetSheet
			)
		if ret is not None:
			ret = Dispatch(ret, 'CopyTo', '{206B59B1-22A6-11D4-B7A8-0060B0F159EF}')
		return ret

	def CreateOriginIndicator(self, Intent=defaultNamedNotOptArg):
		'Creates the origin indicator for ordinate dimensions and hole tables. The specified input GeometryIntent object must be associated with this drawing view'
		return self._oleobj_.InvokeTypes(117441608, LCID, 1, (24, 0), ((9, 1),),Intent
			)

	def Delete(self):
		'Deletes this view from the sheet'
		return self._oleobj_.InvokeTypes(117441554, LCID, 1, (24, 0), (),)

	# Result is of type Line
	def DrawingViewToModelSpace(self, ViewCoordinate=defaultNamedNotOptArg):
		'Transform Drawing Space to Model Space'
		ret = self._oleobj_.InvokeTypes(117441558, LCID, 1, (9, 0), ((9, 1),),ViewCoordinate
			)
		if ret is not None:
			ret = Dispatch(ret, 'DrawingViewToModelSpace', '{CB69F178-558E-11D3-B793-0060B0F159EF}')
		return ret

	# Result is of type Point2d
	def DrawingViewToSheetSpace(self, ViewCoordinate=defaultNamedNotOptArg):
		'Transform Drawing Space to Sheet Space'
		ret = self._oleobj_.InvokeTypes(117441560, LCID, 1, (9, 0), ((9, 1),),ViewCoordinate
			)
		if ret is not None:
			ret = Dispatch(ret, 'DrawingViewToSheetSpace', '{CB69F173-558E-11D3-B793-0060B0F159EF}')
		return ret

	def GetAutomatedCenterlineSettings(self, AutomatedCenterlineSettings=pythoncom.Missing):
		'Gets the settings that define how automatic center lines and center marks are to be calculated for this view'
		return self._ApplyTypes_(117441633, 1, (24, 0), ((16393, 2),), 'GetAutomatedCenterlineSettings', None,AutomatedCenterlineSettings
			)

	# Result is of type DrawingCurvesEnumerator
	# The method GetDrawingCurves is actually a property, but must be used as a method to correctly pass the arguments
	def GetDrawingCurves(self, ModelObject=defaultNamedOptArg):
		'Gets an enumerator of all drawing curves in this view optionally filtered to input model object'
		ret = self._oleobj_.InvokeTypes(117441587, LCID, 2, (9, 0), ((12, 17),),ModelObject
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetDrawingCurves', '{E49C9290-6D71-4C14-8B15-3595306A49D6}')
		return ret

	def GetIncludeStatus(self, Object=defaultNamedNotOptArg):
		'Gets the include status of the input object in the view'
		return self._oleobj_.InvokeTypes(117441604, LCID, 1, (11, 0), ((9, 1),),Object
			)

	def GetReferenceKey(self, ReferenceKey=defaultNamedNotOptArg, KeyContext=0):
		"Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object"
		return self._ApplyTypes_(2130706454, 1, (24, 0), ((24593, 3), (3, 49)), 'GetReferenceKey', None,ReferenceKey
			, KeyContext)

	def GetVisibility(self, Object=defaultNamedNotOptArg):
		'Gets the visibility of the input object in the view'
		return self._oleobj_.InvokeTypes(117441575, LCID, 1, (11, 0), ((9, 1),),Object
			)

	def GetWeldmentState(self, WeldmentState=pythoncom.Missing, Component=pythoncom.Missing):
		'Gets the weldment option for the drawing view'
		return self._ApplyTypes_(117441624, 1, (24, 0), ((16387, 2), (16393, 2)), 'GetWeldmentState', None,WeldmentState
			, Component)

	def InsertInModelSpace(self):
		'Inserts the view geometry into model space only if the drawing lives in an Inventor DWG file'
		return self._oleobj_.InvokeTypes(117441637, LCID, 1, (24, 0), (),)

	# Result is of type Point2d
	def ModelToDrawingViewSpace(self, ModelCoordinate=defaultNamedNotOptArg):
		'Transform Model Space to Drawing Space'
		ret = self._oleobj_.InvokeTypes(117441562, LCID, 1, (9, 0), ((9, 1),),ModelCoordinate
			)
		if ret is not None:
			ret = Dispatch(ret, 'ModelToDrawingViewSpace', '{CB69F173-558E-11D3-B793-0060B0F159EF}')
		return ret

	# Result is of type Point2d
	def ModelToSheetSpace(self, ModelCoordinate=defaultNamedNotOptArg):
		'Transform Model Space to Sheet Space'
		ret = self._oleobj_.InvokeTypes(117441564, LCID, 1, (9, 0), ((9, 1),),ModelCoordinate
			)
		if ret is not None:
			ret = Dispatch(ret, 'ModelToSheetSpace', '{CB69F173-558E-11D3-B793-0060B0F159EF}')
		return ret

	# Result is of type DrawingView
	def MoveTo(self, TargetSheet=defaultNamedNotOptArg):
		'Move this view to the specified sheet'
		ret = self._oleobj_.InvokeTypes(117441555, LCID, 1, (9, 0), ((9, 1),),TargetSheet
			)
		if ret is not None:
			ret = Dispatch(ret, 'MoveTo', '{206B59B1-22A6-11D4-B7A8-0060B0F159EF}')
		return ret

	def RotateByAngle(self, Angle=defaultNamedNotOptArg, Clockwise=True):
		'Rotate the drawing view by an angle'
		return self._oleobj_.InvokeTypes(117441585, LCID, 1, (24, 0), ((5, 1), (11, 49)),Angle
			, Clockwise)

	# Result is of type ObjectsEnumerator
	def SetAutomatedCenterlineSettings(self, AutomatedCenterlineSettings=defaultNamedOptArg):
		'Sets the automatic centerline and center mark settings for this view and creates the centerlines and center marks defined by the settings'
		ret = self._oleobj_.InvokeTypes(117441634, LCID, 1, (9, 0), ((12, 17),),AutomatedCenterlineSettings
			)
		if ret is not None:
			ret = Dispatch(ret, 'SetAutomatedCenterlineSettings', '{A94DCF5E-90E9-4F60-BB55-F65B4618ECD5}')
		return ret

	def SetDesignViewRepresentation(self, Representation=defaultNamedNotOptArg, Associative=False):
		'Sets a design view representation a drawing view of an assembly'
		return self._oleobj_.InvokeTypes(117441592, LCID, 1, (24, 0), ((8, 1), (11, 49)),Representation
			, Associative)

	def SetIncludeStatus(self, Object=defaultNamedNotOptArg, Include=defaultNamedNotOptArg):
		'Sets the include status of the input object in the view'
		return self._oleobj_.InvokeTypes(117441605, LCID, 1, (24, 0), ((9, 1), (11, 1)),Object
			, Include)

	def SetVisibility(self, Object=defaultNamedNotOptArg, Visible=defaultNamedNotOptArg):
		'Sets the visibility of the input object in the view'
		return self._oleobj_.InvokeTypes(117441576, LCID, 1, (24, 0), ((9, 1), (11, 1)),Object
			, Visible)

	def SetWeldmentState(self, WeldmentState=defaultNamedNotOptArg, Component=defaultNamedOptArg):
		'Sets the weldment option for the drawing view'
		return self._oleobj_.InvokeTypes(117441630, LCID, 1, (24, 0), ((3, 1), (12, 17)),WeldmentState
			, Component)

	# Result is of type Point2d
	def SheetToDrawingViewSpace(self, SheetCoordinate=defaultNamedNotOptArg):
		'Transform Sheet Space to Drawing Space'
		ret = self._oleobj_.InvokeTypes(117441569, LCID, 1, (9, 0), ((9, 1),),SheetCoordinate
			)
		if ret is not None:
			ret = Dispatch(ret, 'SheetToDrawingViewSpace', '{CB69F173-558E-11D3-B793-0060B0F159EF}')
		return ret

	# Result is of type Line
	def SheetToModelSpace(self, SheetCoordinate=defaultNamedNotOptArg):
		'Transform Sheet Space to Model Space'
		ret = self._oleobj_.InvokeTypes(117441567, LCID, 1, (9, 0), ((9, 1),),SheetCoordinate
			)
		if ret is not None:
			ret = Dispatch(ret, 'SheetToModelSpace', '{CB69F178-558E-11D3-B793-0060B0F159EF}')
		return ret

	def ShowHiddenAnnotations(self):
		'Displays all the annotations hidden by the user'
		return self._oleobj_.InvokeTypes(117441589, LCID, 1, (24, 0), (),)

	def ShowHiddenCurves(self):
		'Displays all the curves explicitly hidden by the user'
		return self._oleobj_.InvokeTypes(117441588, LCID, 1, (24, 0), (),)

	def _Update(self):
		'*** DEFUNCT SINCE R12'
		return self._oleobj_.InvokeTypes(117441595, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"ActiveDesignViewRepresentation": (117441591, 2, (8, 0), (), "ActiveDesignViewRepresentation", None),
		"ActiveLevelOfDetailRepresentation": (117441593, 2, (8, 0), (), "ActiveLevelOfDetailRepresentation", None),
		"ActiveMemberName": (117441594, 2, (8, 0), (), "ActiveMemberName", None),
		"ActivePositionalRepresentation": (117441590, 2, (8, 0), (), "ActivePositionalRepresentation", None),
		"ActivePresentationView": (117441612, 2, (8, 0), (), "ActivePresentationView", None),
		"Aligned": (117441615, 2, (11, 0), (), "Aligned", None),
		# Method 'AttributeSets' returns object of type 'AttributeSets'
		"AttributeSets": (2130706452, 2, (9, 0), (), "AttributeSets", '{790B4EB3-7947-4D08-9510-372E93A24CF1}'),
		# Method 'AuxiliaryOrientationEdge' returns object of type 'DrawingCurve'
		"AuxiliaryOrientationEdge": (117441616, 2, (9, 0), (), "AuxiliaryOrientationEdge", '{1C98EA42-27FC-4BFA-84E4-D29C7A11F889}'),
		"BitmapAvailable": (117441548, 2, (11, 0), (), "BitmapAvailable", None),
		# Method 'BreakOperations' returns object of type 'BreakOperations'
		"BreakOperations": (117441635, 2, (9, 0), (), "BreakOperations", '{1880ABD8-B826-4258-A2F1-31B5E5740FA6}'),
		# Method 'BreakOutOperations' returns object of type 'BreakOutOperations'
		"BreakOutOperations": (117441636, 2, (9, 0), (), "BreakOutOperations", '{600D4AE6-12FB-47E9-86E6-46C8C2A9161E}'),
		# Method 'Camera' returns object of type 'Camera'
		"Camera": (117441546, 2, (9, 0), (), "Camera", '{9C88D3AD-C3EB-11D3-B79E-0060B0F159EF}'),
		# Method 'Center' returns object of type 'Point2d'
		"Center": (117441602, 2, (9, 0), (), "Center", '{CB69F173-558E-11D3-B793-0060B0F159EF}'),
		# Method 'ClientGraphicsCollection' returns object of type 'ClientGraphicsCollection'
		"ClientGraphicsCollection": (117441571, 2, (9, 0), (), "ClientGraphicsCollection", '{66829BB6-656B-431C-BF5C-0BF53DBA225D}'),
		# Method 'DataIO' returns object of type 'DataIO'
		"DataIO": (117441549, 2, (9, 0), (), "DataIO", '{FBCADB33-9CBE-11D3-B799-0060B0F159EF}'),
		"DisplayBendExtents": (117441617, 2, (11, 0), (), "DisplayBendExtents", None),
		"DisplayDefinitionInBase": (117441618, 2, (11, 0), (), "DisplayDefinitionInBase", None),
		"DisplayForeshortenedTangentEdges": (117441621, 2, (11, 0), (), "DisplayForeshortenedTangentEdges", None),
		"DisplayHatching": (117441619, 2, (11, 0), (), "DisplayHatching", None),
		"DisplayInterferenceEdges": (117441620, 2, (11, 0), (), "DisplayInterferenceEdges", None),
		"DisplayTangentEdges": (117441596, 2, (11, 0), (), "DisplayTangentEdges", None),
		"DisplayThreadFeatures": (117441622, 2, (11, 0), (), "DisplayThreadFeatures", None),
		"DisplayTrails": (117441623, 2, (11, 0), (), "DisplayTrails", None),
		# Method 'DrawingCurves' returns object of type 'DrawingCurvesEnumerator'
		"DrawingCurves": (117441587, 2, (9, 0), ((12, 17),), "DrawingCurves", '{E49C9290-6D71-4C14-8B15-3595306A49D6}'),
		# Method 'DrawingViewEvents' returns object of type 'DrawingViewEvents'
		"DrawingViewEvents": (117441557, 2, (13, 0), (), "DrawingViewEvents", '{4A1FD94B-337F-43F7-AA7C-BA33B076B1EB}'),
		# Method 'DrawingViewToModelTransform' returns object of type 'Matrix'
		"DrawingViewToModelTransform": (117441559, 2, (9, 0), (), "DrawingViewToModelTransform", '{CB69F171-558E-11D3-B793-0060B0F159EF}'),
		# Method 'DrawingViewToSheetTransform' returns object of type 'Matrix'
		"DrawingViewToSheetTransform": (117441561, 2, (9, 0), (), "DrawingViewToSheetTransform", '{CB69F171-558E-11D3-B793-0060B0F159EF}'),
		"GeneralDimensionType": (117441601, 2, (3, 0), (), "GeneralDimensionType", None),
		# Method 'GraphicsDataSetsCollection' returns object of type 'GraphicsDataSetsCollection'
		"GraphicsDataSetsCollection": (117441572, 2, (9, 0), (), "GraphicsDataSetsCollection", '{8C2CC3CF-A455-40D6-8505-56A702F6FB77}'),
		"HasOriginIndicator": (117441609, 2, (11, 0), (), "HasOriginIndicator", None),
		"Height": (117441544, 2, (5, 0), (), "Height", None),
		"IncludeMeshBodies": (117441641, 2, (11, 0), (), "IncludeMeshBodies", None),
		"IncludeSurfaceBodies": (117441642, 2, (11, 0), (), "IncludeSurfaceBodies", None),
		"InheritBreak": (117441625, 2, (11, 0), (), "InheritBreak", None),
		"InheritBreakOut": (117441626, 2, (11, 0), (), "InheritBreakOut", None),
		"InheritSection": (117441627, 2, (11, 0), (), "InheritSection", None),
		"InheritSlice": (117441628, 2, (11, 0), (), "InheritSlice", None),
		"IsFlatPatternView": (117441600, 2, (11, 0), (), "IsFlatPatternView", None),
		"IsRasterView": (117441640, 2, (11, 0), (), "IsRasterView", None),
		"IsUpdateComplete": (117441639, 2, (11, 0), (), "IsUpdateComplete", None),
		# Method 'Label' returns object of type 'DrawingViewLabel'
		"Label": (117441607, 2, (9, 0), (), "Label", '{C9216F3D-E886-4E75-89AB-D7665FA14AB1}'),
		"Left": (117441543, 2, (5, 0), (), "Left", None),
		# Method 'ModelToDrawingViewTransform' returns object of type 'Matrix'
		"ModelToDrawingViewTransform": (117441563, 2, (9, 0), (), "ModelToDrawingViewTransform", '{CB69F171-558E-11D3-B793-0060B0F159EF}'),
		# Method 'ModelToSheetTransform' returns object of type 'Matrix'
		"ModelToSheetTransform": (117441565, 2, (9, 0), (), "ModelToSheetTransform", '{CB69F171-558E-11D3-B793-0060B0F159EF}'),
		"Name": (117441550, 2, (8, 0), (), "Name", None),
		# Method 'OriginIndicator' returns object of type 'OriginIndicator'
		"OriginIndicator": (117441610, 2, (9, 0), (), "OriginIndicator", '{96E36D73-DFEC-4CF8-9DB3-F97F01A41A23}'),
		# Method 'Parent' returns object of type 'Sheet'
		"Parent": (2130706434, 2, (9, 0), (), "Parent", '{206B59AE-22A6-11D4-B7A8-0060B0F159EF}'),
		# Method 'ParentView' returns object of type 'DrawingView'
		"ParentView": (117441566, 2, (9, 0), (), "ParentView", '{206B59B1-22A6-11D4-B7A8-0060B0F159EF}'),
		# Method 'Position' returns object of type 'Point2d'
		"Position": (117441603, 2, (9, 0), (), "Position", '{CB69F173-558E-11D3-B793-0060B0F159EF}'),
		"PresentationViewAssociative": (117441629, 2, (11, 0), (), "PresentationViewAssociative", None),
		# Method 'ReferencedDocumentDescriptor' returns object of type 'DocumentDescriptor'
		"ReferencedDocumentDescriptor": (117441586, 2, (9, 0), (), "ReferencedDocumentDescriptor", '{D755CFCA-9E02-4A08-AFE8-7178E818C763}'),
		# Method 'ReferencedFile' returns object of type 'ReferencedFileDescriptor'
		"ReferencedFile": (117441552, 2, (9, 0), (), "ReferencedFile", '{9E0BA9CA-E916-11D2-B785-0060B0F159EF}'),
		"Rotation": (117441599, 2, (5, 0), (), "Rotation", None),
		"Scale": (117441541, 2, (5, 0), (), "Scale", None),
		"ScaleFromBase": (117441577, 2, (11, 0), (), "ScaleFromBase", None),
		"ScaleString": (117441598, 2, (8, 0), (), "ScaleString", None),
		# Method 'SheetToDrawingViewTransform' returns object of type 'Matrix'
		"SheetToDrawingViewTransform": (117441570, 2, (9, 0), (), "SheetToDrawingViewTransform", '{CB69F171-558E-11D3-B793-0060B0F159EF}'),
		# Method 'SheetToModelTransform' returns object of type 'Matrix'
		"SheetToModelTransform": (117441568, 2, (9, 0), (), "SheetToModelTransform", '{CB69F171-558E-11D3-B793-0060B0F159EF}'),
		"ShowLabel": (117441611, 2, (11, 0), (), "ShowLabel", None),
		"ShowName": (117441574, 2, (11, 0), (), "ShowName", None),
		"ShowScale": (117441573, 2, (11, 0), (), "ShowScale", None),
		# Method 'Sketches' returns object of type 'DrawingSketches'
		"Sketches": (117441551, 2, (9, 0), (), "Sketches", '{1644E1D7-9BD5-11D5-8DF7-0010B541CAA8}'),
		"StandardPartsSectionBehavior": (117441631, 2, (3, 0), (), "StandardPartsSectionBehavior", None),
		"Suppressed": (117441606, 2, (11, 0), (), "Suppressed", None),
		"Top": (117441542, 2, (5, 0), (), "Top", None),
		"Type": (0, 2, (3, 0), (), "Type", None),
		"UpToDate": (117441597, 2, (11, 0), (), "UpToDate", None),
		"ViewJustification": (117441632, 2, (3, 0), (), "ViewJustification", None),
		"ViewOrientationFromBase": (117441638, 2, (11, 0), (), "ViewOrientationFromBase", None),
		"ViewStyle": (117441584, 2, (3, 0), (), "ViewStyle", None),
		"ViewType": (117441537, 2, (3, 0), (), "ViewType", None),
		"Width": (117441545, 2, (5, 0), (), "Width", None),
		# Method '_Center' returns object of type 'Point2d'
		"_Center": (117441553, 2, (9, 0), (), "_Center", '{CB69F173-558E-11D3-B793-0060B0F159EF}'),
	}
	_prop_map_put_ = {
		"ActiveLevelOfDetailRepresentation": ((117441593, LCID, 4, 0),()),
		"ActiveMemberName": ((117441594, LCID, 4, 0),()),
		"ActivePositionalRepresentation": ((117441590, LCID, 4, 0),()),
		"Aligned": ((117441615, LCID, 4, 0),()),
		"Center": ((117441602, LCID, 4, 0),()),
		"DisplayBendExtents": ((117441617, LCID, 4, 0),()),
		"DisplayDefinitionInBase": ((117441618, LCID, 4, 0),()),
		"DisplayForeshortenedTangentEdges": ((117441621, LCID, 4, 0),()),
		"DisplayHatching": ((117441619, LCID, 4, 0),()),
		"DisplayInterferenceEdges": ((117441620, LCID, 4, 0),()),
		"DisplayTangentEdges": ((117441596, LCID, 4, 0),()),
		"DisplayThreadFeatures": ((117441622, LCID, 4, 0),()),
		"DisplayTrails": ((117441623, LCID, 4, 0),()),
		"GeneralDimensionType": ((117441601, LCID, 4, 0),()),
		"IncludeMeshBodies": ((117441641, LCID, 4, 0),()),
		"IncludeSurfaceBodies": ((117441642, LCID, 4, 0),()),
		"InheritBreak": ((117441625, LCID, 4, 0),()),
		"InheritBreakOut": ((117441626, LCID, 4, 0),()),
		"InheritSection": ((117441627, LCID, 4, 0),()),
		"InheritSlice": ((117441628, LCID, 4, 0),()),
		"IsRasterView": ((117441640, LCID, 4, 0),()),
		"Name": ((117441550, LCID, 4, 0),()),
		"Position": ((117441603, LCID, 4, 0),()),
		"PresentationViewAssociative": ((117441629, LCID, 4, 0),()),
		"Rotation": ((117441599, LCID, 4, 0),()),
		"Scale": ((117441541, LCID, 4, 0),()),
		"ScaleFromBase": ((117441577, LCID, 4, 0),()),
		"ScaleString": ((117441598, LCID, 4, 0),()),
		"ShowLabel": ((117441611, LCID, 4, 0),()),
		"ShowName": ((117441574, LCID, 4, 0),()),
		"ShowScale": ((117441573, LCID, 4, 0),()),
		"StandardPartsSectionBehavior": ((117441631, LCID, 4, 0),()),
		"Suppressed": ((117441606, LCID, 4, 0),()),
		"ViewJustification": ((117441632, LCID, 4, 0),()),
		"ViewOrientationFromBase": ((117441638, LCID, 4, 0),()),
		"ViewStyle": ((117441584, LCID, 4, 0),()),
		"_Center": ((117441553, LCID, 4, 0),()),
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

win32com.client.CLSIDToClass.RegisterCLSID( "{206B59B1-22A6-11D4-B7A8-0060B0F159EF}", DrawingView )
