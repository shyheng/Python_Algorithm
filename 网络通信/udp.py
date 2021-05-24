import socket

# 1 创建socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 2 发送数据
s.sendto('hello'.encode('utf8'),('127.0.0.1',9000))

# 3 关闭数据
s.close()