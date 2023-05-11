# 属性：类属性和实例属性
# 类属性：就是类对象所拥有的属性
class Student:
    name='李明' # 属于类属性 就是student类对象所拥有的
    def __init__(self,age):
        self.age=age # 实例属性
        pass
    pass

Student.name='郭富城' # 通过类对象修改数据

lm=Student(18)
print(lm.name)# 通过实例对象去访问类属性
lm.name='刘德华' # 通过实例对象 对类属性进行修改，可以吗？ 答曰不可以，实例对象只有对类属性的使用权力，没有修改权力
print(lm.name)#

# print(lm.name)#

print(lm.age)# 通过实例对象去访问实例属性
print('---------------------------------')
print(Student.name) # 通过类对象 Student 去访问 类属性 name    类名.属性名的形似
# error
# print(Student.age) # 通过类对象 Student 去访问 实例属性
# AttributeError: type object 'Student' has no attribute 'age'
# 小结
# 类属性是可以 被类对象和实例对象共同访问使用
# 实例属性只能由实例对象所访问
# 所有实例对象的类对象指针指向同一类对象。实例属性在每个实例中独有一份，而类属性是所有实例对象共有一份。
