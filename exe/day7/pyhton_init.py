# class People:
#     def __init__(self):
#         """
#         实例属性的声明
#         """
#         self.name='老李'
#         self.sex='男生'
#         self.age=18
#         pass
#
#     def eat(self): # self 默认参数
#         """
#         吃的行为
#         :return:
#         """
#         print("喜欢吃榴莲")
#
#     pass
#
# xq=People()
# xq.name='小溪'
# xq.sex='女神'
# xq.age=20
# xq.eat()
# print(xq.name,xq.sex,xq.age)
#
# # 喜欢吃榴莲
# # 小溪 女神 20
# xa=People() # 在创建新的对象时候，是自动执行init的
# xa.eat()
# # 如果有n个这样对象，被实例化，那么就需要添加很多次这样的属性了，显然是比较麻烦
# print(xa.sex)
# xa.sex='少男'
# print(xa.sex)
#
# # 男生
# # 少男
class People:
    def __init__(self,name,sex,age):
        """
        实例属性的声明
        """
        self.name=name
        self.sex=sex
        self.age=age
        pass

    def eat(self,food): # self 默认参数
        """
        吃的行为
        :return:
        """
        print(self.name+"喜欢吃"+food)

zp=People('照片','非男非女',9999)
print(zp.sex,zp.age,zp.name)
# 非男非女 9999 照片

zp1=People('照1片','非男非女',9999)
print(zp1.sex,zp1.age,zp1.name)
zp1.eat('南瓜子')
# 非男非女 9999 照1片
# 照1片喜欢吃南瓜子