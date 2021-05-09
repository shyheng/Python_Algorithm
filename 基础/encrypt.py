import hashlib
import hmac

# 加密模块 进行数据加密
# hashlib主要有两个加密算法 md5 和 sha
# 加密方式 单下加密 ：只有加密 不能被解密md5/sha

# 需要将加密的内容转换为二进制
x = hashlib.md5() #生成一个md5对象
x.update('abc'.encode('utf8'))
print(x.hexdigest())

h1 = hashlib.sha1('123456'.encode())
print(h1.hexdigest())

h2 = hashlib.sha224('123456'.encode()) # 224位 十六进制
print(h2.hexdigest())

h3 = hashlib.sha256('123456'.encode())
print(h3.hexdigest())

h4 = hashlib.sha384('123456'.encode())
print(h4.hexdigest())

# hmac 加密可以指定秘钥
h = hmac.new('h'.encode(),'hello'.encode())
result = h.hexdigest()
print(result)