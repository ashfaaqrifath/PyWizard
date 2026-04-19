# PyWizard
 
A Python package manager CLI tool with an interactive menu — install, update, uninstall, batch manage, check status, save requirements, create EXEs, and more. All from a clean, color-coded terminal interface.
 
> **Current Version:** v1.5.5
 
---
 
## ✨ Features
 
All features are accessible via an interactive arrow-key menu:
 
| # | Option | Description |
|---|--------|-------------|
| 1 | **Install package** | Install a single pip package by name |
| 2 | **Batch install from requirements.txt** | Install all packages listed in `requirements.txt` |
| 3 | **Update package** | Upgrade a package to its latest version |
| 4 | **Uninstall package** | Remove a single package |
| 5 | **Batch uninstall from requirements.txt** | Uninstall all packages listed in `requirements.txt` |
| 6 | **Check package status** | Verify if a package is installed and show its info |
| 7 | **Display installed packages** | List all currently installed packages (`pip list`) |
| 8 | **Save requirements file** | Freeze current environment to `requirements.txt` |
| 9 | **Upgrade PIP version** | Upgrade pip itself to the latest version |
| 10 | **Check PIP version** | Display current pip version |
| 11 | **Check Python version** | Display current Python version |
| 12 | **Create EXE for Python file** | Convert a `.py` file to a standalone `.exe` using PyInstaller (with optional custom icon) |
| 13 | **Clear terminal** | Clear the terminal and redisplay the menu |
 
---
 
## 📁 Project Structure
 
```
PyWizard/
├── PyWizard.py         # Main script
└── requirements.txt    # PyWizard's own dependencies
```
 
---
 
## ⚙️ Requirements
 
Python 3.x + the following packages:
 
```bash
pip install questionary colorama
```
 
> `colorama` and `pyinstaller` (for option 12) are auto-installed by PyWizard if not found.
 
---
 
## 🚀 Setup & Usage
 
1. Clone the repo:
   ```bash
   git clone https://github.com/ashfaaqrifath/PyWizard.git
   cd PyWizard
   ```
 
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
 
3. Run PyWizard:
   ```bash
   python PyWizard.py
   ```
 
4. Use the arrow keys to navigate the menu and press **Enter** to select an option.
---
 
## 💡 Usage Tips
 
- **Options 2 & 5** (batch install/uninstall) require a `requirements.txt` file to exist in the same directory you run PyWizard from
- **Option 8** (save requirements) — run from your project's root folder to capture its specific dependencies
- **Option 12** (create EXE) — run from the folder containing your `.py` file; optionally provide a `.ico` file for a custom icon; PyInstaller is auto-installed if needed
---
 
## 🛠️ Tech Stack
 
- **Language:** Python 3
- **Interactive Menu:** `questionary`
- **Terminal Styling:** `colorama`
- **Package Management:** `pip` (via `subprocess`)
- **EXE Creation:** `pyinstaller`
