import os, psutil, shutil, socket, rich, getpass, platform, distro, time, subprocess

from system import cpu, ram, misc

# Storage Vars

KB = 1024
MB = 1024 * KB
GB = 1024 * MB

# Misc Vars

hostname = socket.gethostname()
ip_addr = socket.gethostbyname(socket.gethostname())
disk_total = round(shutil.disk_usage("/").total / GB, 1)
disk_used = round(shutil.disk_usage("/").used / GB, 1)
disk_usgprct = round(disk_used / disk_total * 100, 1)
usr = getpass.getuser()
arch = platform.machine()

# Distro Vars -- HAS BEEN MOVEDTO ./system/misc.py !

# Uptime Vars -- HAS BEEN MOVED TO ./system/misc.py !

# CPU vars and functions -- HAS BEEN MOVED TO ./system/cpu.py !

# RAM vars -- HAS BEEN MOVED TO ./system/ram.py !

# Package functions

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

print(f"\033[38;2;0;255;255m\n{usr}\033[0m@\033[38;2;0;255;255m{hostname}\033[0m\n----------------------")
print(f"OS:       {misc.dist} {arch}")
print(f"Memory:   {ram.mem_used}/{ram.mem_total} GB ({ram.mem_usedprct}%)")
print(f"Storage:  {disk_used}/{disk_total} GB ({disk_usgprct}%)")
print(f"Uptime:   {misc.uptime_hrs} Hours, {misc.uptime_mns} Minutes")
print(f"CPU:      {cpu.get_cpu()}")
print(f"Packages: {pacman_count} (Pacman), {flatpak_count} (Flatpak), {pip_count} (PIP)")

# Temporary Feature - Not for long term usage.

f = open('./ascii/arch.txt', 'r')
file_contents = f.read()
print(file_contents)
f.close() 