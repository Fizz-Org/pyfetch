import shutil

# Storage vars

KB = 1024
MB = 1024 * KB
GB = 1024 * MB

disk_total = round(shutil.disk_usage("/").total / GB, 1)
disk_used = round(shutil.disk_usage("/").used / GB, 1)
disk_usgprct = round(disk_used / disk_total * 100, 1)