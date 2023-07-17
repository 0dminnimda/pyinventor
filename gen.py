from wincom import gen_path, wincom
import os
import shutil
from pathlib import Path


def GetDispatchPath(disp: wincom.DispatchBaseClass) -> Path:
    # Get the clsid, lcid, major, and minor for the Dispatch object
    ti = disp._oleobj_.GetTypeInfo()
    disp_clsid = ti.GetTypeAttr()[0]
    tlb, index = ti.GetContainingTypeLib()
    clsid, lcid, _, major, minor, *_ = tlb.GetLibAttr()

    # Get the path of the generated file
    filename = wincom.gencache.GetGeneratedFileName(clsid, lcid, major, minor)
    return Path(gen_path) / filename


# def GenerateToDirectory(name: str, directory: Path) -> wincom.DispatchBaseClass:
#     disp = wincom.gencache.EnsureDispatch(name)
#     source = GetDispatchPath(disp)
#     target = Path(directory) / source.name
#     shutil.move(source, target)
#     return disp


META = "metafile.txt"


def GetStoredMtime(directory: Path) -> float:
    metafile = directory / META
    if metafile.exists():
        return float(metafile.read_text())
    return -1.


def SetStoredMtime(directory: Path, mtime: float) -> None:
    metafile = directory / META
    metafile.write_text(str(mtime))


def DispatchToDirectory(name: str, directory: Path, force: bool = False) -> wincom.DispatchBaseClass:
    disp = wincom.gencache.EnsureDispatch(name)
    source = GetDispatchPath(disp)
    destination = Path(directory)

    mtime = source.stat().st_mtime
    if not force and mtime == GetStoredMtime(destination):
        return disp

    if destination.exists():
        shutil.rmtree(destination)

    shutil.copytree(source, destination)
    SetStoredMtime(destination, mtime)


if __name__ == "__main__":
    directory = Path(__file__).parent / "com"
    DispatchToDirectory("Inventor.Application", directory)


# TODO: find out a reason
# If encountering an issue like this:
"""
Traceback (most recent call last):
  File "D:\Aftodesk\pyinventor\pyinventor\gen.py", line 60, in <module>
    DispatchToDirectory("Inventor.Application", directory)
  File "D:\Aftodesk\pyinventor\pyinventor\gen.py", line 43, in DispatchToDirectory
    disp = wincom.gencache.EnsureDispatch(name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\User\AppData\Roaming\Python\Python311\site-packages\win32com\client\gencache.py", line 628, in EnsureDispatch
    mod = EnsureModule(tla[0], tla[1], tla[3], tla[4], bForDemand=bForDemand)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\User\AppData\Roaming\Python\Python311\site-packages\win32com\client\gencache.py", line 601, in EnsureModule
             ^^^^^^^^^^^^^^^^^^^^^
    makepy.GenerateFromTypeLibSpec(
  File "C:\Users\User\AppData\Roaming\Python\Python311\site-packages\win32com\client\makepy.py", line 338, in GenerateFromTypeLibSpec
    gencache.AddModuleToCache(info.clsid, info.lcid, info.major, info.minor)
  File "C:\Users\User\AppData\Roaming\Python\Python311\site-packages\win32com\client\gencache.py", line 647, in AddModuleToCache
    mod = _GetModule(fname)
          ^^^^^^^^^^^^^^^^^
  File "C:\Users\User\AppData\Roaming\Python\Python311\site-packages\win32com\client\gencache.py", line 726, in _GetModule
    mod = __import__(mod_name)
          ^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'win32com.gen_py.D98A091D-3A0F-4C3E-B36E-61F62068D488x0x1x0'
"""

# Try this:
"""
$ python -m win32com.client.makepy -i "Inventor.Application"
$ python
>>> from win32com.client import gencache
>>> gencache.EnsureModule('{D98A091D-3A0F-4C3E-B36E-61F62068D488}', 0, 1, 0)
"""
