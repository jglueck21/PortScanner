import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # 1 second timeout
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} is OPEN")
    except Exception as e:
        pass  # Ignore errors for now

def main():
    host = input("Enter the host to scan (IP or domain): ")
    start_port = int(input("Enter start port number: "))
    end_port = int(input("Enter end port number: "))

    print(f"Scanning ports {start_port} to {end_port} on {host}...\n")

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, host, port)

if __name__ == "__main__":
    main()
