# 计算一段代码的执行速度
import time
# 获取时间
x = 0
st = time.time()

print(st)
for i in range(1,50000000):
    x+=i

print(x)

end = time.time()

print(end)

print('代码时间{}'.format(end-st))

