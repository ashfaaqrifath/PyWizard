import os
import sys
import json
import subprocess
import importlib.util

import colorama
from colorama import Fore, Back, Style as ColorStyle
from questionary import Style, select


colorama.init(autoreset=True)


# -------------------------------
# Basic setup
# -------------------------------
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def run_command(command, success_message=None, error_message="ERROR OCCURRED"):
    try:
        subprocess.check_call(command)

        if success_message:
            print(" " + Fore.BLACK + Back.GREEN + f" {success_message} ")

        print()

    except subprocess.CalledProcessError:
        print(" " + Fore.BLACK + Back.RED + f" {error_message} ")
        print()


def get_requirements_file():
    file_name = input(Fore.CYAN + " Enter requirements file name: " + ColorStyle.RESET_ALL).strip()

    if file_name == "":
        file_name = "requirements.txt"

    return file_name


def print_title():
    title = ('''
 █▀▀█ █   █ █▀▀▄ █▀▀▀ █▀▀█ █▀▄▀█ █▀▀▀ █▀▀█
 █▄▄█ █▄▄▄█ █  █ █▀▀▀ █▄▄█ █ █ █ █ ▀█ █▄▄▀
 █      █   █▄▄▀ █▄▄▄ █    █   █ █▄▄█ █  █ v1.6.0''')

    print(title)
    print(Fore.YELLOW + "          PYTHON DEPENDENCY MANAGER")
    print()


def install_pyinstaller_if_missing():
    if importlib.util.find_spec("PyInstaller") is None:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])


def main():
    clear_terminal()
    print_title()

    menu_styles = Style([
        ("pointer", "fg:#00FF00"),
        ("selected", "fg:#00FF00"),
        ("highlighted", "fg:#00FF00 bold"),
        ("answer", "fg:#c19c00"),
    ])

    # -------------------------------
    # Main menu loop
    # -------------------------------
    while True:
        print()

        option = select(
            "Select option:",
            choices=[
                "(1) Install package",
                "(2) Update package",
                "(3) Uninstall package",
                "(4) Batch install dependencies",
                "(5) Batch uninstall packages",

                "(6) Search installed package",
                "(7) List all installed packages",
                "(8) List all outdated packages",
                "(9) Update all outdated packages",
                "(10) Check broken dependencies",

                "(11) Save requirements file",
                "(12) Upgrade PIP version",
                "(13) Check PIP version",
                "(14) Check Python version",
                "(15) Clear PIP cache",

                "(16) Create virtual environment",
                "(17) Create executable",

                "(18) Clear terminal",
                "(19) Exit"
            ],
            qmark="",
            style=menu_styles
        ).ask()

        if option is None:
            print()
            print(Fore.RED + " Exiting...")
            break

        option = option[option.index("(") + 1:option.index(")")]

        # -------------------------------
        # 1. Install package
        # -------------------------------
        if option == "1":
            print()
            install_pkg = input(Fore.CYAN + " Enter package name: " + ColorStyle.RESET_ALL).strip()

            if install_pkg:
                run_command(
                    [sys.executable, "-m", "pip", "install", install_pkg],
                    f"Installed {install_pkg}",
                    "PACKAGE NOT FOUND"
                )
            else:
                print(" " + Fore.BLACK + Back.RED + " PACKAGE NAME CANNOT BE EMPTY ")
                print()

        # -------------------------------
        # 2. Update package
        # -------------------------------
        elif option == "2":
            print()
            update_pkg = input(Fore.GREEN + " Enter package name: " + ColorStyle.RESET_ALL).strip()

            if update_pkg:
                run_command(
                    [sys.executable, "-m", "pip", "install", "--upgrade", update_pkg],
                    f"Updated {update_pkg}",
                    "PACKAGE NOT FOUND"
                )
            else:
                print(" " + Fore.BLACK + Back.RED + " PACKAGE NAME CANNOT BE EMPTY ")
                print()

        # -------------------------------
        # 3. Uninstall package
        # -------------------------------
        elif option == "3":
            print()
            uninstall_pkg = input(Fore.LIGHTRED_EX + " Enter package name: " + ColorStyle.RESET_ALL).strip()

            if uninstall_pkg:
                confirm = input(Fore.LIGHTRED_EX + f" Uninstall {uninstall_pkg}? (y/n): " + ColorStyle.RESET_ALL).lower()

                if confirm == "y":
                    run_command(
                        [sys.executable, "-m", "pip", "uninstall", "-y", uninstall_pkg],
                        f"Uninstalled {uninstall_pkg}",
                        "PACKAGE NOT FOUND"
                    )
                else:
                    print(" " + Fore.BLACK + Back.RED + " UNINSTALL CANCELLED ")
                    print()
            else:
                print(" " + Fore.BLACK + Back.RED + " PACKAGE NAME CANNOT BE EMPTY ")
                print()

        # -------------------------------
        # 4. Batch install
        # -------------------------------
        elif option == "4":
            print()
            print(Fore.YELLOW + " NOTE: Make sure the requirements file is in the root directory.")
            req_file = get_requirements_file()

            if os.path.isfile(req_file):
                print(Fore.GREEN + " Batch installing packages...")

                with open(req_file, "r", encoding="utf-8") as f:
                    reqs = f.read().splitlines()

                for pkg in reqs:
                    pkg = pkg.strip()

                    if pkg and not pkg.startswith("#"):
                        try:
                            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
                            print(" " + Fore.BLACK + Back.GREEN + f" Installed {pkg} ")
                            print()

                        except subprocess.CalledProcessError:
                            print(" " + Fore.BLACK + Back.RED + f" Failed to install {pkg} ")
                            print()
            else:
                print(" " + Fore.BLACK + Back.RED + " REQUIREMENTS FILE DOES NOT EXIST ")
                print()

        # -------------------------------
        # 5. Batch uninstall
        # -------------------------------
        elif option == "5":
            print()
            confirm = input(Fore.LIGHTRED_EX + " Do you want to proceed? (y/n): " + ColorStyle.RESET_ALL).lower()

            if confirm == "y":
                print()
                print(Fore.YELLOW + " NOTE: Input package names in the requirements file.")
                req_file = get_requirements_file()

                if os.path.isfile(req_file):
                    print(Fore.RED + " Batch uninstalling packages...")
                    print()

                    with open(req_file, "r", encoding="utf-8") as f:
                        reqs = f.read().splitlines()

                    for pkg in reqs:
                        pkg = pkg.strip()

                        if pkg and not pkg.startswith("#"):
                            try:
                                subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", pkg])
                                print(" " + Fore.BLACK + Back.RED + f" Uninstalled {pkg} ")

                            except subprocess.CalledProcessError:
                                print(" " + Fore.BLACK + Back.RED + f" Failed to uninstall {pkg} ")
                else:
                    print(" " + Fore.BLACK + Back.RED + " REQUIREMENTS FILE DOES NOT EXIST ")
                    print()
            else:
                print(" " + Fore.BLACK + Back.RED + " UNINSTALL CANCELLED ")
                print()

        # -------------------------------
        # 6. Search installed package
        # -------------------------------
        elif option == "6":
            print()
            verify_pkg = input(Fore.CYAN + " Enter package name: " + ColorStyle.RESET_ALL).strip()

            if verify_pkg:
                run_command(
                    [sys.executable, "-m", "pip", "show", verify_pkg],
                    f"{verify_pkg} package exists",
                    "PACKAGE NOT FOUND"
                )
            else:
                print(" " + Fore.BLACK + Back.RED + " PACKAGE NAME CANNOT BE EMPTY ")
                print()

        # -------------------------------
        # 7. Display installed packages
        # -------------------------------
        elif option == "7":
            print()
            print(Fore.GREEN + " Displaying all installed packages...")
            subprocess.run([sys.executable, "-m", "pip", "list"])
            print()

        # -------------------------------
        # 8. Display outdated packages
        # -------------------------------
        elif option == "8":
            print()
            print(Fore.GREEN + " Displaying outdated packages...")
            subprocess.run([sys.executable, "-m", "pip", "list", "--outdated"])
            print()

        # -------------------------------
        # 9. Update all outdated packages
        # -------------------------------
        elif option == "9":
            print()
            confirm = input(Fore.YELLOW + " Update all outdated packages? This may affect projects. (y/n): " + ColorStyle.RESET_ALL).lower()

            if confirm == "y":
                print(Fore.GREEN + " Checking outdated packages...")

                try:
                    result = subprocess.run(
                        [sys.executable, "-m", "pip", "list", "--outdated", "--format=json"],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True
                    )

                    outdated_packages = json.loads(result.stdout)

                    if len(outdated_packages) == 0:
                        print(" " + Fore.BLACK + Back.GREEN + " ALL PACKAGES ARE UP TO DATE ")
                        print()
                    else:
                        for package in outdated_packages:
                            pkg = package["name"]

                            try:
                                subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", pkg])
                                print(" " + Fore.BLACK + Back.GREEN + f" Updated {pkg} ")

                            except subprocess.CalledProcessError:
                                print(" " + Fore.BLACK + Back.RED + f" Failed to update {pkg} ")

                        print()

                except Exception:
                    print(" " + Fore.BLACK + Back.RED + " ERROR OCCURRED ")
                    print()
            else:
                print(" " + Fore.BLACK + Back.RED + " UPDATE CANCELLED ")
                print()

        # -------------------------------
        # 10. Check broken dependencies
        # -------------------------------
        elif option == "10":
            print()
            print(Fore.GREEN + " Checking broken dependencies...")
            run_command(
                [sys.executable, "-m", "pip", "check"],
                "Dependency check completed",
                "DEPENDENCY ISSUES FOUND"
            )

        # -------------------------------
        # 11. Save requirements file
        # -------------------------------
        elif option == "11":
            print()
            print(Fore.YELLOW + " NOTE: Run this tool from the desired project folder.")
            req_file = get_requirements_file()

            print(Fore.GREEN + f" Saving project requirements to {req_file}...")

            try:
                save = subprocess.run(
                    [sys.executable, "-m", "pip", "freeze"],
                    stdout=subprocess.PIPE
                )

                with open(req_file, "wb") as f:
                    f.write(save.stdout)

                print(" " + Fore.BLACK + Back.GREEN + f" PROJECT REQUIREMENTS SAVED TO {req_file} ")
                print()

            except subprocess.CalledProcessError:
                print(" " + Fore.BLACK + Back.RED + " ERROR OCCURRED ")
                print()

        # -------------------------------
        # 12. Upgrade PIP version
        # -------------------------------
        elif option == "12":
            print()
            print(Fore.GREEN + " Upgrading to new PIP version...")

            run_command(
                [sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
                "PIP version upgrade successful",
                "ERROR OCCURRED"
            )

        # -------------------------------
        # 13. Check PIP version
        # -------------------------------
        elif option == "13":
            print()
            print(Fore.GREEN + " Displaying PIP version")
            subprocess.run([sys.executable, "-m", "pip", "--version"])
            print()

        # -------------------------------
        # 14. Check Python version
        # -------------------------------
        elif option == "14":
            print()
            print(Fore.GREEN + " Displaying Python version")
            subprocess.run([sys.executable, "--version"])
            print()

        # -------------------------------
        # 15. Clear PIP cache
        # -------------------------------
        elif option == "15":
            print()
            confirm = input(Fore.YELLOW + " Clear PIP cache? (y/n): " + ColorStyle.RESET_ALL).lower()

            if confirm == "y":
                run_command(
                    [sys.executable, "-m", "pip", "cache", "purge"],
                    "PIP cache cleared",
                    "ERROR OCCURRED"
                )
            else:
                print(" " + Fore.BLACK + Back.RED + " CACHE CLEAR CANCELLED ")
                print()

        # -------------------------------
        # 16. Create virtual environment
        # -------------------------------
        elif option == "16":
            print()
            venv_name = input(Fore.CYAN + " Enter virtual environment name: " + ColorStyle.RESET_ALL).strip()

            if venv_name == "":
                venv_name = "venv"

            if os.path.isdir(venv_name):
                print(" " + Fore.BLACK + Back.RED + " VIRTUAL ENVIRONMENT ALREADY EXISTS ")
                print()
            else:
                try:
                    subprocess.check_call([sys.executable, "-m", "venv", venv_name])
                    print(" " + Fore.BLACK + Back.GREEN + f" Created virtual environment: {venv_name} ")
                    print()

                    print(Fore.YELLOW + " Activate it using:")

                    if os.name == "nt":
                        print(Fore.CYAN + f" {venv_name}\\Scripts\\activate")
                    else:
                        print(Fore.CYAN + f" source {venv_name}/bin/activate")

                    print()

                except subprocess.CalledProcessError:
                    print(" " + Fore.BLACK + Back.RED + " ERROR OCCURRED ")
                    print()

        # -------------------------------
        # 17. Create executable
        # -------------------------------
        elif option == "17":
            install_pyinstaller_if_missing()

            print()
            file_name = input(Fore.CYAN + " Enter Python file name (.py): " + ColorStyle.RESET_ALL).strip()

            if os.path.isfile(file_name):
                icon_option = input(Fore.YELLOW + " Do you want an icon for this file? (y/n): " + ColorStyle.RESET_ALL).lower()

                if icon_option == "y":
                    icon_name = input(Fore.CYAN + " Enter ICO file name (.ico): " + ColorStyle.RESET_ALL).strip()

                    if os.path.isfile(icon_name):
                        print()
                        print(Fore.YELLOW + " NOTE: Run this tool from the desired project folder.")
                        print(Fore.GREEN + f" Creating EXE file for {file_name}...")

                        run_command(
                            ["pyinstaller", "--onefile", f"--icon={icon_name}", file_name],
                            f"Created EXE file for {file_name}",
                            "ERROR OCCURRED"
                        )
                    else:
                        print(" " + Fore.BLACK + Back.RED + " ICON FILE DOES NOT EXIST ")
                        print()

                elif icon_option == "n":
                    print()
                    print(Fore.YELLOW + " NOTE: Run this tool from the desired project folder.")
                    print(Fore.GREEN + f" Creating EXE file for {file_name}...")

                    run_command(
                        ["pyinstaller", "--onefile", file_name],
                        f"Created EXE file for {file_name}",
                        "ERROR OCCURRED"
                    )
                else:
                    print(" " + Fore.BLACK + Back.RED + " INVALID OPTION ")
                    print()
            else:
                print(" " + Fore.BLACK + Back.RED + " FILE DOES NOT EXIST ")
                print()

        # -------------------------------
        # 18. Clear terminal
        # -------------------------------
        elif option == "18":
            clear_terminal()
            print_title()

        # -------------------------------
        # 19. Exit
        # -------------------------------
        elif option == "19":
            print()
            break


if __name__ == "__main__":
    main()