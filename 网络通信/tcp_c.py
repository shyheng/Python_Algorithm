# tcp客服端
import socket
# 1 创建
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2 连接服务器
    s.connect(('127.0.0.1',9000))
    s.send('hello,java'.encode('utf8'))
    s.close()

