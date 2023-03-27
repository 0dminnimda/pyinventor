# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 16:47:33 2023
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
class PartComponentDefinition(DispatchBaseClass):
	'PartComponentDefinition Object'
	CLSID = IID('{DA33F1A3-7C3F-11D3-B794-0060B0F159EF}')
	coclass_clsid = None

	def ClearAppearanceOverrides(self, AppearanceOverrideObjects=defaultNamedOptArg):
		'Clears the appearance overrides on the provided objects. The objects can include faces, features, work surfaces, surface bodies and occurrences.'
		return self._oleobj_.InvokeTypes(83886633, LCID, 1, (24, 0), ((12, 17),),AppearanceOverrideObjects
			)

	# Result is of type iPartFactory
	def CreateFactory(self):
		'Converts a part to an iPart factory'
		ret = self._oleobj_.InvokeTypes(83886609, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CreateFactory', '{B9F30FBA-DABE-4327-AAB3-65E2160135C1}')
		return ret

	# Result is of type GeometryIntent
	def CreateGeometryIntent(self, Geometry=defaultNamedNotOptArg, Intent=defaultNamedOptArg):
		'Method that creates a GeometryIntent object.  GeometryIntent objects are used as input when creating annotations in the model.  They are used to identify geometry and optionally specific locations on that geometry.'
		ret = self._oleobj_.InvokeTypes(83886635, LCID, 1, (9, 0), ((9, 1), (12, 17)),Geometry
			, Intent)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGeometryIntent', '{56B990B9-D25A-436F-A652-1D21EC739C57}')
		return ret

	def DeleteObjects(self, Objects=defaultNamedNotOptArg, RetainConsumedSketches=False, RetainDepFeatsAndSketches=False, RetainDepWorkFeats=False):
		'Deletes a collection of objects that belong to the part'
		return self._oleobj_.InvokeTypes(83886618, LCID, 1, (24, 0), ((9, 1), (11, 49), (11, 49), (11, 49)),Objects
			, RetainConsumedSketches, RetainDepFeatsAndSketches, RetainDepWorkFeats)

	def ExportObjects(self, Objects=defaultNamedNotOptArg):
		'Marks all the input objects as exported'
		return self._oleobj_.InvokeTypes(83886629, LCID, 1, (24, 0), ((9, 1),),Objects
			)

	# Result is of type ObjectsEnumerator
	def FindUsingPoint(self, Point=defaultNamedNotOptArg, ObjectTypes=defaultNamedNotOptArg, ProximityTolerance=defaultNamedNotOptArg, VisibleObjectsOnly=True):
		'Finds all the entities of the specified type at the specified location.'
		ret = self._oleobj_.InvokeTypes(67113286, LCID, 1, (9, 0), ((9, 1), (24579, 1), (12, 17), (11, 49)),Point
			, ObjectTypes, ProximityTolerance, VisibleObjectsOnly)
		if ret is not None:
			ret = Dispatch(ret, 'FindUsingPoint', '{A94DCF5E-90E9-4F60-BB55-F65B4618ECD5}')
		return ret

	def FindUsingRay(self, RayStartPoint=defaultNamedNotOptArg, RayDirection=defaultNamedNotOptArg, Radius=defaultNamedNotOptArg, FoundEntities=pythoncom.Missing
			, LocationPoints=pythoncom.Missing, FindFirstOnly=False):
		'Find the lowest order brep topology entities found by firing the specified ray onto the model'
		return self._ApplyTypes_(83886608, 1, (24, 0), ((9, 1), (9, 1), (5, 1), (16393, 2), (16393, 2), (11, 49)), 'FindUsingRay', None,RayStartPoint
			, RayDirection, Radius, FoundEntities, LocationPoints, FindFirstOnly
			)

	# Result is of type ObjectsEnumerator
	def FindUsingVector(self, OriginPoint=defaultNamedNotOptArg, Direction=defaultNamedNotOptArg, ObjectTypes=defaultNamedNotOptArg, UseCylinder=True
			, ProximityTolerance=defaultNamedNotOptArg, VisibleObjectsOnly=True, LocationPoints=pythoncom.Missing):
		'Finds all the entities of the specified type along the specified vector.'
		return self._ApplyTypes_(67113287, 1, (9, 0), ((9, 1), (9, 1), (24579, 1), (11, 49), (12, 17), (11, 49), (16396, 18)), 'FindUsingVector', '{A94DCF5E-90E9-4F60-BB55-F65B4618ECD5}',OriginPoint
			, Direction, ObjectTypes, UseCylinder, ProximityTolerance, VisibleObjectsOnly
			, LocationPoints)

	def GetEndOfPartPosition(self, After=pythoncom.Missing, Before=pythoncom.Missing):
		'Gets the current end of part position in the browser in parts'
		return self._ApplyTypes_(83886623, 1, (24, 0), ((16393, 2), (16393, 2)), 'GetEndOfPartPosition', None,After
			, Before)

	def SetEndOfPartToTopOrBottom(self, SetToTop=defaultNamedNotOptArg):
		'Sets the End of Part marker to the top or bottom of the browser.'
		return self._oleobj_.InvokeTypes(83886617, LCID, 1, (24, 0), ((11, 1),),SetToTop
			)

	def SuppressFeatures(self, Features=defaultNamedNotOptArg):
		'Suppresses the input set of features and their dependents'
		return self._oleobj_.InvokeTypes(83886621, LCID, 1, (24, 0), ((9, 1),),Features
			)

	def UnsuppressFeatures(self, Features=defaultNamedNotOptArg):
		'Unsuppresses the input set of features'
		return self._oleobj_.InvokeTypes(83886622, LCID, 1, (24, 0), ((9, 1),),Features
			)

	def _AutoStitchAndPromote(self):
		'Hidden property. Not for public use. Attempts to auto stitch the entire contents of the explicit environment and promote the solid result.'
		return self._oleobj_.InvokeTypes(83886600, LCID, 1, (24, 0), (),)

	def _InvalidateSketchNodes(self):
		'Invalidates the scene node for active sketch or all unconsumed sketches and consumed visible sketches. Performance degradation warning.'
		return self._oleobj_.InvokeTypes(67113284, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'AnalysisManager' returns object of type 'AnalysisManager'
		"AnalysisManager": (83886620, 2, (9, 0), (), "AnalysisManager", '{BB075EDC-49B3-4F03-8737-5E20737B1AEB}'),
		# Method 'AnnotationPlanes' returns object of type 'AnnotationPlanes'
		"AnnotationPlanes": (83886636, 2, (9, 0), (), "AnnotationPlanes", '{02F3D9FA-F750-4C1B-8A2E-A2C5BB99C76C}'),
		# Method 'AppearanceOverridesObjects' returns object of type 'ObjectsEnumerator'
		"AppearanceOverridesObjects": (83886632, 2, (9, 0), (), "AppearanceOverridesObjects", '{A94DCF5E-90E9-4F60-BB55-F65B4618ECD5}'),
		"Application": (2130706433, 2, (9, 0), (), "Application", None),
		# Method 'AttributeSets' returns object of type 'AttributeSets'
		"AttributeSets": (2130706452, 2, (9, 0), (), "AttributeSets", '{790B4EB3-7947-4D08-9510-372E93A24CF1}'),
		# Method 'BIMComponent' returns object of type 'BIMComponent'
		"BIMComponent": (83886631, 2, (9, 0), (), "BIMComponent", '{47005682-42D1-4831-A4BC-63AD38B98D6E}'),
		# Method 'BOMQuantity' returns object of type 'BOMQuantity'
		"BOMQuantity": (67113283, 2, (9, 0), (), "BOMQuantity", '{07F8CD55-9194-4CDB-8403-6BFC4F99D1EE}'),
		"BOMStructure": (67113282, 2, (3, 0), (), "BOMStructure", None),
		# Method 'ClientGraphicsCollection' returns object of type 'ClientGraphicsCollection'
		"ClientGraphicsCollection": (67113280, 2, (9, 0), (), "ClientGraphicsCollection", '{66829BB6-656B-431C-BF5C-0BF53DBA225D}'),
		"CompactModelHistory": (83886606, 2, (11, 0), (), "CompactModelHistory", None),
		"CompactModelHistoryOnNextSave": (83886607, 2, (11, 0), (), "CompactModelHistoryOnNextSave", None),
		# Method 'DataIO' returns object of type 'DataIO'
		"DataIO": (67113273, 2, (9, 0), (), "DataIO", '{FBCADB33-9CBE-11D3-B799-0060B0F159EF}'),
		"Document": (67113270, 2, (9, 0), (), "Document", None),
		# Method 'Features' returns object of type 'PartFeatures'
		"Features": (83886593, 2, (9, 0), (), "Features", '{DA33F1A5-7C3F-11D3-B794-0060B0F159EF}'),
		"HasMultipleSolidBodies": (83886627, 2, (11, 0), (), "HasMultipleSolidBodies", None),
		# Method 'ImmediateReferencedDefinitions' returns object of type 'ComponentDefinitionReferences'
		"ImmediateReferencedDefinitions": (67113269, 2, (9, 0), (), "ImmediateReferencedDefinitions", '{5DF86023-6B16-11D3-B794-0060B0F159EF}'),
		"IsContentMember": (83886628, 2, (11, 0), (), "IsContentMember", None),
		"IsiPartFactory": (83886612, 2, (11, 0), (), "IsiPartFactory", None),
		"IsiPartMember": (83886613, 2, (11, 0), (), "IsiPartMember", None),
		# Method 'MassProperties' returns object of type 'MassProperties'
		"MassProperties": (83886604, 2, (9, 0), (), "MassProperties", '{2FA1D3CF-EAFF-4D47-9E13-E5B074C1565C}'),
		# Method 'Material' returns object of type 'Material'
		"Material": (83886602, 2, (9, 0), (), "Material", '{57CFD4EC-1776-48D3-B5C4-7B6E015D0541}'),
		# Method 'MeshFeatureSets' returns object of type 'MeshFeatureSets'
		"MeshFeatureSets": (83886638, 2, (9, 0), (), "MeshFeatureSets", '{D6DB0745-4B18-4A22-8F03-DD12B0D444E0}'),
		# Method 'ModelAnnotations' returns object of type 'ModelAnnotations'
		"ModelAnnotations": (83886634, 2, (9, 0), (), "ModelAnnotations", '{9789E1AC-1767-4225-96DD-FD06F614AD59}'),
		# Method 'ModelDatumReferenceFrames' returns object of type 'ModelDatumReferenceFrames'
		"ModelDatumReferenceFrames": (83886640, 2, (9, 0), (), "ModelDatumReferenceFrames", '{10F5BF67-5FAB-44DD-B1D8-BCE056E71000}'),
		"ModelGeometryVersion": (67113281, 2, (8, 0), (), "ModelGeometryVersion", None),
		# Method 'ModelToleranceFeatures' returns object of type 'ModelToleranceFeatures'
		"ModelToleranceFeatures": (83886639, 2, (9, 0), (), "ModelToleranceFeatures", '{496CD658-85F0-449A-BA13-9B94962ACBEA}'),
		# Method 'Occurrences' returns object of type 'ComponentOccurrences'
		"Occurrences": (67113268, 2, (9, 0), (), "Occurrences", '{5DF86024-6B16-11D3-B794-0060B0F159EF}'),
		# Method 'Parameters' returns object of type 'Parameters'
		"Parameters": (83886594, 2, (9, 0), (), "Parameters", '{528C9A32-4173-420A-AD05-B6FBF8382212}'),
		# Method 'PartEvents' returns object of type 'PartEvents'
		"PartEvents": (83886598, 2, (13, 0), (), "PartEvents", '{BABF5BB7-9878-11D4-8DE2-0010B541CAA8}'),
		# Method 'PointClouds' returns object of type 'PointClouds'
		"PointClouds": (83886637, 2, (9, 0), (), "PointClouds", '{715899F9-C5E6-4A31-96C7-151D74A852B8}'),
		# Method 'RangeBox' returns object of type 'Box'
		"RangeBox": (67113285, 2, (9, 0), (), "RangeBox", '{5DF86062-6B16-11D3-B794-0060B0F159EF}'),
		# Method 'ReferenceComponents' returns object of type 'ReferenceComponents'
		"ReferenceComponents": (83886605, 2, (9, 0), (), "ReferenceComponents", '{45D64D2D-8D31-4ABD-BB94-E55F0879A90C}'),
		# Method 'RepresentationsManager' returns object of type 'RepresentationsManager'
		"RepresentationsManager": (83886630, 2, (9, 0), (), "RepresentationsManager", '{B25D15A6-B823-42FF-9ABB-781A3043ECB0}'),
		"RolledBackForEdit": (83886619, 2, (11, 0), (), "RolledBackForEdit", None),
		# Method 'SketchBlockDefinitions' returns object of type 'SketchBlockDefinitions'
		"SketchBlockDefinitions": (83886624, 2, (9, 0), (), "SketchBlockDefinitions", '{BC450138-0F96-4342-BC2C-239747CD4797}'),
		# Method 'Sketches' returns object of type 'PlanarSketches'
		"Sketches": (83886599, 2, (9, 0), (), "Sketches", '{A03B2CAF-A5F8-4522-BF79-CF4D497DCF4E}'),
		# Method 'Sketches3D' returns object of type 'Sketches3D'
		"Sketches3D": (83886614, 2, (9, 0), (), "Sketches3D", '{07FB0B7F-D08F-473F-8EF0-A5E6B4CBA3BC}'),
		# Method 'SurfaceBodies' returns object of type 'SurfaceBodies'
		"SurfaceBodies": (67113265, 2, (9, 0), (), "SurfaceBodies", '{5DF860AE-6B16-11D3-B794-0060B0F159EF}'),
		"Type": (2130706435, 2, (3, 0), (), "Type", None),
		# Method 'UserCoordinateSystems' returns object of type 'UserCoordinateSystems'
		"UserCoordinateSystems": (83886626, 2, (9, 0), (), "UserCoordinateSystems", '{D0BD7B89-04B5-4165-8E8D-1DB705A02E47}'),
		# Method 'WorkAxes' returns object of type 'WorkAxes'
		"WorkAxes": (83886596, 2, (9, 0), (), "WorkAxes", '{28DD48B5-8D70-11D4-8DDE-0010B541CAA8}'),
		# Method 'WorkPlanes' returns object of type 'WorkPlanes'
		"WorkPlanes": (83886595, 2, (9, 0), (), "WorkPlanes", '{46785C3B-7F4A-11D4-8DDB-0010B541CAA8}'),
		# Method 'WorkPoints' returns object of type 'WorkPoints'
		"WorkPoints": (83886597, 2, (9, 0), (), "WorkPoints", '{28DD48C7-8D70-11D4-8DDE-0010B541CAA8}'),
		# Method 'WorkSurfaces' returns object of type 'WorkSurfaces'
		"WorkSurfaces": (83886615, 2, (9, 0), (), "WorkSurfaces", '{5987714B-D55A-4AED-8AE5-97C062EC1F68}'),
		# Method 'iMateDefinitions' returns object of type 'iMateDefinitions'
		"iMateDefinitions": (83886616, 2, (9, 0), (), "iMateDefinitions", '{AE309209-288A-4083-BEAB-7DFB7EC9947D}'),
		# Method 'iPartFactory' returns object of type 'iPartFactory'
		"iPartFactory": (83886610, 2, (9, 0), (), "iPartFactory", '{B9F30FBA-DABE-4327-AAB3-65E2160135C1}'),
		# Method 'iPartMember' returns object of type 'iPartMember'
		"iPartMember": (83886611, 2, (9, 0), (), "iPartMember", '{2DB692B1-9CA2-40CA-AD6B-D1250C063724}'),
	}
	_prop_map_put_ = {
		"BOMStructure": ((67113282, LCID, 4, 0),()),
		"CompactModelHistory": ((83886606, LCID, 4, 0),()),
		"CompactModelHistoryOnNextSave": ((83886607, LCID, 4, 0),()),
		"Material": ((83886602, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{DA33F1A3-7C3F-11D3-B794-0060B0F159EF}", PartComponentDefinition )
