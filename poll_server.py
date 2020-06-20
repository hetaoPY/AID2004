"""
IO多路复用
"""

from socket import *
from select import *

sockfd = socket()
sockfd.bind(("0.0.0.0", 8888))
sockfd.listen(5)

sockfd.setblocking(False)

p_dict = dict({})
p = poll()
p.register(sockfd, POLLIN)
p_dict[sockfd.fileno()] = sockfd

while True:
    events = p.poll()
    for fd, event in events:
        if fd == sockfd.fileno():
            connfd, addr = p_dict[fd].accept()
            print("Connect from", addr)
            connfd.setblocking(False)
            p.register(connfd, POLLIN)
            p_dict[connfd.fileno()] = connfd
        else:
            data = p_dict[fd].recv(1024)
            if not data:
                p.unregister(p_dict[fd])
                p_dict[fd].close()
                del p_dict[fd]
                continue
            print(data.decode())
            p_dict[fd].send(b"OK")
