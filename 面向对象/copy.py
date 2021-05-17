import os.path

file_name = input('输入一个路径:')

if os.path.isfile(file_name):
    # 打开旧文件
    old_file = open(file_name,'rb') # 二进制的文件方式读取

    names = os.path.splitext(file_name)
    new_file_name = names[0] + '.bak' + names[1]

    new_file = open(new_file_name,'wb')# 二进制方式进行写入

    while True:
        content = old_file.read()
        new_file.write(content)
        if not content:
            break

    new_file.close()
    old_file.close()

else:
    print('输入的文件不存在')