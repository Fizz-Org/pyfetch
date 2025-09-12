import subprocess

def get_pkgs(command, skip=0):
    try:
        output = subprocess.check_output(command, shell=True, text=True).splitlines()
        return len(output) - skip
    except subprocess.CalledProcessError:
        return 0

pacman_count = get_pkgs("pacman -Qq")
yay_count = get_pkgs("yay -Qq")
flatpak_count = get_pkgs("flatpak list --app --columns=application")
pip_count = get_pkgs("pip list", skip=2)