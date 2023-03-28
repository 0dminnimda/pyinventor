import win32com
import win32com.client as wincom


def set_genpath(path: str):
    win32com.__gen_path__ = str(path)


set_genpath("com")

gen_path = win32com.__gen_path__
