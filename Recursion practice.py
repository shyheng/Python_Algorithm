# 使用递归求n
def facoto(n):
    if n == 0:
        return 1
    return n*facoto(n-1)
print(facoto(3))

# 使用递归求斐波那契数列的第n个数
def fi(n):
    if n == 1 or n == 2:
        return 1
    return fi(n-2)+fi(n-1)


print(fi(9))