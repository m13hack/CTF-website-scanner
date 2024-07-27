import subprocess
import sys

def install(package):
    """Install a Python package using pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    """Main function to handle package installation."""
    try:
        import selenium
        print("The 'selenium' package is already installed.")
    except ImportError:
        print("The 'selenium' package is not installed. Installing...")
        install('selenium')
        print("The 'selenium' package has been installed.")

if __name__ == "__main__":
    main()
