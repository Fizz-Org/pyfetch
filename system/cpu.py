import platform, subprocess
    
def get_win_cpu():
    if platform.system != "Windows":
        return []
    
    import wmi
    try:
        pc = wmi.WMI()
        cpu_name = pc.Win32_Processor()[0].Name
        return cpu_name
    except:
        pass
    return "Unknown CPU"

def get_linux_cpu():
    try:
        with open("/proc/cpuinfo") as f:
            for line in f:
                if "model name" in line:
                    return line.strip().split(": ")[1]
    except:
        pass
    return "Unknown CPU"

def get_darwin_cpu():
    try:
        result = subprocess.check_output(['sysctl', '-n', 'machdep.cpu.brand_string'], text=True)
        return result.strip()
    except:
        pass
    return "Unknown CPU"

def get_cpu():
    system = platform.system()

    if system == "Linux":
        return get_linux_cpu()
    elif system == "Windows":
        return get_win_cpu()
    elif system == "Darwin":
        return get_darwin_cpu()
