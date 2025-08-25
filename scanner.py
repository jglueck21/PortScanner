import socket
import argparse
import threading

# Try to grab a service name from the port
def get_service(port):
    try:
        return socket.getservbyport(port)
    except:
        return "Unknown service"

# Function to scan a single port
def scan_port(host, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"[+] Port {port} is open ({get_service(port)})")
    except Exception as e:
        pass  # ignore errors like refused connections

# Function to scan a range of ports
def scan_ports(host, start_port, end_port, threads=100):
    print(f"\n🔍 Scanning {host} from port {start_port} to {end_port}...\n")

    thread_list = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(host, port))
        thread_list.append(t)
        t.start()

        # Limit number of active threads
        if len(thread_list) >= threads:
            for t in thread_list:
                t.join()
            thread_list = []

    # Join any remaining threads
    for t in thread_list:
        t.join()

    print("\n✅ Scan complete!")

# Command-line interface
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("host", help="Target hostname or IP address")
    parser.add_argument("start_port", type=int, help="Start port")
    parser.add_argument("end_port", type=int, help="End port")
    args = parser.parse_args()

    scan_ports(args.host, args.start_port, args.end_port)
