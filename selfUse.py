class S(object):
    __slots__ = ('x','y','name') # 元组 规定可以存的属性
    def __init__(self,x,y):
        self.x = x
        self.y = y

s1 = S("x","y")

print(s1.x)

# 动态属性
s1.name = 'shy'
print(s1.name)