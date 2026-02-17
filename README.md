# Quick Installation Tool

A lightweight Windows software installation tool built with **Python** and **Tkinter**.

This tool allows you to select and install multiple `.exe` or `.msi` files from a predefined folder using an administrator-elevated GUI interface.

---

## Features

- Automatic Administrator elevation (UAC)
- Simple Tkinter-based GUI
- Batch installation of selected programs
- Live log output window
- Supports `.exe` and `.msi` installers
- Can be compiled into a standalone `.exe`

---

## Requirements (if not using the compiled `.exe`)

- Python 3.11+
- Dependencies listed in `requirements.txt`

Install dependencies:

```bash
pip install -r requirements.txt
```
---

## Usage

1. Run `main.py` or `main.exe` as Administrator  
2. Select the programs you want to install  
3. Click **Start**  
4. Wait until installation is finished

## Build Executable

Using PyInstaller:

```bash
python -m PyInstaller --onefile --noconsole  --icon=".\images\icon.ico"  main.py
```


