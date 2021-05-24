# udp接受数据
import socket
# 1 创建socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 2 绑定端口和ip地址
s.bind(('127.0.0.1',9000))

# 接收数据
data,addr = s.recvfrom(1024)
print(addr[0],addr[1],data.decode('utf8'))

# 关闭数据
s.close()
