class People:
    country='china'
    # 类方法 用classmethod类进行修饰
    @classmethod #
    def get_country(cls):
        return cls.country # 访问类属性
        pass
    pass

    @classmethod
    def change_country(cls,data):
        cls.country=data  # 修改类属性的值 在类方法中
        pass
    pass

print(People.get_country()) # 通过类对象去引用
p=People()
print('实例对象访问{}'.format(p.get_country))
print('实例对象访问{}'.format(p.get_country()))
# china
# 实例对象访问<bound method People.get_country of <class '__main__.People'>>
# 实例对象访问china
print('--------------修改之后---------------------')
People.change_country('英国')
print(People.get_country()) # 通过类对象去引用

