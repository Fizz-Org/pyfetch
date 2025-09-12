import subprocess

def get_pkgs(command, skip=0):
    try:
        output = subprocess.check_output(
            command,
            shell=True,
            text=True,
            stderr=subprocess.DEVNULL 
        ).splitlines()
        
        if len(output) <= skip:
            return 0

        return len(output) - skip

    except (subprocess.CalledProcessError, FileNotFoundError):
        return 0

pacman_count = get_pkgs("pacman -Qq")
yay_count = get_pkgs("yay -Qq")
flatpak_count = get_pkgs("flatpak list --app --columns=application")
pip_count = get_pkgs("pip list", skip=2)