import socket

def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return "Internet connection is available."
    except OSError:
        return "Internet connection is not available."

if __name__ == "__main__":
    print("TechAssist Network Check:")
    print(check_internet())