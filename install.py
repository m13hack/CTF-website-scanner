import subprocess
import sys

def install(package):
    """Install a package using pip."""
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

def main():
    """Install all required dependencies."""
    packages = [
        'requests',
        'beautifulsoup4',
        'exifread',
        # Add other dependencies if needed
    ]
    
    for package in packages:
        print(f"Installing {package}...")
        install(package)
    
    print("All dependencies installed successfully!")

if __name__ == "__main__":
    main()
