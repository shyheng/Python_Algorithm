# os模块 操作系统的模块
import os

print(os.name)# 操作系统的名字
print(os.sep)#分隔符
print(os.path.abspath('if.py'))# 获取文件的绝对路径
print(os.path.isdir('Lib'))# 判断是否 是文件夹
print(os.path.isfile('if.py'))# 判断是否 是文件
print(os.path.exists('filter.py'))# 判断文件 是否存在

file_name = '2020.2.20.dome.py'
# print(file_name.rpartition('.'))
print(os.path.splitext(file_name))# 获取文件后缀名
print(os.environ)# 查看系统所有配置
print(os.environ.get('PATH'))# 查看PATH所有配置



