# 自定义异常
# raise 可以抛出异常
class MyError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return print("错误")


password = input("输入密码")
m = 6
n = 12
if n <= len(password) <= m:
    print('密码正确')

else:
    raise MyError()
