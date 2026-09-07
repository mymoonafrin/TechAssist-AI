import subprocess
import platform

def ping_host(host):
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
    host = input("Enter a host to ping: ")
    print("\nTechAssist Ping Diagnostic:")
    print(ping_host(host))