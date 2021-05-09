from functools import reduce

# reduce 是一个内置函数类
ages = [1,5,3,54,4,949,8]
print(reduce(lambda e1, e2: e1 + e2, ages))

studet = [
    {'cj':50,'name':'zph'},
    {'cj':60,'name':'p'},
    {'cj':70,'name':'shy'}
]

print(reduce(lambda x, y: x + y['cj'], studet, 0))