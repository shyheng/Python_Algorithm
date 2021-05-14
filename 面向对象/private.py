class P(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__moy = 1000 # 两个下划线代表私有属性

    def get_moy(self):
        return self.__moy

    def set_moy(self,m):
        if type(m) != int:
            print("不对")
            return
        self.__moy = m


p = P('shy',12)


# 获取私有属性
# 1 直接获取
print(p._P__moy)

# 2 定义get和set方法
print(p.get_moy())
p.set_moy(100)
print(p.get_moy())
