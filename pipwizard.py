import importlib
import subprocess

print('''
(1) Install library
(2) Upgrade library
(3) Uninstall library''')
option = input("Enter opton: ")

if option == "1":
    print()
    install_lib = input("Enter library name: ")

    try:
        importlib.import_module(install_lib)
        print(f"{install_lib} is already installed")
    except ImportError:
        subprocess.check_call(["pip", "install", install_lib])
        print(f"{install_lib} had been installed.")

elif option == "2":
    upgrade_lib = input("Enter library name: ")

    subprocess.check_call(["pip", "install", "--upgrade", upgrade_lib])
    print(f"{upgrade_lib} has been upgraded.")

elif option == "3":
    uninstall_lib = input("Enter library name: ")

    subprocess.check_call(["pip", "uninstall", uninstall_lib])
    print(f"{uninstall_lib} had been uninstalled.")
