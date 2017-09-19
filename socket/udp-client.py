# This example is using Python 3.6
import socket

# Get host name, IP address, and port number.
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
host_port = 8181

# Make a UDP socket object.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = ['Hello network world', 'This is Zhifeng']
bufsize = 1024
for line in message:
  # Send messages to server over UDP socket.
  #
  # API: sendto(bytes, address)
  #   Send data to the socket. The socket should not be connected to a
  #   remote socket, since the destination socket is specified by
  #   address. Return the number of bytes sent.
  s.sendto(str.encode(line), (host_ip, host_port))
  data, addr = s.recvfrom(bufsize)
  print(addr, '==>', data)
