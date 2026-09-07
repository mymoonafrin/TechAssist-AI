import platform
import socket
import sys

def get_system_info():
    info = {
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Computer Name": socket.gethostname(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Python Version": sys.version.split()[0]
    }

    return info

if __name__ == "__main__":
    print("TechAssist System Information:\n")

    system_info = get_system_info()

    for key, value in system_info.items():
        print(f"{key}: {value}")