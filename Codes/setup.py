import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Reverse Shell",
      version="0.1",
      description="Python Reverse Shell Demo",
      executables=[Executable("server.py", base=base),Executable("client.py", base=base),Executable("client2.py", base=base) ])

# python setup.py build
