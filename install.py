import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    try:
        import requests
    except ImportError:
        install('requests')

    print("All dependencies are installed!")

if __name__ == "__main__":
    main()
