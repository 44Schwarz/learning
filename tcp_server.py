import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 2222))
s.listen(10)

# Single client
while True:
    print('Start listening')
    conn, addr = s.accept()
    while True:
        print('Connection is established')
        data = conn.recv(1024)
        if not data or data == b'close':
            break
        print('Received data:', data)
        conn.send(data)
    conn.close()

# Multiple clients
# while True:
#     conn, addr = s.accept()
#     pid = os.fork()  # Unix-only
#     if pid == 0:
#         data = conn.recv(1024)
#         if not data or data == b'close':
#             break
#         print('Received data:', data)
#         conn.send(data)
#         conn.close()
#     else:
#         conn.close()
