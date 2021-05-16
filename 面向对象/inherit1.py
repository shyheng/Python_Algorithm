 # 面向对象编程有三大特性 ： 封装 继承 多态
 # 封装 ： 函数是对语句的赋值；类是对函数和变量的封装
 # 继承 ： 类和类之间可以认为手动的建立父子关系，父类的属性和方法，子类可以使用
 # 多态 ： 是一种技巧，提高代码的灵活度

class A(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '正在睡觉')


class B(object):
    def bark(self):
        print(self.name + '正在叫')

# 允许多继承
class C(A,B):
    def study(self):
        print(self.name + '正在好好学习')

# Dog() 调用__new__ 方法，在调用__init__ 方法
# Dog 里没有__new__ 方法，会查看父类是否重写 __new__方法
# 父类里也没有重写 __new__方法，查找父类的父类的找到object

#调用 __init__ 方法，Dog类没有实现，会自动找Animal父类
d1 = B('shy', 3)
print(d1.name) # 父类里定义的属性，子类可以直接使用
d1.sleep() # 父类的方法子类实例对象可以直接

