import importlib
import subprocess

def install_lib (pkg):
    try:
        importlib.import_module(pkg)
        print(f"{pkg} is already installed")
    except ImportError:
        subprocess.check_call(["pip", "install", pkg])
        print(f"{pkg} had been installed.")

install_lib("pyperclip")