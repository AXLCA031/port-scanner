import socket

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open on {target}")
        sock.close()
    except:
        pass

def main():
    target = input("Enter target IP address or hostname: ")
    ports = range(1, 1025)  # Scan ports from 1 to 1024

    for port in ports:
        scan_port(target, port)

if __name__ == "__main__":
    main()