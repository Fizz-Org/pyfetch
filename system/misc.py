import psutil, time, distro, socket, getpass, platform

# Linux Only

dist = distro.name()

# Boot Time

boot_time = psutil.boot_time()
uptime_seconds = time.time() - boot_time
uptime_hrs = int(uptime_seconds // 3600)
uptime_mns = int((uptime_seconds % 3600) // 60)

# Hostname and IP vars

hostname = socket.gethostname()
ip_addr = socket.gethostbyname(socket.gethostname())

# Username var

usr = getpass.getuser()

# Architecture var

arch = platform.machine()