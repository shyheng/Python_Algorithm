class A(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃东西')

    def __test(self):
        print('私有方法')


class P(A):
    pass

p = P("shy",18)
print(p.name)
p.eat()
p._A_test()