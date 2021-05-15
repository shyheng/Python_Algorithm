# 异常
try:
    print("_____________")

    f = open("test1.txt") # 打开一个不存在的文件

    print("_____________")

except (IOError,NameError) as r: # 需要找到相对应的异常名
    print("出现IO异常") # 当捕获到异常后执行的代码
    print(r) # 打印错误信息
finally:
    print("一定要执行的")
    f.close()




