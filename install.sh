#!/bin/bash
set -e 

# -------------
# Configuration
# -------------
INSTALL_DIR="/opt/pyfetch-dir"
VENV_DIR="$INSTALL_DIR/venv"

DEPENDENCIES=(
    "distro==1.9.0"
    "markdown-it-py==4.0.0"
    "mdurl==0.1.2"
    "psutil==7.0.0"
    "Pygments==2.19.2"
    "rich==14.1.0"
)

# -----------------------------------
# Remove old installation if existing
# -----------------------------------
if [ -d "$INSTALL_DIR" ]; then
    echo "Removing old installation..."
    sudo rm -rf "$INSTALL_DIR"
fi

# ----------------
# Clone repository
# ----------------
sudo git clone https://github.com/Fizz-Org/pyfetch.git "$INSTALL_DIR"

# -----------------------
# Detect main Python file
# -----------------------
MAIN_SCRIPT=$(find "$INSTALL_DIR" -maxdepth 1 -type f -name "*.py" | head -n 1)

if [ -z "$MAIN_SCRIPT" ]; then
    echo "No Python file found in the repository. Please try again."
    exit 1
fi

echo "Detected main script: $MAIN_SCRIPT"

# -----------------------
# Add shebang if missing
# -----------------------
if ! head -n 1 "$MAIN_SCRIPT" | grep -q "^#\!"; then
    echo "Adding shebang to $MAIN_SCRIPT"
    sudo sed -i '1i #!/usr/bin/env python3' "$MAIN_SCRIPT"
fi

# --------------------------
# Create virtual environment
# --------------------------
echo "Creating virtual environment..."
sudo python3 -m venv "$VENV_DIR"

# --------------------------------------
# Install dependencies in venv (no sudo)
# --------------------------------------
echo "Installing dependencies..."
source "$VENV_DIR/bin/activate"
pip install --upgrade pip
for pkg in "${DEPENDENCIES[@]}"; do
    pip install "$pkg"
done
deactivate

# -------------------------------
# Make the main script executable
# -------------------------------
sudo chmod +x "$MAIN_SCRIPT"

# -----------------------
# Create launcher script
# -----------------------
LAUNCHER="$INSTALL_DIR/pyfetch-launcher"
sudo tee "$LAUNCHER" > /dev/null << EOF
#!/bin/bash
source "$VENV_DIR/bin/activate"
exec python "$MAIN_SCRIPT" "\$@"
EOF
sudo chmod +x "$LAUNCHER"

# -----------------------
# Create symlink in PATH
# -----------------------
sudo ln -sf "$LAUNCHER" /usr/local/bin/pyfetch

echo "Installation complete. You can now run pyfetch from anywhere."
