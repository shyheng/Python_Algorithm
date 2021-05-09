class S(object):
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height

    def run(self):
        print("run")

    def eat(self):
        print("eat")

# 创建两个实例对象
s1 = S('shy',18,1.17)
s2 = S('zph',17,1.64)

# 使用实例对象的方法
s1.run()
s2.eat()