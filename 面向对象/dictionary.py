class P(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]


p = P("shy",12)
print(p.__dict__)
p['name'] = 'zph' # 调用__setitem__
p['age'] = 20
print(p.name,p.age)
print(p['name']) # 调用__getitem__