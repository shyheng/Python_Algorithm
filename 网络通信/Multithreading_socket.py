import socket
import threading

if __name__ == '__main__':

    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(('172.20.38.79',8080))

    def w():
        while True:
            i = input('输入')
            s.sendto(i.encode('utf8'),('172`.20.38.79',9090))

    def r():
        while True:
            data,addr = s.recvfrom(1024)
            print(data)

t1 = threading.Thread(target=w)
t2 = threading.Thread(target=r)

t1.start()
t2.start()

