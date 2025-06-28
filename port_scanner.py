import socket
from concurrent.futures import ThreadPoolExecutor
import argparse

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # 1 second timeout
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} is OPEN")
    except Exception:
        pass

def main():
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument('--host', type=str, required=True, help='Target host IP or domain')
    parser.add_argument('--start', type=int, default=1, help='Start port number (default: 1)')
    parser.add_argument('--end', type=int, default=1024, help='End port number (default: 1024)')

    args = parser.parse_args()

    print(f"Scanning ports {args.start} to {args.end} on {args.host}...\n")

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(args.start, args.end + 1):
            executor.submit(scan_port, args.host, port)

if __name__ == "__main__":
    main()