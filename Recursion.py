conunt =0

def text():
    global conunt
    conunt+=1
    print("text")
    print("shy")
    print("zph")
    print("java")

    if conunt < 5:
        text()
text()

#求1到n的和
def get_sum(n):
    if n == 0:
        return 0
    return n+get_sum(n-1)

print(get_sum(9))