import sys
from pathlib import Path


def run_makepy(args: list[str]) -> None:
    from win32com.client import makepy

    old_argv = sys.argv
    try:
        sys.argv = sys.argv[:]
        Path
        sys.argv[1:] = args
        makepy.main()
    finally:
        sys.argv = old_argv


run_makepy(["-o", str(Path(__file__).parent / "com" / "generated.py"), 'Inventor.Application'])


# from win32com.client import gencache
# module = gencache.EnsureDispatch("Inventor.Application")
