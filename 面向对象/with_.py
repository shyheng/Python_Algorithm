# with关键字是文件自动关闭
# 称为上下文管理器 文件，socket连接和数据库连接 with自动关闭
try:
    with open('zph.csv','r',encoding='utf8') as file:
        file.read() # 不需要手动关闭 会自动关闭
except FileNotFoundError:
    print("找不到")

# 在对象上with 会调用__exit

class Deam:
    def __init__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __enter__(self):
        print('enter')

def p():
    return Deam()

# p().__enter__

if __name__ == '__main__':
    with p() as p:
        print(p)