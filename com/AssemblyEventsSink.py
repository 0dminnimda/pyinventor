# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Sun Mar 26 15:46:24 2023
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

class AssemblyEventsSink:
	'Outgoing IDispatch-based interface recognized by the Assembly Events Object'
	CLSID = CLSID_Sink = IID('{BABF5BBF-9878-11D4-8DE2-0010B541CAA8}')
	coclass_clsid = IID('{BABF5BC3-9878-11D4-8DE2-0010B541CAA8}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		100667393 : "OnAssemblyChanged",
		100667394 : "OnAssemblySolve",
		100667395 : "OnAssemblyChange",
		100667396 : "OnNewOccurrence",
		100667397 : "OnOccurrenceChange",
		100667398 : "OnNewConstraint",
		100667408 : "OnNewRelationship",
		100667400 : "OnDelete",
		100667401 : "OnLoadStateChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnAssemblyChanged(self, Context=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		'Fires after any change occurs that impacts the Assembly Structure'
#	def OnAssemblySolve(self, Solver=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg):
#		'Fires before and after the assembly solver solves an assembly'
#	def OnAssemblyChange(self, DocumentObject=defaultNamedNotOptArg, Context=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		'Fires when any change occurs that impacts the Assembly Structure'
#	def OnNewOccurrence(self, DocumentObject=defaultNamedNotOptArg, Occurrence=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg
#			, HandlingCode=pythoncom.Missing):
#		'Fires whenever an occurrence is created'
#	def OnOccurrenceChange(self, DocumentObject=defaultNamedNotOptArg, Occurrence=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg
#			, HandlingCode=pythoncom.Missing):
#		'Fires whenever an occurrence changes'
#	def OnNewConstraint(self, DocumentObject=defaultNamedNotOptArg, Constraint=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg
#			, HandlingCode=pythoncom.Missing):
#		'Fires whenever an assembly constraint or iMateResult is created'
#	def OnNewRelationship(self, DocumentObject=defaultNamedNotOptArg, Relationship=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg
#			, HandlingCode=pythoncom.Missing):
#		'Fires whenever an assembly relationship or iMateResult is created'
#	def OnDelete(self, DocumentObject=defaultNamedNotOptArg, Entity=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg
#			, HandlingCode=pythoncom.Missing):
#		'Fires when an Assembly related object is deleted, supplying the context in which this action is being taken'
#	def OnLoadStateChange(self, DocumentObject=defaultNamedNotOptArg, NewLoadState=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg
#			, HandlingCode=pythoncom.Missing):
#		'Fires when an assembly document goes from lite to full or full to lite loading'


win32com.client.CLSIDToClass.RegisterCLSID( "{BABF5BBF-9878-11D4-8DE2-0010B541CAA8}", AssemblyEventsSink )
