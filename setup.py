import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["xmltodict", "pandas", "PySimpleGUI", "numpy"],
    "includes": ["conversor"],
    "excludes": [],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Para criar um executável sem a janela de console no Windows

setup(
    name="Conversor NFe XML",
    version="1.0",
    description="Converte NF-e XML em planilha Excel",
    options={"build_exe": build_exe_options},
    executables=[Executable("Conversor.py", base=base)]
)
