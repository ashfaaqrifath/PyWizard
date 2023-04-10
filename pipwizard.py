import importlib
import os
import subprocess
subprocess.check_call(["pip", "install", "colorama"])
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

os.system("cls")
print()
print(" " + Fore.BLACK + Back.YELLOW + " PIPWIZARD - Package Installer ")
print(Fore.LIGHTBLACK_EX + " Copyright © 2023 Ashfaaq Rifath - PipWizard v1.2.0")
print('''
 (1) Install library
 (2) Upgrade library
 (3) Uninstall library''')
option = input(Fore.CYAN + " Enter option: " + Style.RESET_ALL)

if option == "1":
    print()
    install_lib = input(Fore.CYAN + " Enter library name: " + Style.RESET_ALL)
    try:
        importlib.import_module(install_lib)
        print(" " + Fore.BLACK + Back.GREEN + f" {install_lib} already installed ")
        print()
        input("Press Enter to exit...")
    except ImportError:
        subprocess.check_call(["pip", "install", install_lib])
        print(" " + Fore.BLACK + Back.GREEN + f" {install_lib} has been installed ")
        print()
        input("Press Enter to exit...")

elif option == "2":
    print()
    upgrade_lib = input(Fore.YELLOW + " Enter library name: " + Style.RESET_ALL)

    subprocess.check_call(["pip", "install", "--upgrade", upgrade_lib])
    print(" " + Fore.BLACK + Back.GREEN + f" {upgrade_lib} has been upgraded ")
    print()
    input("Press Enter to exit...")

elif option == "3":
    print()
    uninstall_lib = input(Fore.LIGHTRED_EX + " Enter library name: " + Style.RESET_ALL)

    subprocess.check_call(["pip", "uninstall", uninstall_lib])
    print(" " + Fore.BLACK  + Back.RED + f"{uninstall_lib} has been uninstalled ")
    print()
    input("Press Enter to exit...")
else:
    print(" " + Fore.BLACK  + Back.RED + " INVALID OPTION ")
    print()
    input("Press Enter to exit...")
