class Person:
    def __init__(self,pro):
        """

        :param pro:专业
        """
        self.pro=pro
        pass
    """
    定义类
    """
    def eat(a,name,food):
        """
        实例方法
        :return:
        """
        # print('self=%s',id(self))
        # print(self)
        print("%s 喜欢 %s,他的专业是%s"%(name,food,a.pro))
        pass

    pass

xw=Person('软工')
print('xw=%s',id(xw))
# xw=%s 1961916404624
# self=%s 1961916404624
# xw.eat()
# <__main__.Person object at 0x00000192EEDE9390>
# xw.pro('软工')
xw.eat('小微','李兰')
# 小微 喜欢 李兰
# 小微 喜欢 李兰,他的专业是软工