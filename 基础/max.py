# 编写一个行数求最大值
import random


def get_max(*args):
    x = args[0]
    for arg in args:
        if arg > x:
            x = arg
    return x


print(get_max(1, 2, 3, 4, 7, 5, 4, 3))

# 求摇骰子之和
def get_sum(n):
    m = 0
    for i in range(n):
        x = random.randint(1,6)
        m += x
    return m

print(get_sum(5))



