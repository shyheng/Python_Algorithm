import pickle
# 序列化 dump Python文件转二进制
# 反序列化 load 二进制转Python

names = ['shy','zph']
a = pickle.dump(names)
print(a)

file = open('name','wb')
file.write(a)
file.close()

file1 = open('name','rb')
x = file1.read()
y = pickle.load(x)
print(y)
file1.close()





