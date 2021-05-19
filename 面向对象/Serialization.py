# 序列化：将内存中存入硬盘
# 反序列化：将硬盘存入硬盘

# 使用json格式进行
import json
names = ['shy','zph']
x = json.dumps(names) # 将数据转换成字符串

file = open('zph','w',encoding='utf8')

json.dump(names,file) # 不用写write,直接写入

file.close()

# loads 将json字符串加载成Python文件
x = '{"name","age"}'
json.loads(x)

file1 = open('zph','r',encoding='utf8')
p = json.load(file)
print(p)
print(p[0])


