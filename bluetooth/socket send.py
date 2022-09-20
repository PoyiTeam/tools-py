import socket
import time
device_addr = '98:D3:41:FD:72:AF'
port = 1  # Normal port for rfcomm?
buf_size = bytes(8)

sock = socket.socket(socket.AF_BLUETOOTH,
                     socket.SOCK_STREAM,
                     socket.BTPROTO_RFCOMM)
sock.setsockopt(socket.SOL_SOCKET,
                socket.SO_SNDBUF,
                buf_size)
sock.connect((device_addr, port))
data = 'h_+00'
while True:
    time.sleep(0.2)
    sock.send(data.encode())
