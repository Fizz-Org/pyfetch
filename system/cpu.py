import platform, wmi, subprocess

def get_cpu():

    system = platform.system

    if system == "Linux":
        try:
           with open("/proc/cpuinfo") as f:
              for line in f:
                   if "model name" in line:
                     return line.strip().split(": ")[1]
        except:
            pass
        return "Unknown CPU"
    
    elif system == "Windows":
        try:
            pc = wmi.WMI()
            cpu_name = pc.Win32_Processor()[0].Name
            return cpu_name
        except:
            pass
        return "Unknown CPU"
    
    elif system == "Darwin":
        try:
            result = subprocess.check_output(['sysctl', '-n', 'machdep.cpu.brand_string'], text=True)
            return result.strip()
        except:
            pass
        return "Unknown CPU"
