# 多态：故名思义就是多种状态、形态，就是同一种行为对于不同的子类【对象】有不同的行为表现
# 定义时的类型和运行时的类型不一样，此时就成为多态
# python不支持java和C#这一类强类型语言中多态的写法，但是原生多态，python崇尚“鸭子类型”，利用python伪代码实现Java和C#的多态
# 要想实现多态，必须的有两个前提需要遵守：
# 1、继承：多态必须发生在父类和子类之间
# 2、重写：子类重写父类的方法
# 多态有什么用
# 1、增加程序的灵活性
# 2、增加程序的扩展性
# If it looks like a duck, swims like a duck and quacks like a duck, it probably is a duck!
# 案例演示
class Animal:
    """
    父类【基类】
    """
    def say_who(self):
        print("我是一个动物...")
        pass
    pass
class Duck(Animal):
    """
    鸭子类【子类】 派生类
    """
    def say_who(self):
        """
        在这里重写父类的方法
        :return:
        """
        print('我是一只漂亮的鸭子')
        pass
    pass
class Dog(Animal):
    """
    小狗类【子类】 派生类
    """
    def say_who(self):
        """
        在这里重写父类的方法
        :return:
        """
        print('我是一只中华田园犬')
        pass
    pass
class Cat(Animal):
    """
    小猫类【子类】 派生类
    """
    def say_who(self):
        """
        在这里重写父类的方法
        :return:
        """
        print('我是一只波斯猫猫')
        pass
    pass

class Bird(Animal):
    """
    新增鸟类，无需要修改代码
    小鸟类【子类】 派生类
    """
    def say_who(self):
        """
        在这里重写父类的方法
        :return:
        """
        print('我是一只小小鸟')
        pass
    pass

def commonInvoke(obj):
    """
    统一调用的方法
    :param obj: 对象的实例
    :return:
    """
    obj.say_who()

lisObj=[Duck(),Dog(),Cat(),Bird()]
for item in lisObj:
    """
    循环调用函数
    """
    commonInvoke(item)

# 我是一只漂亮的鸭子
# 我是一只中华田园犬
# 我是一只波斯猫猫
# 我是一只小小鸟

# ducK1=Duck()
# ducK1.say_who()
# dog1=Dog()
# dog1.say_who()
# cat1=Cat()
# cat1.say_who()
# 我是一只漂亮的鸭子
# 我是一只中华田园犬
# 我是一只波斯猫猫