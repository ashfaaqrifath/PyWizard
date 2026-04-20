import os
import sys
import subprocess
import importlib
import pkgutil
import importlib
from questionary import Style, select

if importlib.util.find_spec("colorama") is None:
    subprocess.check_call(["pip", "install", "colorama"])
    #installs colorama automatically
else:
    pass

import colorama
from colorama import Fore, Back, Style as ColorStyle
colorama.init(autoreset=True)


os.system("cls")

title = ('''
 █▀▀█ █   █ █   █ ▀█▀ █▀▀▀█ █▀▀█ █▀▀█ █▀▀▄ 
 █▄▄█ █▄▄▄█ █ █ █  █  ▄▄▄▀▀ █▄▄█ █▄▄▀ █  █ 
 █      █   █▄▀▄█ ▄█▄ █▄▄▄█ █  █ █  █ █▄▄▀ v1.5.5''')
print(title)
print(Fore.YELLOW + "          PYTHON PACKAGE MANAGER")
print()

menu_styles = Style([
    ("pointer", "fg:#00FF00"),      
    ("selected", "fg:#00FF00"),     
    ("highlighted", "fg:#00FF00 bold"),
    ("answer", "fg:#c19c00"),
])


while True:
    print()

    option = select(
        "Select option:",
        choices=["(1) Install package", 
                "(2) Batch install", 
                "(3) Update package",
                "(4) Uninstall package",
                "(5) Batch uninstall",
                "(6) Check package status",
                "(7) Display installed packages",
                "(8) Save requirements file",
                "(9) Upgrade PIP version",
                "(10) Check PIP version",
                "(11) Check Python version",
                "(12) Create executable",
                "(13) Clear terminal"],
        qmark="",
        style=menu_styles
    ).ask()
    
    # Extract number from the option string
    option = option[option.index("(")+1:option.index(")")]
    
    if option == "1":
        print()
        install_pkg = input(Fore.CYAN + " Enter package name: " + ColorStyle.RESET_ALL)

        try:
            subprocess.check_call(["pip", "install", install_pkg])
            print(" " + Fore.BLACK + Back.GREEN + f" Installed {install_pkg} ")
            print()
        except subprocess.CalledProcessError:
            print(" " + Fore.BLACK  + Back.RED + " PACKAGE NOT FOUND ")
            print()

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
                    print()
        else:
            print(" " + Fore.BLACK  + Back.RED + " REQUIREMENTS FILE DOES NOT EXIST ")
            print()

    elif option == "3":
        print()
        update_pkg = input(Fore.GREEN + " Enter package name: " + ColorStyle.RESET_ALL)

        try:
            subprocess.check_call(["pip", "install", "--upgrade", update_pkg])
            print(" " + Fore.BLACK + Back.GREEN + f" Updated {update_pkg} ")
            print()
        except subprocess.CalledProcessError:
            print(" " + Fore.BLACK  + Back.RED + " PACKAGE NOT FOUND ")
            print()

    elif option == "4":
        print()
        uninstall_pkg = input(Fore.LIGHTRED_EX + " Enter package name: " + ColorStyle.RESET_ALL)

        try:
            subprocess.check_call(["pip", "uninstall", uninstall_pkg])
            print(" " + Fore.BLACK  + Back.RED + f" Uninstalled {uninstall_pkg} ")
            print()
        except subprocess.CalledProcessError:
            print(" " + Fore.BLACK  + Back.RED + " PACKAGE NOT FOUND ")
            print()

    elif option == "5":
        confirm = input(Fore.LIGHTRED_EX + " Do you want to proceed? (y/n): ")
        if confirm == "y".lower():
            print()
            print(Fore.YELLOW + " NOTE: Input package names in the requirements file." + ColorStyle.RESET_ALL)
            if os.path.isfile("requirements.txt"):
                print(Fore.RED + " Batch uninstalling packages..." + ColorStyle.RESET_ALL)
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
                print()
        else:
            print(" " + Fore.BLACK  + Back.RED + " UNINSTALL CANCELLED ")
            print()

    elif option == "6":
        print()
        verify_pkg = input(Fore.CYAN + " Enter package name: " + ColorStyle.RESET_ALL)

        try:
            subprocess.check_call(["pip", "show", verify_pkg])
            print(" " + Fore.BLACK  + Back.GREEN + f" {verify_pkg} package exists ")
            print()
        except subprocess.CalledProcessError:
            print(" " + Fore.BLACK  + Back.RED + " PACKAGE NOT FOUND ")
            print()

    elif option == "7":
        print()
        print(Fore.GREEN + " Displaying all installed packages...")
        subprocess.check_call(["pip", "list"])
        print()
        
    elif option == "8":
        print()
        print(Fore.YELLOW + " NOTE: Run this tool from the desired project folder.")
        print(Fore.GREEN + " Saving project requirements to text file...")

        try:
            save = subprocess.run(["pip", "freeze"], stdout=subprocess.PIPE)
            with open('requirements.txt', 'wb') as f:
                f.write(save.stdout)
            print(" " + Fore.BLACK  + Back.GREEN + " PROJECT REQUIREMENTS SAVED ")
            print()
        except subprocess.CalledProcessError:
            print(" " + Fore.BLACK  + Back.RED + " ERROR OCCURRED ")
            print()

    elif option == "9":
        print()
        print(Fore.GREEN + " Upgrading to new PIP version...")

        try:
            subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pip"])
            print(" " + Fore.BLACK  + Back.GREEN + " PIP version upgrade successful ")
            print()
        except subprocess.CalledProcessError:
            print(" " + Fore.BLACK  + Back.RED + " ERROR OCCURRED ")
            print()

    elif option == "10":
        print()
        print(Fore.GREEN + " Displaying PIP version")
        subprocess.run(["pip", "--version"])
        print()

    elif option == "11":
        print()
        print(Fore.GREEN + " Displaying Python version")
        subprocess.run(["python", "--version"])
        print()

    elif option == "12":
        if importlib.util.find_spec("pyinstaller") is None:
            subprocess.check_call(["pip", "install", "pyinstaller"])
        #installs pyinstaller automatically
        else:
            pass

        print()
        file_name = input(Fore.CYAN + " Enter Python file name (.py): " + ColorStyle.RESET_ALL)

        if os.path.isfile(file_name):
            icon_option = input(Fore.YELLOW + " Do you want an icon for this file? (y/n): " + ColorStyle.RESET_ALL)

            if icon_option == "y".lower():
                icon_name = input(Fore.CYAN + " Enter ICO file name (.ico): " + ColorStyle.RESET_ALL)

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
            print()

    elif option == "13":
        #clears terminal
        os.system("cls")
        print(title)
        print(Fore.YELLOW + "          PYTHON PACKAGE MANAGER")
        print()
