# 写入内存
from io import StringIO

s_io = StringIO()
s_io.write('hello') # 写成缓存存入内存

print(s_io.getvalue())


