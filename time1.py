# 计算一段代码的执行速度---优化
import time

def cal_time(fn):
    st = time.time()
    fn()
    end = time.time()
    print('代码时间{}'.format(end-st))

def dome():
    x = 0
    for i in range(1,50000000):
        x+=i
    print(x)

cal_time(dome)

def foo():
    print('shy')
    time.sleep(3)
    print('zph')

cal_time(foo)
