"""
非阻塞IO演示
套接字对象 --》非阻塞
"""

from socket import *
import time

sockfd = socket()
sockfd.bind(("0.0.0.0", 8888))
sockfd.listen(5)

sockfd.setblocking(False)
sockfd.settimeout(3)
while True:
    try:
        print("................")
        connfd, addr = sockfd.accept()
        print("Connect from", addr)
    except BlockingIOError as e:
        time.sleep(2)
        with open("test.log", "a") as f:
            msg = "%s :%s \n" % (time.ctime(), e)
            f.write(msg)
    except timeout as e:
        with open("test.log", "a") as f:
            msg = "%s :%s \n" % (time.ctime(), e)
            f.write(msg)
    else:
        data = connfd.recv(1024)
