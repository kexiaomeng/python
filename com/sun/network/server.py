import socket
import threading
import time

def tcplink(sock, addr):
    print('accept a new connection form clent %s:%s...' %addr)
    sock.send(b'welcome hello world')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode("utf-8") == 'exit':
            print('exit')
            break
        else:
            print(data.decode("utf-8"))

        sock.send(('hello,%s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 8888))

s.listen(5)
print('start listen')

while True:
    sock, addr = s.accept()

    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


