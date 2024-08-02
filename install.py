import os
import shutil

# Set the script name and version
SCRIPT_NAME = "ctf-flag-scanner"
VERSION = "1.0"

# Set the installation directory
INSTALL_DIR = "/usr/local/bin"

# Check if the script is already installed
if os.path.isfile(os.path.join(INSTALL_DIR, SCRIPT_NAME)):
    print("Error: {} is already installed.".format(SCRIPT_NAME))
    exit(1)

# Create the installation directory if it doesn't exist
if not os.path.exists(INSTALL_DIR):
    os.makedirs(INSTALL_DIR)

# Copy the script to the installation directory
shutil.copy("ctf-flag-scanner.py", os.path.join(INSTALL_DIR, SCRIPT_NAME))

# Make the script executable
os.chmod(os.path.join(INSTALL_DIR, SCRIPT_NAME), 0o755)

# Print a success message
print("Installation complete! You can now run {} from anywhere.".format(SCRIPT_NAME))

# Add a git hook to run the script
with open(os.path.expanduser("~/.gitconfig"), "a") as f:
    f.write("[alias]\nctf-flag-scanner =!{} {}\n".format(INSTALL_DIR, SCRIPT_NAME))
