# 1，一个函数做另一个函数的参数 lambda
# 2, 一个函数做另一个函数的返回值
# 3，函数内部定义一个函数

# 闭包的概念
def shy():
    n = 10
    def zph():
        # 内部函数如何修改函数内的局部参数
        nonlocal n
        n = 20
        m =20
        print('n={}',n)
    return zph

shy()()