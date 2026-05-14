# pydepmgr

`pydepmgr` is a simple terminal-based Python dependency manager. It gives you an interactive menu for common `pip`, requirements file, virtual environment, and PyInstaller tasks.

## Features

- Install Python packages
- Update installed packages
- Uninstall packages
- Batch install packages from a requirements file
- Batch uninstall packages from a requirements file
- Search for an installed package
- List installed packages
- List outdated packages
- Update all outdated packages
- Check broken dependencies
- Save installed packages to a requirements file
- Upgrade pip
- Check pip and Python versions
- Clear the pip cache
- Create a virtual environment
- Create an executable file with PyInstaller

## Installation

Install `pydepmgr` with pip:

```bash
pip install pydepmgr
```

## Usage

After installation, run:

```bash
pydepmgr
```

You will see an interactive menu where you can choose what you want to do.

## Requirements

- Python 3.8 or newer
- pip

The package automatically installs its required dependencies:

- `colorama`
- `questionary`

## Example Workflow

```bash
pydepmgr
```

Then choose an option from the menu, such as:

- Install a package
- Update a package
- Save a requirements file
- Create a virtual environment
- Check broken dependencies

## Notes

- Run `pydepmgr` from the project folder you want to manage.
- Batch install and uninstall actions use a requirements file such as `requirements.txt`.
- The executable creation option uses PyInstaller. If PyInstaller is missing, `pydepmgr` will install it automatically.

## Project Links

- PyPi: https://pypi.org/project/pydepmgr/1.6.0/
