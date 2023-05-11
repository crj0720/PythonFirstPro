class shenxian:
    def fly(self):
        print('神仙都会飞')

    pass

class Monkey:
    def chitao(self):
        print('猴子喜欢吃桃子')
    pass

class Sunwukong(shenxian,Monkey):
    pass

swk=Sunwukong()
swk.fly()
swk.chitao()
# 神仙都会飞
# 猴子喜欢吃桃子
# 问题是 当多个父类存在相同方法的时候，应该调用哪一个
class D(object):
    def eat(self):
        print('D.eat')
        pass
    pass
class C(D):
    # def eat(self):
    #     print("c.eat")
    #     pass
    pass
class B(D):
    pass
class A(B,C):
    def eat(self):
        print("A.eat")
        pass
    pass

a=A()
a.eat()
print(A.__mro__)
# 在执行eat方法时，查找方法的顺序是
# 首先在A里面去查找， 如果A中没有，则继续去B类中去查找，如果B中没有，则去C中查找
# 如果C类中没有，则去D类中去查找，如果在D类中没有的话，则报错
# c.eat

# 所谓重写，就是子类中，有一个和父类相同名字的方法，在子类中的方法会覆盖掉父类中同名的方法
# 为什么要重写，父类的方法已经不满足子类的需要，那么子类就可以重写父类或者完善父类的方法
class Dog:
    def __init__(self,name,color):
        self.name1=name
        self.color1=color
    def bark(self):
        print('旺旺叫....')
        pass
    pass
class kjq(Dog):
    def __init__(self,name,color):
        # Dog.__init__(self,name,color) # 调用父类得方法了 执行完毕就可以具备name,color这两个实例属性了
        super().__init__(name,color) # super()是自动找到父类，进而调通方法
        self.height=90
        self.weight=200
        pass
    def __str__(self):
        return '身高：{}，体重：{}'.format(self.height,self.weight)
    def bark(self):
        super().bark() # 调用父类的方法，然后再调用子类的方法
        print('叫得跟神一样....')
        print(self.name1,self.color1)
        pass
    pass

kj=kjq('cc','red')
kj.bark()
print(kjq.__mro__)
print(kj)
# 身高：90，体重：200