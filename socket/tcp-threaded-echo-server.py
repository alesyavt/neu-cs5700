# This example is using Python 3.6
import socket
import _thread
import time

# Get host name, IP address, and port number.
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
host_port = 8181

# Make a TCP socket object.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to server IP and port number.
s.bind((host_ip, host_port))

# Start listen to incoming requests.
s.listen()
print('Server started. Waiting for connection...')

# Current time on the server.
def now():
  return time.ctime(time.time())

bufsize = 1024
def handler(conn, addr):
  while True:
    data = conn.recv(bufsize)
    if not data: break
    print('Server received: ', data, 'from', addr)
    conn.sendall(str.encode('Echo ==> ') + data)
    time.sleep(10)  # simulating long running program
  conn.close()


while True:
  conn, addr = s.accept()
  print('Server connected by', addr, 'at', now())
  _thread.start_new_thread(handler, (conn,addr))
