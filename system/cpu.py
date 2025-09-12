def get_cpu():
    try:
        with open("/proc/cpuinfo") as f:
            for line in f:
                if "model name" in line:
                    return line.strip().split(": ")[1]
    except:
        pass
    return "Unknown CPU"
