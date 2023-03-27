# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 19:09:30 2023
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
class LoftFeature(DispatchBaseClass):
	'Part Loft Feature Object'
	CLSID = IID('{F7DDBE1D-2C8E-48B9-9E52-FC0BFB7D59A6}')
	coclass_clsid = None

	def Delete(self, RetainConsumedSketches=False, RetainDependentFeaturesAndSketches=False, RetainDependentWorkFeatures=False):
		'Delete this feature from the model'
		return self._oleobj_.InvokeTypes(83886851, LCID, 1, (24, 0), ((11, 49), (11, 49), (11, 49)),RetainConsumedSketches
			, RetainDependentFeaturesAndSketches, RetainDependentWorkFeatures)

	def GetReferenceKey(self, ReferenceKey=defaultNamedNotOptArg, KeyContext=0):
		"Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object"
		return self._ApplyTypes_(2130706454, 1, (24, 0), ((24593, 3), (3, 49)), 'GetReferenceKey', None,ReferenceKey
			, KeyContext)

	# Result is of type RenderStyle
	def GetRenderStyle(self, StyleSourceType=pythoncom.Missing):
		'Gets the render style currently used for this feature'
		return self._ApplyTypes_(83886859, 1, (9, 0), ((16387, 2),), 'GetRenderStyle', '{D480B516-E785-4CEE-B43C-FD4E3B6055F4}',StyleSourceType
			)

	def GetSuppressionCondition(self, Parameter=pythoncom.Missing, ComparisonType=pythoncom.Missing, Expression=pythoncom.Missing):
		'Gets the suppression condition for this feature'
		return self._ApplyTypes_(83886866, 1, (11, 0), ((16393, 2), (16387, 2), (16396, 2)), 'GetSuppressionCondition', None,Parameter
			, ComparisonType, Expression)

	def RemoveParticipant(self, Occurrence=defaultNamedNotOptArg):
		'Remove the specified occurrence from the list of participants for this feature.  This method only applies to assembly features'
		return self._oleobj_.InvokeTypes(83886863, LCID, 1, (24, 0), ((9, 1),),Occurrence
			)

	def SetAffectedBodies(self, Bodies=defaultNamedNotOptArg):
		'Method that sets a collection of SurfaceBody objects affected by this feature'
		return self._oleobj_.InvokeTypes(83886873, LCID, 1, (24, 0), ((9, 1),),Bodies
			)

	def SetEndOfPart(self, Before=defaultNamedNotOptArg):
		'Method that repositions the end of part marker relative to the object'
		return self._oleobj_.InvokeTypes(2130706472, LCID, 1, (24, 0), ((11, 1),),Before
			)

	def SetRenderStyle(self, StyleSourceType=defaultNamedNotOptArg, RenderStyle=defaultNamedOptArg):
		'Sets the render style to use for this feature'
		return self._oleobj_.InvokeTypes(83886861, LCID, 1, (24, 0), ((3, 1), (12, 17)),StyleSourceType
			, RenderStyle)

	def SetSuppressionCondition(self, Parameter=defaultNamedNotOptArg, ComparisonType=defaultNamedNotOptArg, Expression=defaultNamedNotOptArg):
		'Sets the suppression condition for this feature'
		return self._oleobj_.InvokeTypes(83886867, LCID, 1, (24, 0), ((9, 1), (3, 1), (12, 1)),Parameter
			, ComparisonType, Expression)

	_prop_map_get_ = {
		"Adaptive": (83886853, 2, (11, 0), (), "Adaptive", None),
		# Method 'Appearance' returns object of type 'Asset'
		"Appearance": (83886875, 2, (9, 0), (), "Appearance", '{766A9447-A604-43C8-9393-2D2709837D1E}'),
		"AppearanceSourceType": (83886876, 2, (3, 0), (), "AppearanceSourceType", None),
		"Application": (2130706433, 2, (9, 0), (), "Application", None),
		# Method 'AttributeSets' returns object of type 'AttributeSets'
		"AttributeSets": (2130706452, 2, (9, 0), (), "AttributeSets", '{790B4EB3-7947-4D08-9510-372E93A24CF1}'),
		"Centerline": (83912719, 2, (9, 0), (), "Centerline", None),
		"Closed": (83912705, 2, (11, 0), (), "Closed", None),
		"ConsumeInputs": (83886868, 2, (11, 0), (), "ConsumeInputs", None),
		# Method 'Definition' returns object of type 'LoftDefinition'
		"Definition": (83912727, 2, (9, 0), (), "Definition", '{FBEBA281-9346-4AC6-B324-6CEB7318BEBE}'),
		# Method 'EndFace' returns object of type 'Face'
		"EndFace": (83912707, 2, (9, 0), (), "EndFace", '{5DF8608B-6B16-11D3-B794-0060B0F159EF}'),
		"ExtendedName": (83886874, 2, (8, 0), (), "ExtendedName", None),
		# Method 'Faces' returns object of type 'Faces'
		"Faces": (83886854, 2, (9, 0), (), "Faces", '{5DF86092-6B16-11D3-B794-0060B0F159EF}'),
		# Method 'FeatureDimensions' returns object of type 'FeatureDimensions'
		"FeatureDimensions": (83886871, 2, (9, 0), (), "FeatureDimensions", '{44A143D3-13C8-4B0A-AE53-CCC6169C44DB}'),
		# Method 'FirstSectionAngle' returns object of type 'Parameter'
		"FirstSectionAngle": (83912709, 2, (9, 0), (), "FirstSectionAngle", '{44E517BC-D882-4AFE-A300-B3DAC6B8DB58}'),
		"FirstSectionCondition": (83912710, 2, (3, 0), (), "FirstSectionCondition", None),
		"FirstSectionDirectionReversed": (83912720, 2, (11, 0), (), "FirstSectionDirectionReversed", None),
		# Method 'FirstSectionImpact' returns object of type 'Parameter'
		"FirstSectionImpact": (83912711, 2, (9, 0), (), "FirstSectionImpact", '{44E517BC-D882-4AFE-A300-B3DAC6B8DB58}'),
		"FirstSectionTangentPlane": (83912721, 2, (9, 0), (), "FirstSectionTangentPlane", None),
		"HealthStatus": (83886850, 2, (3, 0), (), "HealthStatus", None),
		"IsOwnedByFeature": (83886869, 2, (11, 0), (), "IsOwnedByFeature", None),
		# Method 'LastSectionAngle' returns object of type 'Parameter'
		"LastSectionAngle": (83912712, 2, (9, 0), (), "LastSectionAngle", '{44E517BC-D882-4AFE-A300-B3DAC6B8DB58}'),
		"LastSectionCondition": (83912713, 2, (3, 0), (), "LastSectionCondition", None),
		"LastSectionDirectionReversed": (83912722, 2, (11, 0), (), "LastSectionDirectionReversed", None),
		# Method 'LastSectionImpact' returns object of type 'Parameter'
		"LastSectionImpact": (83912714, 2, (9, 0), (), "LastSectionImpact", '{44E517BC-D882-4AFE-A300-B3DAC6B8DB58}'),
		"LastSectionTangentPlane": (83912723, 2, (9, 0), (), "LastSectionTangentPlane", None),
		# Method 'LoftRails' returns object of type 'LoftRails'
		"LoftRails": (83912724, 2, (9, 0), (), "LoftRails", '{3E43E559-0053-402D-BE5F-4AC170C11A04}'),
		"LoftType": (83912725, 2, (3, 0), (), "LoftType", None),
		# Method 'MapPointCurves' returns object of type 'MapPointCurves'
		"MapPointCurves": (83912715, 2, (9, 0), (), "MapPointCurves", '{E405BACE-0EE8-4427-B6BE-82CC11F9CC35}'),
		"MergeTangentFaces": (83912726, 2, (11, 0), (), "MergeTangentFaces", None),
		"Name": (83886849, 2, (8, 0), (), "Name", None),
		"Operation": (83912716, 2, (3, 0), (), "Operation", None),
		# Method 'OwnedBy' returns object of type 'PartFeature'
		"OwnedBy": (83886870, 2, (9, 0), (), "OwnedBy", '{DA33F1A4-7C3F-11D3-B794-0060B0F159EF}'),
		# Method 'Parameters' returns object of type 'ParametersEnumerator'
		"Parameters": (83886864, 2, (9, 0), (), "Parameters", '{C52EE54D-B18E-4CB3-AEE3-7D0375F92948}'),
		# Method 'Parent' returns object of type 'ComponentDefinition'
		"Parent": (2130706434, 2, (9, 0), (), "Parent", '{5DF8601E-6B16-11D3-B794-0060B0F159EF}'),
		# Method 'Participants' returns object of type 'ComponentOccurrencesEnumerator'
		"Participants": (83886862, 2, (9, 0), (), "Participants", '{EF562DD1-92FA-11D4-8DE0-0010B541CAA8}'),
		# Method 'Rails' returns object of type 'ObjectCollection'
		"Rails": (83912717, 2, (9, 0), (), "Rails", '{6939FFDD-BA10-11D2-B779-0060B0F159EF}'),
		# Method 'RangeBox' returns object of type 'Box'
		"RangeBox": (83886852, 2, (9, 0), (), "RangeBox", '{5DF86062-6B16-11D3-B794-0060B0F159EF}'),
		# Method 'Sections' returns object of type 'ObjectCollection'
		"Sections": (83912718, 2, (9, 0), (), "Sections", '{6939FFDD-BA10-11D2-B779-0060B0F159EF}'),
		"Shared": (83886865, 2, (11, 0), (), "Shared", None),
		# Method 'SideFaces' returns object of type 'Faces'
		"SideFaces": (83912708, 2, (9, 0), (), "SideFaces", '{5DF86092-6B16-11D3-B794-0060B0F159EF}'),
		# Method 'StartFace' returns object of type 'Face'
		"StartFace": (83912706, 2, (9, 0), (), "StartFace", '{5DF8608B-6B16-11D3-B794-0060B0F159EF}'),
		"Suppressed": (83886858, 2, (11, 0), (), "Suppressed", None),
		# Method 'SurfaceBodies' returns object of type 'SurfaceBodies'
		"SurfaceBodies": (83886872, 2, (9, 0), (), "SurfaceBodies", '{5DF860AE-6B16-11D3-B794-0060B0F159EF}'),
		# Method 'SurfaceBody' returns object of type 'SurfaceBody'
		"SurfaceBody": (83886857, 2, (9, 0), (), "SurfaceBody", '{5DF86089-6B16-11D3-B794-0060B0F159EF}'),
		"Type": (2130706435, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Adaptive": ((83886853, LCID, 4, 0),()),
		"Appearance": ((83886875, LCID, 4, 0),()),
		"AppearanceSourceType": ((83886876, LCID, 4, 0),()),
		"ConsumeInputs": ((83886868, LCID, 4, 0),()),
		"Definition": ((83912727, LCID, 4, 0),()),
		"Name": ((83886849, LCID, 4, 0),()),
		"Shared": ((83886865, LCID, 4, 0),()),
		"Suppressed": ((83886858, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{F7DDBE1D-2C8E-48B9-9E52-FC0BFB7D59A6}", LoftFeature )
