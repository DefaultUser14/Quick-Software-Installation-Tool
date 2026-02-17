import pyuac
import sys

def main():
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
        sys.exit()

    import gui
    gui.run()
    
if __name__ == "__main__":
    main()