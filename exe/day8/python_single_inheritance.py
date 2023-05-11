class Animal:
    def eat(self):
        """
        吃
        :return:
        """
        print('吃')
        pass
    def drink(self):
        """
        喝
        :return:
        """
        print('喝')
        pass
    def run(self):
        """
        跑
        :return:
        """
        print('跑步了')
        pass

class Dog(Animal): # 继承了Animal父类 此时dog就是子类
    def wwj(self):
        print("小狗旺旺叫")
    pass
class Cat(Animal):
    def mmj(self):
        print("小猫喵喵叫")
    pass

d1=Dog()
d1.eat() # 具备了吃的行为 是继承了父类的行为
d1.wwj()
print('*'*40)
c1=Cat()
c1.drink()
c1.mmj()