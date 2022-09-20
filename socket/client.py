# %%
import socket
import datetime
import time
# %%
HOST = '127.0.0.1'
PORT = 8000


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
# client.sendall(clientMessage.encode())
num = 1

#current_time = datetime.datetime.now()
while True:
    clientMessage = f"num:{num}, client msg"
    current_time = datetime.datetime.now()
    serverMessage = str(client.recv(1024), encoding='utf-8')
    client.sendall(clientMessage.encode())
    time.sleep(1)
    time_diff = current_time - datetime.datetime.now()
    time_diff = time_diff.microseconds
    print(time_diff)

    print(f'Cast time: {time_diff} ms, Server:', serverMessage)
    num += 1
    # client.close()
