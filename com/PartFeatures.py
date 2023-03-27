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
class PartFeatures(DispatchBaseClass):
	'Part Feature Collection Object. Presents the current view of Part Features and allows their creation'
	CLSID = IID('{DA33F1A5-7C3F-11D3-B794-0060B0F159EF}')
	coclass_clsid = None

	# Result is of type Path
	def CreatePath(self, SketchCurve=defaultNamedNotOptArg):
		'Method that creates a path used to define the shape of several part features such as sweep, rectangular pattern, split, etc. All other 2D and 3D curves that are connected to the input curve are obtained and used to create a Path object. The new Path is returne'
		ret = self._oleobj_.InvokeTypes(83887130, LCID, 1, (9, 0), ((9, 1),),SketchCurve
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePath', '{86338055-4538-47A0-BD9B-06A8C4BD8D93}')
		return ret

	# Result is of type Path
	def CreateSpecifiedPath(self, SketchCurves=defaultNamedNotOptArg):
		'Method that creates a path used to define the shape of several part features such as sweep, rectangular pattern, split, etc. The new path is returned. This method will fail if the input curves are not connected end-to-end.'
		ret = self._oleobj_.InvokeTypes(83887131, LCID, 1, (9, 0), ((9, 1),),SketchCurves
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSpecifiedPath', '{86338055-4538-47A0-BD9B-06A8C4BD8D93}')
		return ret

	# Result is of type PartFeature
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{DA33F1A4-7C3F-11D3-B794-0060B0F159EF}')
		return ret

	_prop_map_get_ = {
		# Method 'AliasFreeformFeatures' returns object of type 'AliasFreeformFeatures'
		"AliasFreeformFeatures": (83887149, 2, (9, 0), (), "AliasFreeformFeatures", '{3C007201-8D66-47BD-AD94-2012FF75C4C5}'),
		"Application": (2130706433, 2, (9, 0), (), "Application", None),
		# Method 'BendPartFeatures' returns object of type 'BendPartFeatures'
		"BendPartFeatures": (83887138, 2, (9, 0), (), "BendPartFeatures", '{3E39E3B3-FA8E-463D-A191-6D7A7CB8E7AE}'),
		# Method 'BossFeatures' returns object of type 'BossFeatures'
		"BossFeatures": (83887142, 2, (9, 0), (), "BossFeatures", '{A110C93B-A3B5-4717-A697-87EA0126216F}'),
		# Method 'BoundaryPatchFeatures' returns object of type 'BoundaryPatchFeatures'
		"BoundaryPatchFeatures": (83887132, 2, (9, 0), (), "BoundaryPatchFeatures", '{97D6B280-1D62-48E6-B4B9-007F25F7A3A5}'),
		# Method 'ChamferFeatures' returns object of type 'ChamferFeatures'
		"ChamferFeatures": (83887105, 2, (9, 0), (), "ChamferFeatures", '{2D38284B-DEAD-48C3-905D-02D1B7432699}'),
		# Method 'CircularPatternFeatures' returns object of type 'CircularPatternFeatures'
		"CircularPatternFeatures": (83887106, 2, (9, 0), (), "CircularPatternFeatures", '{E2E51C17-C894-45AF-9827-988D38C283C7}'),
		# Method 'ClientFeatures' returns object of type 'ClientFeatures'
		"ClientFeatures": (83887137, 2, (9, 0), (), "ClientFeatures", '{68AF2955-0901-433D-B7C3-D91D637DD21C}'),
		# Method 'CoilFeatures' returns object of type 'CoilFeatures'
		"CoilFeatures": (83887107, 2, (9, 0), (), "CoilFeatures", '{2C30965F-FD0D-4D6E-AC98-797F2F0E2DEB}'),
		# Method 'CombineFeatures' returns object of type 'CombineFeatures'
		"CombineFeatures": (83887140, 2, (9, 0), (), "CombineFeatures", '{010971C0-0359-4820-A5EA-5EB9E6FFDA76}'),
		# Method 'CoreCavityFeatures' returns object of type 'CoreCavityFeatures'
		"CoreCavityFeatures": (83887148, 2, (9, 0), (), "CoreCavityFeatures", '{C44DF7B9-A598-407F-AE04-2594D11B9DC7}'),
		"Count": (2130706438, 2, (3, 0), (), "Count", None),
		# Method 'DecalFeatures' returns object of type 'DecalFeatures'
		"DecalFeatures": (83887124, 2, (9, 0), (), "DecalFeatures", '{0218B59B-0CE5-4CA1-9A3B-F7D266C4E75F}'),
		# Method 'DeleteFaceFeatures' returns object of type 'DeleteFaceFeatures'
		"DeleteFaceFeatures": (83887125, 2, (9, 0), (), "DeleteFaceFeatures", '{91BDBCAB-AC12-4216-ACE4-4F561D7DD4BD}'),
		# Method 'DirectEditFeatures' returns object of type 'DirectEditFeatures'
		"DirectEditFeatures": (83887153, 2, (9, 0), (), "DirectEditFeatures", '{69F95DF7-6F84-4FF8-8060-AB921DF1E4F1}'),
		# Method 'EmbossFeatures' returns object of type 'EmbossFeatures'
		"EmbossFeatures": (83887126, 2, (9, 0), (), "EmbossFeatures", '{730B9714-80D2-4009-8904-1AEF4EAF3F23}'),
		# Method 'ExtendFeatures' returns object of type 'ExtendFeatures'
		"ExtendFeatures": (83887136, 2, (9, 0), (), "ExtendFeatures", '{4A355C86-508E-4A45-80C3-001139E9FD81}'),
		# Method 'ExtrudeFeatures' returns object of type 'ExtrudeFeatures'
		"ExtrudeFeatures": (83887108, 2, (9, 0), (), "ExtrudeFeatures", '{F05DFBBD-F824-48A1-8272-A62F1A524F42}'),
		# Method 'FaceDraftFeatures' returns object of type 'FaceDraftFeatures'
		"FaceDraftFeatures": (83887109, 2, (9, 0), (), "FaceDraftFeatures", '{C77D9639-C58A-4E5A-BAE0-14966E37DDEE}'),
		# Method 'FaceOffsetFeatures' returns object of type 'FaceOffsetFeatures'
		"FaceOffsetFeatures": (83887151, 2, (9, 0), (), "FaceOffsetFeatures", '{3FD23B6F-222D-485D-A9E8-164C497B17F8}'),
		# Method 'FilletFeatures' returns object of type 'FilletFeatures'
		"FilletFeatures": (83887110, 2, (9, 0), (), "FilletFeatures", '{94ABF5D8-E979-494E-84D3-883672074BD4}'),
		# Method 'FreeformFeatures' returns object of type 'FreeformFeatures'
		"FreeformFeatures": (83887152, 2, (9, 0), (), "FreeformFeatures", '{E15EF363-30C7-420B-91DE-B76BE5F6007F}'),
		# Method 'GrillFeatures' returns object of type 'GrillFeatures'
		"GrillFeatures": (83887143, 2, (9, 0), (), "GrillFeatures", '{6AC23513-A004-4DC5-B77D-6D18BCB5E43E}'),
		# Method 'HoleFeatures' returns object of type 'HoleFeatures'
		"HoleFeatures": (83887111, 2, (9, 0), (), "HoleFeatures", '{A0DB05CD-57E9-47C9-9D33-E648BB57226A}'),
		# Method 'KnitFeatures' returns object of type 'KnitFeatures'
		"KnitFeatures": (83887127, 2, (9, 0), (), "KnitFeatures", '{1426BDF8-DD91-4FF0-AD8D-BB0EC8797B24}'),
		# Method 'LipFeatures' returns object of type 'LipFeatures'
		"LipFeatures": (83887144, 2, (9, 0), (), "LipFeatures", '{2AD0B878-13E1-4BB0-BDFF-BBAA7DA553DD}'),
		# Method 'LoftFeatures' returns object of type 'LoftFeatures'
		"LoftFeatures": (83887112, 2, (9, 0), (), "LoftFeatures", '{24A0170B-C253-4A3C-9639-5DE9818A8F31}'),
		# Method 'MidSurfaceFeatures' returns object of type 'MidSurfaceFeatures'
		"MidSurfaceFeatures": (83887150, 2, (9, 0), (), "MidSurfaceFeatures", '{B148630A-2ECA-4159-8FF2-77CD1B7A79A5}'),
		# Method 'MirrorFeatures' returns object of type 'MirrorFeatures'
		"MirrorFeatures": (83887113, 2, (9, 0), (), "MirrorFeatures", '{26C57F9F-A6AC-4FCD-BE7C-DAE2F0940E8E}'),
		# Method 'MoveFaceFeatures' returns object of type 'MoveFaceFeatures'
		"MoveFaceFeatures": (83887133, 2, (9, 0), (), "MoveFaceFeatures", '{04370FAD-4F3A-4589-A7F8-6DFA839522D3}'),
		# Method 'MoveFeatures' returns object of type 'MoveFeatures'
		"MoveFeatures": (83887141, 2, (9, 0), (), "MoveFeatures", '{972006AB-5037-4850-AF98-8D3B5A55C1F4}'),
		# Method 'NonParametricBaseFeature' returns object of type 'NonParametricBaseFeature'
		"NonParametricBaseFeature": (83887121, 2, (9, 0), (), "NonParametricBaseFeature", '{1D09051E-D674-4ABE-BEC9-5A58016455B1}'),
		# Method 'NonParametricBaseFeatures' returns object of type 'NonParametricBaseFeatures'
		"NonParametricBaseFeatures": (83887123, 2, (9, 0), (), "NonParametricBaseFeatures", '{59E208A8-BB82-4322-92D6-DA364F8B9AB0}'),
		# Method 'RectangularPatternFeatures' returns object of type 'RectangularPatternFeatures'
		"RectangularPatternFeatures": (83887114, 2, (9, 0), (), "RectangularPatternFeatures", '{ADA699FB-D9E7-4879-A1A3-86D9F2C6F57F}'),
		# Method 'ReferenceFeatures' returns object of type 'ReferenceFeatures'
		"ReferenceFeatures": (83887122, 2, (9, 0), (), "ReferenceFeatures", '{347FB32C-79ED-4A5B-89B1-7B14FF6A9CA8}'),
		# Method 'ReplaceFaceFeatures' returns object of type 'ReplaceFaceFeatures'
		"ReplaceFaceFeatures": (83887128, 2, (9, 0), (), "ReplaceFaceFeatures", '{3CBD2849-0258-4583-9CE0-578A71CB7483}'),
		# Method 'RestFeatures' returns object of type 'RestFeatures'
		"RestFeatures": (83887145, 2, (9, 0), (), "RestFeatures", '{0E000A5B-67FD-4B23-A312-E6E5F444C045}'),
		# Method 'RevolveFeatures' returns object of type 'RevolveFeatures'
		"RevolveFeatures": (83887115, 2, (9, 0), (), "RevolveFeatures", '{8EB2E33C-2CF3-41E6-9B08-C0C0D15DF5EE}'),
		# Method 'RibFeatures' returns object of type 'RibFeatures'
		"RibFeatures": (83887116, 2, (9, 0), (), "RibFeatures", '{436A627D-919B-4B92-B242-268F7266D8A1}'),
		# Method 'RuleFilletFeatures' returns object of type 'RuleFilletFeatures'
		"RuleFilletFeatures": (83887146, 2, (9, 0), (), "RuleFilletFeatures", '{9B108AAB-237A-460D-BC99-40FAF5EABD65}'),
		# Method 'RuledSurfaceFeatures' returns object of type 'RuledSurfaceFeatures'
		"RuledSurfaceFeatures": (83887154, 2, (9, 0), (), "RuledSurfaceFeatures", '{721CC25E-D96C-4E25-BED5-04EF710574B4}'),
		# Method 'SculptFeatures' returns object of type 'SculptFeatures'
		"SculptFeatures": (83887134, 2, (9, 0), (), "SculptFeatures", '{EAADC3AE-D599-495E-A56C-FA79AE3E8848}'),
		# Method 'ShellFeatures' returns object of type 'ShellFeatures'
		"ShellFeatures": (83887117, 2, (9, 0), (), "ShellFeatures", '{3B4B3DE9-7B05-47A7-975A-2C370BBBF974}'),
		# Method 'SketchDrivenPatternFeatures' returns object of type 'SketchDrivenPatternFeatures'
		"SketchDrivenPatternFeatures": (83887155, 2, (9, 0), (), "SketchDrivenPatternFeatures", '{DC6DA623-B4F1-4185-B954-92F92F3C8E21}'),
		# Method 'SnapFitFeatures' returns object of type 'SnapFitFeatures'
		"SnapFitFeatures": (83887147, 2, (9, 0), (), "SnapFitFeatures", '{ED254D15-6E11-409A-83A0-BB085F017204}'),
		# Method 'SplitFeatures' returns object of type 'SplitFeatures'
		"SplitFeatures": (83887118, 2, (9, 0), (), "SplitFeatures", '{209DF795-8088-4158-969C-0CC120E0A2A3}'),
		# Method 'SweepFeatures' returns object of type 'SweepFeatures'
		"SweepFeatures": (83887119, 2, (9, 0), (), "SweepFeatures", '{CADFFDB1-11E6-4684-A35E-7EE2064AA46C}'),
		# Method 'ThickenFeatures' returns object of type 'ThickenFeatures'
		"ThickenFeatures": (83887129, 2, (9, 0), (), "ThickenFeatures", '{F59CE3B0-44CC-4FB5-9C81-7234A25DD381}'),
		# Method 'ThreadFeatures' returns object of type 'ThreadFeatures'
		"ThreadFeatures": (83887120, 2, (9, 0), (), "ThreadFeatures", '{D0786DD9-AD8A-431B-B2A9-388211ABD7DD}'),
		# Method 'TrimFeatures' returns object of type 'TrimFeatures'
		"TrimFeatures": (83887135, 2, (9, 0), (), "TrimFeatures", '{109C1DF4-2290-44AC-9E90-A108D090B4E9}'),
		"Type": (2130706435, 2, (3, 0), (), "Type", None),
		# Method 'UnwrapFeatures' returns object of type 'UnwrapFeatures'
		"UnwrapFeatures": (83887156, 2, (9, 0), (), "UnwrapFeatures", '{FACF4224-09C8-4856-A2B8-6EAA1BFCB5CA}'),
		# Method 'iFeatures' returns object of type 'iFeatures'
		"iFeatures": (83887139, 2, (9, 0), (), "iFeatures", '{D50258F5-140B-4AE1-BCC7-3CB2438B04E1}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{DA33F1A4-7C3F-11D3-B794-0060B0F159EF}')
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
		return win32com.client.util.Iterator(ob, '{DA33F1A4-7C3F-11D3-B794-0060B0F159EF}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2130706438, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

win32com.client.CLSIDToClass.RegisterCLSID( "{DA33F1A5-7C3F-11D3-B794-0060B0F159EF}", PartFeatures )
