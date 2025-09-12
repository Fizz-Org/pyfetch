import psutil

mem = psutil.virtual_memory()
mem_total = round(mem.total / (1024**3), 1)
mem_used = round(mem.used / (1024**3), 1)
mem_usedprct = round(mem_used / mem_total * 100, 1)