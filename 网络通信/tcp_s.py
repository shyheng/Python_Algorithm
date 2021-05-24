# tcp服务器
import socket

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('127.0.0.1',8888))
    s.listen(128)
    c_socket, c_addr = s.accept()  # 接收到一个元组
    while True:
        # print(c_addr[0], c_addr[1])  # 地址
        data = c_socket.recv(1024).decode(encoding='utf8')
        print(data)


