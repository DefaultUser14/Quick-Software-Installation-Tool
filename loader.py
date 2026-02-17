import sys
from pathlib import Path

def scan_packages():
    BASE_DIR = Path(sys.argv[0]).resolve().parent
    FILES_DIR = BASE_DIR / "files"

    if not FILES_DIR.is_dir():
        raise FileNotFoundError(f'"files" folder not found in: {BASE_DIR}')
    
    file_list = []
    for f in FILES_DIR.iterdir():
        if f.is_file() and f.suffix.lower() in (".exe", ".msi"):
            file_list.append(f.name)

    return(file_list)