# 匿名内部类

def cacl(x,y,fn):
    c = fn(x,y)
    return c

x1 = cacl(1,2,lambda x,y:x+y)
x2 = cacl(4,2,lambda x,y:x-y)
x3 = cacl(1,2,lambda x,y:x*y)

print(x1)
print(x2)
print(x3)