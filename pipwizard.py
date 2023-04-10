import importlib
import os
import subprocess
subprocess.check_call(["pip", "install", "colorama"])
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

os.system("cls")
print()
print(" " + Fore.BLACK + Back.YELLOW + " PIPWIZARD - Package Manager ")
print(Fore.LIGHTBLACK_EX + " Copyright © 2023 Ashfaaq Rifath - PipWizard v1.3.0")
print('''
 (1) Install package
 (2) Upgrade package
 (3) Uninstall package''')

while True:
    option = input(Fore.CYAN + " Enter option: " + Style.RESET_ALL)
    if option == "1":
        print()
        install_pkg = input(Fore.CYAN + " Enter package name: " + Style.RESET_ALL)

        try:
            importlib.import_module(install_pkg)
            print(" " + Fore.BLACK + Back.GREEN + f" {install_pkg} already installed ")
            print()
            input("Press Enter to exit...")
        except ImportError:
            subprocess.check_call(["pip", "install", install_pkg])
            print(" " + Fore.BLACK + Back.GREEN + f" Installed {install_pkg} ")
            print()
            input("Press Enter to exit...")
        break

    elif option == "2":
        print()
        upgrade_pkg = input(Fore.YELLOW + " Enter package name: " + Style.RESET_ALL)

        try:
            subprocess.check_call(["pip", "install", "--upgrade", upgrade_pkg])
            print(" " + Fore.BLACK + Back.GREEN + f" Upgraded {upgrade_pkg} ")
            print()
            input("Press Enter to exit...")
        except subprocess.CalledProcessError:
            print(" " + Fore.BLACK  + Back.RED + " PACKAGE NOT FOUND ")
            print()
            input("Press Enter to exit...")
        break

    elif option == "3":
        print()
        uninstall_pkg = input(Fore.LIGHTRED_EX + " Enter package name: " + Style.RESET_ALL)

        try:
            subprocess.check_call(["pip", "uninstall", uninstall_pkg])
            print(" " + Fore.BLACK  + Back.RED + f" Uninstalled {uninstall_pkg} ")
            print()
            input("Press Enter to exit...")
        except subprocess.CalledProcessError:
            print(" " + Fore.BLACK  + Back.RED + " PACKAGE NOT FOUND ")
            print()
            input("Press Enter to exit...")
        break
    else:
        print(" " + Fore.BLACK  + Back.RED + " INVALID OPTION ")
        print()
