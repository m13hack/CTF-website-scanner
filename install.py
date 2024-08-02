#!/bin/bash

# Set the script name and version
SCRIPT_NAME="ctf-flag-scanner"
VERSION="1.0"

# Set the installation directory
INSTALL_DIR="/usr/local/bin"

# Check if the script is already installed
if [ -f "$INSTALL_DIR/$SCRIPT_NAME" ]; then
  echo "Error: $SCRIPT_NAME is already installed."
  exit 1
fi

# Create the installation directory if it doesn't exist
if [ ! -d "$INSTALL_DIR" ]; then
  mkdir -p "$INSTALL_DIR"
fi

# Copy the script to the installation directory
cp ctf-flag-scanner.py "$INSTALL_DIR/$SCRIPT_NAME"

# Make the script executable
chmod +x "$INSTALL_DIR/$SCRIPT_NAME"

# Add a shebang line to the script
echo "#!/usr/bin/env python3" > "$INSTALL_DIR/$SCRIPT_NAME"

# Append the script contents to the file
cat ctf-flag-scanner.py >> "$INSTALL_DIR/$SCRIPT_NAME"

# Print a success message
echo "Installation complete! You can now run $SCRIPT_NAME from anywhere."

# Add a git hook to run the script
git config --global alias.ctf-flag-scanner '!'"$INSTALL_DIR/$SCRIPT_NAME"
