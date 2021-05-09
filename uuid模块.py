# uuid用来生成一个全局唯一模块
import uuid

print(uuid.uuid1()) # 32个长度

# uuid3和uuid5是使用传入的字符串根据指定算法算出来的，是固定
print(uuid.uuid3(uuid.NAMESPACE_DNS,'shy')) # 生成固定的uuid
print(uuid.uuid5(uuid.NAMESPACE_DNS,'shy'))

print(uuid.uuid4()) #使用最多