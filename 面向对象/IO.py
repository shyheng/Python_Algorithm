f = open("test.txt","r") # 打开文件

# f.write("python")

# con = f.read(5) # 读5个字符
# con = f.readlines() # 列表的方式打印全部

# i = 1
# for temp in con:
#     print("{},{}".format(i,temp))
#     i += 1


con = f.readline() #读一行
print(con)


f.close() # 关闭文件
