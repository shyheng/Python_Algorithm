class P(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @staticmethod
    def dome():
        print("shy")


    @classmethod
    def clas(cls):
        print(cls.dome())
        print("yse")


P.dome()
P.clas()