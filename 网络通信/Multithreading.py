# 多线程
import threading


def swing():
    for i in range(50):
        print('在干嘛')


def dun():
    for i in range(50):
        print("滚")

t1 = threading.Thread(target=swing) # 创建一个线程
t2 = threading.Thread(target=dun) # 创建一个线程

t1.start()
t2.start()