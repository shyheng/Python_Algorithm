import sys

# sys.stdin 接收用户的输入
# sys.stdout 标准输出
# sys.stderr 错误输出

s_in = sys.stdin

while True:
    con = s_in.readline().rstrip('\n')
    if con == '':
        break
    print(con)