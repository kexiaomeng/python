import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #AF_INET表示ipv4协议，sock_stream表示面向流的tcp协议

s.connect(('www.baidu.com', 80))  #参数是一个tuple 包含地址和端口号

s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')

buffer = []

while True:
    d = s.recv(1024)

    if d:
        buffer.append(d)
    else:
        break


data = b''.join(buffer)


s.close()

header, html = data.split(b'\r\n\r\n',1)

print(header.decode("utf-8"))

print('\n')

print(html.decode("utf-8"))
with open('baidu.html', 'wb') as f:
    f.write(html)