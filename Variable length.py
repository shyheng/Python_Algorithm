# *args 表示可变位置参数
# **kwargs 表示可变的关键字参数

def add(a,b,*args,mul=1,**kwargs):
    # print('a = {},b = {}'.format(a,b))
    # print('args = {}'.format(args))
    print('kwagr ={}'.format(kwargs))
    c = a +b
    for arg in args:
        c += arg
    return c*mul

# def add(*args):
#     pass

# add()
print(add(1, 2, 4, 3, mul=2))
print(add(1, 2, 4, 3, mul=2,p=1,s=1))
