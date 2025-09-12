from system import cpu, gpu, misc, packages, ram, storage

print(f"\033[38;2;0;255;255m\n{misc.usr}\033[0m@\033[38;2;0;255;255m{misc.hostname}\033[0m\n----------------------")
print(f"OS:       {misc.dist} {misc.arch}")
print(f"Memory:   {ram.mem_used}/{ram.mem_total} GB ({ram.mem_usedprct}%)")
print(f"Storage:  {storage.disk_used}/{storage.disk_total} GB ({storage.disk_usgprct}%)")
print(f"Uptime:   {misc.uptime_hrs} Hours, {misc.uptime_mns} Minutes")
print(f"CPU:      {cpu.get_cpu()}")
print(f"GPU:      {gpu.return_gpu()}")
print(f"Packages: {packages.pacman_count} (Pacman), {packages.flatpak_count} (Flatpak), {packages.pip_count} (PIP)")

# Temporary Feature - Not for long term usage.

#f = open('./ascii/arch.txt', 'r')
#file_contents = f.read()
#print(file_contents)
#f.close() 