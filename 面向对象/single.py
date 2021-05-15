# 单列模式
class single:
    __isinstance = None
    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.__isinstance is None:
            # 申请内存，创建一个对象类型设置为cls
            cls.__isinstance = object.__new__(cls)
        return cls.__isinstance

    def __init__(self,name,age):
        self.name = name
        self.age = age

