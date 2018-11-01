import socket, threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0',9999))
s.listen(5)

def tcplink():
    sock, addr = s.accept()
    sock.send(b'Welcome!')
    while True:
        msg = sock.recv(1024)
        if msg.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s'%msg.decode('utf-8')).encode('utf-8'))

t = threading.Thread(target = tcplink, args = ())
t.start()
