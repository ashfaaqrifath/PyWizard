import os
import sys
import subprocess
import importlib
import pkgutil

if pkgutil.find_loader("colorama") is None:
    subprocess.check_call(["pip", "install", "colorama"])
    #installs colorama automatically
else:
    pass
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#clears terminal
os.system("cls")
print('''
 █▀▀█ █   █ █   █ ▀█▀ █▀▀▀█ █▀▀█ █▀▀█ █▀▀▄ 
 █▄▄█ █▄▄▄█ █ █ █  █  ▄▄▄▀▀ █▄▄█ █▄▄▀ █  █ 
 █      █   █▄▀▄█ ▄█▄ █▄▄▄█ █  █ █  █ █▄▄▀ v1.5.4''')
print(Fore.YELLOW + "          PYTHON PACKAGE MANAGER")
print()
print(Fore.LIGHTBLACK_EX + "        Copyright © Ashfaaq Rifath")

print('''
 (1) Install package
 (2) Batch install from requirements file
 (3) Update package
 (4) Uninstall package
 (5) Batch uninstall from requirements file
 (6) Check package status
 (7) Display installed packages
 (8) Save requirements file
 (9) Upgrade PIP version
 (10) Check PIP version
 (11) Check Python version
 (12) Create EXE for Python file''')

while True:
    print()
    option = input(Fore.CYAN + " Select option: " + Style.RESET_ALL)
    if option == "1":
        print()
        install_pkg = input(Fore.CYAN + " Enter package name: " + Style.RESET_ALL)

        try:
            subprocess.check_call(["pip", "install", install_pkg])
            print(" " + Fore.BLACK + Back.GREEN + f" Installed {install_pkg} ")
        except subprocess.CalledProcessError:
            print(" " + Fore.BLACK  + Back.RED + " PACKAGE NOT FOUND ")

    elif option == "2":
        print()
        print(Fore.YELLOW + " NOTE: Make sure requirements.txt is in the root directory.")
        if os.path.isfile("requirements.txt"):
            print(Fore.GREEN + " Batch installing packages...")

            with open("requirements.txt") as f:
                reqs = f.read().splitlines()
            for pkg in reqs:
                try:
                    subprocess.check_call(["pip", "install", pkg])
                    print(" " + Fore.BLACK + Back.GREEN + f" Installed {pkg} ")
                    print()
                except subprocess.CalledProcessError:
                    print(" " + Fore.BLACK  + Back.RED + " ERROR OCCURRED ")
        else:
            print(" " + Fore.BLACK  + Back.RED + " REQUIREMENTS FILE DOES NOT EXIST ")

    elif option == "3":
        print()
        update_pkg = input(Fore.GREEN + " Enter package name: " + Style.RESET_ALL)

        try:
            subprocess.check_call(["pip", "install", "--upgrade", update_pkg])
            print(" " + Fore.BLACK + Back.GREEN + f" Updated {update_pkg} ")
        except subprocess.CalledProcessError:
            print(" " + Fore.BLACK  + Back.RED + " PACKAGE NOT FOUND ")

    elif option == "4":
        print()
        uninstall_pkg = input(Fore.LIGHTRED_EX + " Enter package name: " + Style.RESET_ALL)

        try:
            subprocess.check_call(["pip", "uninstall", uninstall_pkg])
            print(" " + Fore.BLACK  + Back.RED + f" Uninstalled {uninstall_pkg} ")
        except subprocess.CalledProcessError:
            print(" " + Fore.BLACK  + Back.RED + " PACKAGE NOT FOUND ")

    elif option == "5":
        confirm = input(Fore.LIGHTRED_EX + " Do you want to proceed? (y/n): ")
        if confirm == "y".lower():
            print()
            print(Fore.YELLOW + " NOTE: Input package names in the requirements file." + Style.RESET_ALL)
            if os.path.isfile("requirements.txt"):
                print(Fore.RED + " Batch uninstalling packages..." + Style.RESET_ALL)
                print()

                with open("requirements.txt") as f:
                    reqs = f.read().splitlines()
                for pkg in reqs:
                    try:
                        subprocess.check_call(["pip", "uninstall", "-y", pkg])
                        print(" " + Fore.BLACK + Back.RED + f" Uninstalled {pkg} ")
                    except subprocess.CalledProcessError:
                        print(" " + Fore.BLACK  + Back.RED + " PACKAGE NOT FOUND ")
            else:
                print(" " + Fore.BLACK  + Back.RED + " REQUIREMENTS FILE DOES NOT EXIST ")
        else:
            print(" " + Fore.BLACK  + Back.RED + " UNINSTALL CANCELLED ")

    elif option == "6":
        print()
        verify_pkg = input(Fore.CYAN + " Enter package name: " + Style.RESET_ALL)

        try:
            subprocess.check_call(["pip", "show", verify_pkg])
            print(" " + Fore.BLACK  + Back.GREEN + f" {verify_pkg} package exists ")
        except subprocess.CalledProcessError:
            print(" " + Fore.BLACK  + Back.RED + " PACKAGE NOT FOUND ")

    elif option == "7":
        print()
        print(Fore.GREEN + " Displaying all installed packages...")
        subprocess.check_call(["pip", "list"])
        
    elif option == "8":
        print()
        print(Fore.YELLOW + " NOTE: Run this tool from the desired project folder.")
        print(Fore.GREEN + " Saving project requirements to text file...")

        try:
            save = subprocess.run(["pip", "freeze"], stdout=subprocess.PIPE)
            with open('requirements.txt', 'wb') as f:
                f.write(save.stdout)
            print(" " + Fore.BLACK  + Back.GREEN + " PROJECT REQUIREMENTS SAVED ")
        except subprocess.CalledProcessError:
            print(" " + Fore.BLACK  + Back.RED + " ERROR OCCURRED ")

    elif option == "9":
        print()
        print(Fore.GREEN + " Upgrading to new PIP version...")

        try:
            subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pip"])
            print(" " + Fore.BLACK  + Back.GREEN + " PIP version upgrade successful ")
        except subprocess.CalledProcessError:
            print(" " + Fore.BLACK  + Back.RED + " ERROR OCCURRED ")

    elif option == "10":
        print()
        print(Fore.GREEN + " Displaying PIP version")
        subprocess.run(["pip", "--version"])

    elif option == "11":
        print()
        print(Fore.GREEN + " Displaying Python version")
        subprocess.run(["python", "--version"])

    elif option == "12":
        if pkgutil.find_loader("pyinstaller") is None:
            subprocess.check_call(["pip", "install", "pyinstaller"])
        #installs pyinstaller automatically
        else:
            pass

        print()
        file_name = input(Fore.CYAN + " Enter Python file name (.py): " + Style.RESET_ALL)

        if os.path.isfile(file_name):
            icon_option = input(Fore.YELLOW + " Do you want an icon for this file? (y/n): " + Style.RESET_ALL)

            if icon_option == "y".lower():
                icon_name = input(Fore.CYAN + " Enter ICO file name (.ico): " + Style.RESET_ALL)

                if os.path.isfile(icon_name):
                    print()
                    print(Fore.YELLOW + " NOTE: Run this tool from the desired project folder.")
                    print(Fore.GREEN + f" Creating EXE file for {file_name}...")

                    try:
                        subprocess.run(["pyinstaller", "--onefile", f"--icon={icon_name}", file_name])
                        print(" " + Fore.BLACK  + Back.GREEN + f" Created EXE file for {file_name} ")
                    except subprocess.CalledProcessError:
                        print(" " + Fore.BLACK  + Back.RED + " ERROR OCCURRED ")
                else:
                    print(" " + Fore.BLACK  + Back.RED + " FILE DOES NOT EXIST ")

            if icon_option == "n".lower():
                print()
                print(Fore.YELLOW + " NOTE: Run this tool from the desired project folder.")
                print(Fore.GREEN + f" Creating EXE file for {file_name}...")

                try:
                    subprocess.run(["pyinstaller", "--onefile", file_name])
                    print(" " + Fore.BLACK  + Back.GREEN + f" Created EXE file for {file_name} ")
                except subprocess.CalledProcessError:
                    print(" " + Fore.BLACK  + Back.RED + " ERROR OCCURRED ")
        else:
            print(" " + Fore.BLACK  + Back.RED + " FILE DOES NOT EXIST ")

    elif option == "help":
        print('''
 (1) Install package
 (2) Batch install from requirements file
 (3) Update package
 (4) Uninstall package
 (5) Batch uninstall from requirements file
 (6) Check package status
 (7) Display installed packages
 (8) Save requirements file
 (9) Upgrade PIP version
 (10) Check PIP version
 (11) Check Python version
 (12) Create EXE for Python file''')

    else:
        print(" " + Fore.BLACK  + Back.RED + " INVALID OPTION ")



# Copyright © 2023 Ashfaaq Rifath - PyWizard v1.5.4