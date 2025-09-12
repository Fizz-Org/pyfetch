import os

def get_cpu():

    system = os.system

    if system == "Linux":
        try:
           with open("/proc/cpuinfo") as f:
              for line in f:
                   if "model name" in line:
                     return line.strip().split(": ")[1]
        except:
            pass
        return "Unknown CPU"
