import socket
import random
import time

from agents import random_agent

host = "127.0.0.1"
port = 80
s = None

def send_line(s, data):
    s.send(bytes(f"{data}\n", 'utf8'))

def send_header(s, header, value):
    send_line(s, f"{header}: {value}")

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    s.connect((host, port))
    
    send_line(s, f"GET /?{random.randint(0, 2000)} HTTP/1.1\n")
    send_header(s, "User-Agent", random_agent())
    return s
