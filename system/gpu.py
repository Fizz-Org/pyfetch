import platform
import subprocess
import re

def get_gpu():
    system = platform.system()
    gpus = []

    try:
        if system == "Windows":
            output = subprocess.check_output(
                ["wmic", "path", "win32_VideoController", "get", "name"],
                shell=True
            ).decode(errors="ignore").splitlines()
            gpus = [line.strip() for line in output if line.strip() and "Name" not in line]

        elif system == "Linux":
            output = subprocess.check_output(
                "lspci | grep -i 'vga\\|3d\\|display'", shell=True
            ).decode(errors="ignore").splitlines()
            gpus = [re.sub(r".*:\s*", "", line).strip() for line in output if line.strip()]

        elif system == "Darwin":  # macOS
            output = subprocess.check_output(
                ["system_profiler", "SPDisplaysDataType"],
                stderr=subprocess.DEVNULL
            ).decode(errors="ignore").splitlines()
            gpus = [line.split(":")[1].strip() for line in output if "Chipset Model:" in line]

        else:
            gpus = ["Unsupported OS"]

    except Exception as e:
        gpus = [f"Error: {e}"]

    return gpus

def return_gpu():
    gpus = get_gpu()
    return "\n".join(gpus)