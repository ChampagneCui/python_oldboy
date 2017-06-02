import socket

hostname = socket.gethostname() 
ip = socket.gethostbyname(hostname)
ipList = socket.gethostbyname_ex(hostname)
print(ipList)
