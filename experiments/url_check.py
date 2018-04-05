import socket

try:
    socket.gethostbyname('www.google.com')
except socket.gaierror as ex:
    print("not existe")
