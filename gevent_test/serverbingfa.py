import sys
import socket
import time
import gevent

from gevent import socket,monkey
monkey.patch_all()
def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen(1024)
    i = 0
    while True:
        cli, addr = s.accept()
        print(addr,i)
        gevent.spawn(handle_request, cli,i)
        i += 1

def handle_request(s,addr):
    try:
        while True:
            data = s.recv(1024)
            # print('client addr: ',addr)
            # print("recv:", data)
            s.send(data)
            if not data:
                s.shutdown(socket.SHUT_WR)

    except Exception as  ex:
        print(ex)
    finally:
        s.close()
if __name__ == '__main__':
    server(8001)