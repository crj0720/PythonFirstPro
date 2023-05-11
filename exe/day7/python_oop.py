# 定义类和对象
# 类的结构 类名 属性 方法
# class 类名(object):
#     属性
#     方法类别

class Perple:
    """
    对应人的特征
    """
    # name='小明'
    """
    对应人的行为  实例方法
    """
    age=20
    def __init__(self):
        self.name1="小张" # 实例属性
    def eat(self):
        print("大口大口的吃饭")
        pass
    def run(self):
        print("飞快的跑")
        pass
    pass
# 创建一个对象【类的实例化】
# 对象名 = 类名()
xm=Perple()
xm.eat() # 调用函数
xm.run()
# print("{}的年龄是:{}".format(xm.name,xm.age))

# 大口大口的吃饭
# 飞快的跑
# 小明的年龄是:20
print("{}的年龄是:{}".format(xm.name1,xm.age))
# 小张的年龄是:20