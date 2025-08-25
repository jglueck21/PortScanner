# 🔍 Python Port Scanner

A simple but effective **Python-based port scanner** that detects open TCP ports on a host.  
Inspired by tools like **Nmap**, this project demonstrates the fundamentals of network enumeration and cybersecurity.

---

## 🚀 Features
- Multi-threaded scanning for faster results  
- Detects open **TCP ports** in a given range  
- Maps ports to common services (e.g., `22 → ssh`, `3306 → mysql`)  
- Built-in timeout handling (avoids freezing on closed/filtered ports)  
- Tested safely on:
  - Localhost
  - Docker containers (e.g., MariaDB on port 3306)
  - Public test host [`scanme.nmap.org`](https://scanme.nmap.org)

---

## 📖 How It Works
The scanner uses Python’s built-in [`socket`](https://docs.python.org/3/library/socket.html) module to:
1. Create a TCP socket for each port  
2. Attempt a connection to the target host and port  
3. Return `open` if the connection succeeds within a given timeout  
4. Look up the associated service name (if available)  

Concurrency is handled using Python’s `threading` library, allowing multiple ports to be scanned simultaneously.

---

## 💻 Usage

### 1. Run the script
python3 scanner.py <host> <start_port> <end_port>

### 2. Example (scan MariaDB container on port 3306)
python3 scanner.py localhost 3300 3400

**Output:**
🔍 Scanning localhost from port 3300 to 3400...

[+] Port 3306 is open (mysql)

✅ Scan complete!

### 3. Example (scan public test host)
python3 scanner.py scanme.nmap.org 20 1000

---

## 🛡️ Safe Testing
⚠️ Always scan **only**:
- Your own machine (`localhost`)  
- Local test environments (e.g., Docker containers)  
- Approved test servers like `scanme.nmap.org`  

Never scan random websites or servers without explicit permission.

---

## 🎓 Skills Learned
- Networking fundamentals (TCP/IP, ports, sockets)  
- Writing Python scripts with error handling and timeouts  
- Using threads for concurrent execution  
- Safe penetration testing practices using controlled environments  

---

## 🔮 Possible Future Updates
- [ ] Add **process lookup** to show which program is bound to an open port  
- [ ] Implement **UDP scanning** in addition to TCP  
- [ ] Add an option for **output reports** (JSON, CSV, HTML)  
- [ ] Include a **progress bar / fancy CLI UI** for better user experience  
- [ ] Compare results automatically with `nmap` for validation  

---

## 📸 Demo Screenshot Idea
<img width="1104" height="196" alt="image" src="https://github.com/user-attachments/assets/589fa8eb-936c-4fdf-b297-58e18f28d9a7" />

---

## 📜 License
This project is released under the MIT License.  
You are free to use, modify, and share it with attribution.
