from system import cpu, gpu, misc, packages, ram, storage

with open('./ascii/arch.txt', 'r') as f:
    ascii_logo = f.readlines()

sysinfo = [
    f"\033[38;2;0;255;255m{misc.usr}\033[0m@\033[38;2;0;255;255m{misc.hostname}\033[0m",
    "----------------------",
    f"OS:       {misc.dist} {misc.arch}",
    f"Memory:   {ram.mem_used}/{ram.mem_total} GB ({ram.mem_usedprct}%)",
    f"Storage:  {storage.disk_used}/{storage.disk_total} GB ({storage.disk_usgprct}%)",
    f"Uptime:   {misc.uptime_hrs} Hours, {misc.uptime_mns} Minutes",
    f"CPU:      {cpu.get_cpu()}",
    f"GPU(s):   {gpu.return_gpu()}",
    f"Packages: {packages.pacman_count} (Pacman), {packages.flatpak_count} (Flatpak), {packages.pip_count} (PIP)"
]

max_len = max(len(ascii_logo), len(sysinfo))
ascii_logo += [""] * (max_len - len(ascii_logo))
sysinfo += [""] * (max_len - len(sysinfo))

for left, right in zip(ascii_logo, sysinfo):
    print(f"{left.rstrip():<25} {right}")
