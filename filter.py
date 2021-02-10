# filter 过滤类
ages = [1,5,3,54,4,949,9]
# 第一个是函数，第二个是可迭代对象
# y 可迭代对象
y = filter(lambda x:x>5,ages)
# print(y)

# for u in y:
#     print(u)

adult = list(y)
print(adult)