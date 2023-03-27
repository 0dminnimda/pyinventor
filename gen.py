import win32com
import win32com.client as wincom
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
    return Path(win32com.__gen_path__) / filename


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
