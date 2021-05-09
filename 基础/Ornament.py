# 装饰器
import time

def cal_time(fn):
    def inner():
        st = time.time()
        fn()
        end = time.time()
        print("运行时长",end-st)
    return inner

@cal_time
def dome():
    x = 0
    for i in range(1,50000000):
        x+=i
    print(x)
@cal_time
def foo():
    print('shy')
    time.sleep(3)
    print('zph')


dome()
foo()


