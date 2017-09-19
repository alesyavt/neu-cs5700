# This example is using Python 3.6
import socket

# Get host name, IP address, and port number.
host_name = socket.gethostname()
print(host_name)
host_ip = socket.gethostbyname(host_name)
host_port = 8181

# Make a UDP socket object.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to server IP and port number.
s.bind((host_ip, host_port))
print('Server started. Waiting for connection...')

bufsize = 1024
while True:
  data, addr = s.recvfrom(bufsize)
  print(addr, '==>', data)
  s.sendto(data, addr)
