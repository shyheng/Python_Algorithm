import time


class P(object):
    # 调方法就用
    def __init__(self):
        print("--init--")

    def __del__(self):
        # 当对象销毁时调用
        print("--del")

    def __repr__(self):
        return 'hello'

    def __str__(self):
        return 'good'

    def __call__(self, *args, **kwargs):
        print("__call__")
        print('args={},kwargs={}'.format(args,kwargs))
        return kwargs['fn'](args[0],args[1])

p = P()
# del p  #这个方法也可以删除
time.sleep(10)

# 如果不做任何修改 直接打印，是文件的类型 和 内存地址
# 更改__repr__或者__str__其中一个
print(p)

n = p(1,2, fn=lambda x,y: x + y)
print(n)