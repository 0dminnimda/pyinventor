# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 14:38:12 2023
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
class FileManager(DispatchBaseClass):
	'File Manager Object'
	CLSID = IID('{B00506C6-BEB7-47F6-8B1B-A5CB5DCD09B3}')
	coclass_clsid = None

	def CanCADFileBeAssociativelyImported(self, FullFileName=defaultNamedNotOptArg):
		'Method that checks whether a foreign CAD file can be associatively imported into Inventor document or not.'
		return self._oleobj_.InvokeTypes(50378267, LCID, 1, (11, 0), ((8, 1),),FullFileName
			)

	def CopyFile(self, SourceFullFileName=defaultNamedNotOptArg, DestinationFullFileName=defaultNamedNotOptArg, FileManagementOption=0):
		'Copies the file from one location to another'
		return self._oleobj_.InvokeTypes(50378242, LCID, 1, (24, 0), ((8, 1), (8, 1), (3, 49)),SourceFullFileName
			, DestinationFullFileName, FileManagementOption)

	def DeleteFile(self, FullFileName=defaultNamedNotOptArg, FileManagementOption=0):
		'Deletes the file'
		return self._oleobj_.InvokeTypes(50378241, LCID, 1, (24, 0), ((8, 1), (3, 49)),FullFileName
			, FileManagementOption)

	def GetAutoCADBlockDefinitions(self, FullFileName=defaultNamedNotOptArg):
		'Returns the names of all the AutoCAD block definitions contained within the input DWG file'
		return self._ApplyTypes_(50378263, 1, (8200, 0), ((8, 1),), 'GetAutoCADBlockDefinitions', None,FullFileName
			)

	def GetCADFileStructure(self, FullFileName=defaultNamedNotOptArg, ResultXML=defaultNamedNotOptArg):
		'Method that gets the CAD file references structure and saves the result in a XML file. This will raise an error if there is no proper Inventor Compatibility Pack installed.'
		return self._oleobj_.InvokeTypes(50378270, LCID, 1, (24, 0), ((8, 1), (8, 1)),FullFileName
			, ResultXML)

	def GetDWGDocumentReferences(self, DocumentOrFileName=defaultNamedNotOptArg):
		'Gets the set of direct file references from a DWG file'
		return self._ApplyTypes_(50378256, 1, (8200, 0), ((12, 1),), 'GetDWGDocumentReferences', None,DocumentOrFileName
			)

	def GetDesignViewRepresentations(self, FullFileName=defaultNamedNotOptArg):
		'Returns the names of all the design view representations contained within the input file (*.iam, *.ipt or *.idv)'
		return self._ApplyTypes_(50378252, 1, (8200, 0), ((8, 1),), 'GetDesignViewRepresentations', None,FullFileName
			)

	def GetEmbeddedDocumentShortName(self, FullFileName=defaultNamedNotOptArg):
		'Method that returns the short filename of an embedded document path.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(50378272, LCID, 1, (8, 0), ((8, 1),),FullFileName
			)

	def GetExpressGraphicsStatus(self, AssemblyFullFilename=defaultNamedNotOptArg):
		'Returns a value indicating the current state of the express graphics in the specified assembly.'
		return self._oleobj_.InvokeTypes(50378264, LCID, 1, (3, 0), ((8, 1),),AssemblyFullFilename
			)

	def GetFileNameFromIdentifier(self, Identifier=defaultNamedNotOptArg, FullFileName=pythoncom.Missing, AbsolutePath=''):
		'Returns the fully qualified name of a file using its unique identifier. The identifier must have been obtained from the GetIdentifierFromFileName method'
		return self._ApplyTypes_(50378246, 1, (24, 32), ((24593, 3), (16392, 2), (8, 49)), 'GetFileNameFromIdentifier', None,Identifier
			, FullFileName, AbsolutePath)

	def GetFullDocumentName(self, FullFileName=defaultNamedNotOptArg, LevelOfDetailName=''):
		'Method that returns the full document name which is a unique identifier for an open Document.  The returned string is the full file name concatenated with the document name'
		return self._ApplyTypes_(50378249, 1, (8, 32), ((8, 1), (8, 49)), 'GetFullDocumentName', None,FullFileName
			, LevelOfDetailName)

	def GetFullFileName(self, FullDocumentName=defaultNamedNotOptArg):
		'Method that returns the full file name given its full document name'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(50378251, LCID, 1, (8, 0), ((8, 1),),FullDocumentName
			)

	def GetIdentifierFromFileName(self, FullFileName=defaultNamedNotOptArg, Identifier=defaultNamedNotOptArg, AbsolutePath=''):
		'Creates and returns a unique, persistent identifier for the specified file'
		return self._ApplyTypes_(50378245, 1, (24, 32), ((8, 1), (24593, 3), (8, 49)), 'GetIdentifierFromFileName', None,FullFileName
			, Identifier, AbsolutePath)

	def GetLastActiveDesignViewRepresentation(self, FullFileName=defaultNamedNotOptArg):
		'Returns the name of the design view representation that was active when the file was last saved'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(50378261, LCID, 1, (8, 0), ((8, 1),),FullFileName
			)

	def GetLastActiveLevelOfDetailRepresentation(self, FullFileName=defaultNamedNotOptArg):
		'Returns the name of the Level of Detail representation that was last saved with the assembly file'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(50378259, LCID, 1, (8, 0), ((8, 1),),FullFileName
			)

	def GetLevelOfDetailName(self, FullDocumentName=defaultNamedNotOptArg):
		'Method that returns the name of the document given its full document name'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(50378250, LCID, 1, (8, 0), ((8, 1),),FullDocumentName
			)

	def GetLevelOfDetailRepresentations(self, FullFileName=defaultNamedNotOptArg):
		'Returns the names of all the level of detail representations contained within the input file'
		return self._ApplyTypes_(50378254, 1, (8200, 0), ((8, 1),), 'GetLevelOfDetailRepresentations', None,FullFileName
			)

	def GetPositionalRepresentations(self, FullFileName=defaultNamedNotOptArg):
		'Returns the names of all the positional representations contained within the input assembly file'
		return self._ApplyTypes_(50378253, 1, (8200, 0), ((8, 1),), 'GetPositionalRepresentations', None,FullFileName
			)

	def GetSHXFontList(self, BigFont=defaultNamedOptArg):
		'Method that gets the array of strings containing the SHX font name list.'
		return self._ApplyTypes_(50378273, 1, (8200, 0), ((12, 17),), 'GetSHXFontList', None,BigFont
			)

	def GetTemplateFile(self, DocumentType=defaultNamedNotOptArg, SystemOfMeasure=8961, DraftingStandard=9729, DocumentSubType=defaultNamedOptArg):
		'Gets template file'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(50378244, LCID, 1, (8, 0), ((3, 1), (3, 49), (3, 49), (12, 17)),DocumentType
			, SystemOfMeasure, DraftingStandard, DocumentSubType)

	def IsEmbeddedDocumentPath(self, FullFileName=defaultNamedNotOptArg):
		'Method that returns whether the input string indicates an embedded document path.'
		return self._oleobj_.InvokeTypes(50378271, LCID, 1, (11, 0), ((8, 1),),FullFileName
			)

	def IsFileNameValid(self, FileName=defaultNamedNotOptArg, ValidFileName=pythoncom.Missing):
		'Validate the input filename and replace illegal filename characters with something more appropriate'
		return self._ApplyTypes_(50378255, 1, (11, 0), ((8, 1), (16392, 2)), 'IsFileNameValid', None,FileName
			, ValidFileName)

	def IsFutureCADFile(self, FullFileName=defaultNamedNotOptArg):
		'Method that returns whether the input CAD file is a future CAD file that current Inventor version can’t open/translate. If an invalid CAD filename is provided an error would occur.'
		return self._oleobj_.InvokeTypes(50378269, LCID, 1, (11, 0), ((8, 1),),FullFileName
			)

	def IsInventorComponent(self, FullFileName=defaultNamedNotOptArg):
		'Returns whether the input file is an Inventor Component (part or assembly).'
		return self._oleobj_.InvokeTypes(50378268, LCID, 1, (11, 0), ((8, 1),),FullFileName
			)

	def IsInventorDWG(self, FullFileName=defaultNamedNotOptArg):
		'Returns whether the input file is an Inventor DWG file'
		return self._oleobj_.InvokeTypes(50378257, LCID, 1, (11, 0), ((8, 1),),FullFileName
			)

	def MoveFile(self, SourceFullFileName=defaultNamedNotOptArg, DestinationFullFileName=defaultNamedNotOptArg, FileManagementOption=0):
		'Moves the file from one location to another'
		return self._oleobj_.InvokeTypes(50378243, LCID, 1, (24, 0), ((8, 1), (8, 1), (3, 49)),SourceFullFileName
			, DestinationFullFileName, FileManagementOption)

	def ReferencedDocumentCount(self, FullFileName=defaultNamedNotOptArg):
		'Returns the number of uniquely referenced documents the input document had at the time it was last saved. This is the number that is used in determining whether or not an assembly will open in Express mode or Full mode.'
		return self._oleobj_.InvokeTypes(50378265, LCID, 1, (3, 0), ((8, 1),),FullFileName
			)

	def RefreshAllDocuments(self):
		'Refreshes all documents in memory to the latest version on disk'
		return self._oleobj_.InvokeTypes(50378260, LCID, 1, (24, 0), (),)

	# Result is of type SoftwareVersion
	def SoftwareVersionSaved(self, FullFileName=defaultNamedNotOptArg):
		'Returns the object that encapsulates the version of the software with which this file was last saved'
		ret = self._oleobj_.InvokeTypes(50378262, LCID, 1, (9, 0), ((8, 1),),FullFileName
			)
		if ret is not None:
			ret = Dispatch(ret, 'SoftwareVersionSaved', '{076C16D1-4994-11D4-9E0F-0010A4C72F07}')
		return ret

	def WillOpenExpressDefault(self, FullFileName=defaultNamedNotOptArg):
		'Returns whether the input assembly will open in Express mode by default.'
		return self._oleobj_.InvokeTypes(50378266, LCID, 1, (11, 0), ((8, 1),),FullFileName
			)

	_prop_map_get_ = {
		"Application": (2130706433, 2, (9, 0), (), "Application", None),
		# Method 'FileManagerEvents' returns object of type 'FileManagerEvents'
		"FileManagerEvents": (50378247, 2, (13, 0), (), "FileManagerEvents", '{A44AF926-6383-42F0-8B2D-253F82F95ABE}'),
		"FileSystemObject": (50378258, 2, (9, 0), (), "FileSystemObject", None),
		# Method 'Files' returns object of type 'FilesEnumerator'
		"Files": (50378248, 2, (9, 0), (), "Files", '{4771DB69-A789-4BA4-A35C-56BFCC6AECFA}'),
		"Type": (0, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
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

win32com.client.CLSIDToClass.RegisterCLSID( "{B00506C6-BEB7-47F6-8B1B-A5CB5DCD09B3}", FileManager )
