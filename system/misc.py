import psutil, time, distro

dist = distro.name()

boot_time = psutil.boot_time()
uptime_seconds = time.time() - boot_time
uptime_hrs = int(uptime_seconds // 3600)
uptime_mns = int((uptime_seconds % 3600) // 60)