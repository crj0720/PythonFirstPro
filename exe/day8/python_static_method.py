class People:
    country='china'
    # 类方法 用classmethod类进行修饰
    @classmethod #
    def get_country(cls):
        return cls.country # 访问类属性
        pass
    pass

    @classmethod
    def change_country(self,data):
        self.country=data  # 修改类属性的值 在类方法中
        pass
    pass

    # 静态方法
    @staticmethod
    def getData():
        return  People.country # 通过类对象去引用
        pass

    @staticmethod
    def add(x,y):
        return  x+y
        pass

print(People.add(10,56)) # 带有参数的静态方法

print(People.get_country())
p=People()
print(p.getData())  # 注意 一般情况下 我们不会通过实例对象去访问静态方法
# print(People.get_country()) # 通过类对象去引用
# p=People()
# print('实例对象访问{}'.format(p.get_country))
# print('实例对象访问{}'.format(p.get_country()))
# # china
# # 实例对象访问<bound method People.get_country of <class '__main__.People'>>
# # 实例对象访问china
# print('--------------修改之后---------------------')
# People.change_country('英国')
# print(People.get_country()) # 通过类对象去引用

# 为什么要是用静态方法呢
# 由于静态方法主要来存放逻辑性的代码，本身和类以及实例对象没有交互，也就是说，在静态方法中，不会设计到类中方法和属性的操作
# 数据资源能够得到有效的充分利用

# demo 返回当前的系统时间
import time # 引入第三方的时间模块
class TimeTest:
    def __init__(self,hour,min,second):
        self.hour=hour
        self.min=min
        self.second=second

    @staticmethod
    def showTime():
        return time.strftime('%H:%M:%S',time.localtime())
        pass

print(TimeTest.showTime())
t=TimeTest(2,10,15)
print(t.showTime()) #没有必要通过实例返回静态方法