from socket import *
from select import select

sockfd = socket()
sockfd.bind(("0.0.0.0", 8888))
sockfd.listen(5)

sockfd.setblocking(False)

rlist = [sockfd]
wlist = []
xlist = []

while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        if r is sockfd:
            connfd, addr = r.accept()
            print("Connect from", addr)
            connfd.setblocking(False)
            rlist.append(connfd)
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
            wlist.append(r)
    for w in ws:
        w.send(b"OK")
        wlist.remove(w)
    for x in xs:
        pass


