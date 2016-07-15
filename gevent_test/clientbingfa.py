import socket,gevent,time
i = 1

def client1(i):
    HOST = 'localhost'    # The remote host
    PORT = 8001           # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    x = 0
    while x < 2:
        #msg = bytes(input(">>:"),encoding="utf8")
        msg = bytes('%s,%s'%(i,x),encoding='utf8')
        s.sendall(msg)

        data = s.recv(1024)
        #print(data)

        print('Received', repr(data))
        x += 1
        gevent.sleep(0.01)
gevent.joinall([gevent.spawn(client1, i) for i in range(1025)])
    #s.close()
# x =100000
# a = 1024
# b = x // a
# c = x % a
# m = 1
# while m <= b:
#
#     gevent.joinall([gevent.spawn(client1, i) for i in range(1023)])
#     m += 1
#     print(m)


