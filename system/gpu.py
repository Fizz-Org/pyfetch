import platform
import subprocess
import re

def get_gpu():
    system = platform.system()
    gpus = []

    try:
        if system == "Windows":
            output = subprocess.check_output(
                ["powershell", "-Command", "Get-CimInstance Win32_VideoController | Select-Object -ExpandProperty Name"],
                stderr=subprocess.DEVNULL
            ).decode(errors="ignore").splitlines()
            gpus = [line.strip() for line in output if line.strip()]

        elif system == "Linux":
            output = subprocess.check_output(
                "lspci -nnk | grep -A3 -E 'VGA|3D|Display'", shell=True
            ).decode(errors="ignore").splitlines()
            gpus = []
            for line in output:
                if "VGA" in line or "3D" in line or "Display" in line:
                    matches = re.findall(r"\[(.*?)\]", line)
                    if matches:
                        gpus.append(matches[1])

        elif system == "Darwin":
            output = subprocess.check_output(
                "ioreg -l | grep 'model'", shell=True
            ).decode(errors="ignore").splitlines()
            gpus = [re.sub(r'.*"([^"]+)"', r"\1", line).strip() for line in output if line.strip()]

        else:
            gpus = ["Unsupported OS"]

    except Exception as e:
        gpus = [f"Error: {e}"]

    return gpus


def return_gpu():
    gpus = get_gpu()
    if not gpus:
        return "No GPU detected"
    if len(gpus) == 1:
        return gpus[0]
    return ", ".join(gpus)

