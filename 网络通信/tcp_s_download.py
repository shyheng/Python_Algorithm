import socket,os

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(('172.20.37.211',9000))
server_socket.listen(128)

client_socket,client_addr = server_socket.accept()

data = client_socket.recv(1024).decode('utf8')

# print(data)
if os.path.isfile(data):
    with open(data,'rb') as file:
        con = file.read()
        client_socket.send(con)
else:
    print('文件不存在')



server_socket.close()