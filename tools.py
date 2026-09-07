import socket
import platform
import subprocess
import sys
from langchain_core.tools import tool

@tool
def check_internet():
    """Check whether the computer currently has internet connectivity."""
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return "Internet connection is available."
    except OSError:
        return "Internet connection is not available."

@tool
def get_system_info():
    """Get basic information about the current computer."""
    info = {
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Computer Name": socket.gethostname(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Python Version": sys.version.split()[0]
    }

    return "\n".join(f"{key}: {value}" for key, value in info.items())

@tool
def ping_host(host: str):
    """Ping a specified host four times and return the connectivity results."""
    parameter = "-n" if platform.system().lower() == "windows" else "-c"

    try:
        result = subprocess.run(
            ["ping", parameter, "4", host],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0:
            return f"Ping successful for {host}.\n\n{result.stdout}"
        else:
            return f"Ping failed for {host}.\n\n{result.stdout}"

    except subprocess.TimeoutExpired:
        return f"Ping timed out for {host}."

    except Exception as e:
        return f"Unable to perform ping: {e}"

if __name__ == "__main__":
    print(check_internet.invoke({}))
    print()
    print(get_system_info.invoke({}))
    print()
    print(ping_host.invoke({"host": "google.com"}))