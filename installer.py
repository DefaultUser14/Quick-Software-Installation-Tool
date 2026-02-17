import subprocess
import sys
from pathlib import Path

def install_software(package_list, log_callback):
    path_list = []
    name_list = []
    BASE_DIR = Path(sys.argv[0]).resolve().parent
    FILES_DIR = BASE_DIR / "files"
    success = 0
    
    for i in package_list:
        installer_path = FILES_DIR / i
        path_list.append(installer_path)
        name_list.append(i.split('.', 1)[0])

    n = 0
    for i in path_list:
        
        installer_path = i
        try:
            if not installer_path.is_file():
                log_callback(f"{n+1}/{len(path_list)}\n{name_list[n]} Installation file not found\n", 'error')
                n+=1
            else:
                if installer_path.suffix.lower() == ".msi":
                    subprocess.run(["msiexec", "/i", str(installer_path), "/qn"], check=True, cwd=r'C:\WINDOWS\system32')

                elif installer_path.suffix.lower() == ".exe":
                    subprocess.run([str(installer_path), "/S"], check=True, cwd=r'C:\WINDOWS\system32')
                
                #subprocess.run(command, check=True, cwd=r'C:\WINDOWS\system32')
                log_callback(f"{n+1}/{len(path_list)}\nSuccessfully installed {name_list[n]}\n", 'success')
                n +=1
                success +=1

        except subprocess.CalledProcessError as e:
            
            log_callback(f"{n+1}/{len(path_list)}\nFailed to install {name_list[n]}\n{e}\n", 'error')
            n +=1
            
    log_callback(f'INSTALLATION FINISHED\nSUCCESSFULLY INSTALLED {success} OUT OF {len(path_list)} PACKAGES', 'success')          
