# 继承的特点 如果一个类A继承子类B 由类A创建出来的实例对象直接在B类用

class P:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '正在睡觉')

class S(P):

    def __init__(self,name,age,school):
        # 1 使用super直接调用父类飞
        super(S, self).__init__(name,age)
        self.school = school


    def stud(self):
        print(self.name + '正在学习')

    def sleep(self):
        print(self.name + '正在上课睡觉')


s = S("shy",20)
s.sleep()