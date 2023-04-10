import importlib
import os
import subprocess
import pkgutil

if pkgutil.find_loader("colorama") is None:
    subprocess.check_call(["pip", "install", "colorama"])
else:
    pass
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

os.system("cls")
print()
print(" " + Fore.BLACK + Back.YELLOW + " PIPWIZARD - Package Manager ")
print(Fore.LIGHTBLACK_EX + " Copyright © 2023 Ashfaaq Rifath - PipWizard v1.4.0")
print('''
 (1) Install package
 (2) Batch install
 (3) Update package
 (4) Uninstall package
 (5) Batch uninstall
 (6) Check package status''')

#------------------------------------------------------------------------------------------------
package_list = ["pyperclip", "numpy", "colorama", "pytz"] #Enter packages you need to install
#------------------------------------------------------------------------------------------------

while True:
    option = input(Fore.CYAN + " Enter option: " + Style.RESET_ALL)
    if option == "1":
        print()
        install_pkg = input(Fore.CYAN + " Enter package name: " + Style.RESET_ALL)

        try:
            importlib.import_module(install_pkg)
            print(" " + Fore.BLACK + Back.GREEN + f" {install_pkg} already installed ")
            print()
            input(" Press Enter to exit...")
        except ImportError:
            subprocess.check_call(["pip", "install", install_pkg])
            print(" " + Fore.BLACK + Back.GREEN + f" Installed {install_pkg} ")
            print()
            input(" Press Enter to exit...")
        break

    elif option == "2":
        print()
        print(Fore.YELLOW + " (●) Make sure package list is modified in the source code." + Style.RESET_ALL)
        print(Fore.GREEN + " Batch installing packages..." + Style.RESET_ALL)
        print()

        for pkg in package_list:
            try:
                subprocess.check_call(["pip", "install", pkg])
                print(" " + Fore.BLACK + Back.GREEN + f" Installed {pkg} ")
                print()
            except subprocess.CalledProcessError:
                print(" " + Fore.BLACK  + Back.RED + " PACKAGE NOT FOUND ")
                print()
        input(" Press Enter to exit...")
        break

    elif option == "3":
        print()
        update_pkg = input(Fore.GREEN + " Enter package name: " + Style.RESET_ALL)

        try:
            subprocess.check_call(["pip", "install", "--upgrade", update_pkg])
            print(" " + Fore.BLACK + Back.GREEN + f" Updated {update_pkg} ")
            print()
            input(" Press Enter to exit...")
        except subprocess.CalledProcessError:
            print(" " + Fore.BLACK  + Back.RED + " PACKAGE NOT FOUND ")
            print()
            input(" Press Enter to exit...")
        break

    elif option == "4":
        print()
        uninstall_pkg = input(Fore.LIGHTRED_EX + " Enter package name: " + Style.RESET_ALL)

        try:
            subprocess.check_call(["pip", "uninstall", uninstall_pkg])
            print(" " + Fore.BLACK  + Back.RED + f" Uninstalled {uninstall_pkg} ")
            print()
            input(" Press Enter to exit...")
        except subprocess.CalledProcessError:
            print(" " + Fore.BLACK  + Back.RED + " PACKAGE NOT FOUND ")
            print()
            input(" Press Enter to exit...")
        break

    elif option == "5":
        print()
        print(Fore.YELLOW + " (●) Make sure package list is modified in the source code." + Style.RESET_ALL)
        print(Fore.RED + " Batch uninstalling packages..." + Style.RESET_ALL)
        print()

        for pkg in package_list:
            try:
                subprocess.check_call(["pip", "uninstall", pkg])
                print(" " + Fore.BLACK + Back.RED + f" Uninstalled {pkg} ")
                print()
            except subprocess.CalledProcessError:
                print(" " + Fore.BLACK  + Back.RED + " PACKAGE NOT FOUND ")
                print()
        input(" Press Enter to exit...")
        break

    elif option == "6":
        print()
        verify_pkg = input(Fore.YELLOW + " Enter package name: " + Style.RESET_ALL)

        try:
            subprocess.check_call(["pip", "show", verify_pkg])
            print(" " + Fore.BLACK  + Back.GREEN + f" {verify_pkg} package exists ")
            print()
            input(" Press Enter to exit...")
        except subprocess.CalledProcessError:
            print(" " + Fore.BLACK  + Back.RED + " PACKAGE NOT FOUND ")
            print()
            input(" Press Enter to exit...")
        break
    else:
        print(" " + Fore.BLACK  + Back.RED + " INVALID OPTION ")
        print()
