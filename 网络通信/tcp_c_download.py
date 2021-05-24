import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect(('172.20.37.211',9000))

flie_name = input('请输入要下载文件名')
client_socket.send(flie_name.encode('utf8'))

with open(flie_name,'wb') as file:
    while True:
        con = client_socket.recv(1024)
        if not con:
            break
        file.write(con)

client_socket.close()