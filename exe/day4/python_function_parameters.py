# 参数的分类：
# 必选参数、默认参数【缺省参数】、可选参数、关键字参数
# 参数：其实就是函数为了是实现某项特定的功能，进而为了得到实现功能所需要的数据
# 为了得到外部数据的

# 1、必选参数
def sumOfNumber(a,b): # 形式参数：只是意义上的一种参数，在定义的时候是不占内存地址的
    """
    这里是简单的加法运算
    :param a:
    :param b:
    :return:
    """
    sum=a+b
    print(sum)
    pass
# 函数的调用
# sumOfNumber(2,3) # 2 3 实际参数：实参，实实在在的参数，是实际占用内存地址的
# 在调用的时候必选参数 ，是必须要赋值的
# sumOfNumber(4)


# 2、默认参数【缺省参数】
def sumOfNumber2(a=20,b=30):
    """
    这里是简单的加法运算 缺省参数
    :param a:
    :param b:
    :return:
    """
    print("默认参数使用=%d"%(a+b))
    pass

# 默认参数调用
# sumOfNumber2() # 50 在调用的时候如果未赋值，就会用定义函数时给定的默认值
# sumOfNumber2(10) # 40
# sumOfNumber2(10,20) # 30
# sumOfNumber2(,20) # invalid syntax


# 3、可变参数（不定长参数），当参数的个数不确定时使用，比较灵活
def getComputer(*args):
    """
    计算累加和
    :param args:可变长的参数类型
    :return:
    """
    print("args参数有",args)
    result = 0
    for item in args:
        result += item
        pass
    print("result=%d"%result)
    pass
# 调用参数
getComputer(1,2,3,4,5,6,7) # args参数有 (1, 2, 3, 4, 5, 6, 7)
getComputer(1,2) # args参数有 (1, 2)
getComputer(1) # args参数有 (1,) 元组中只有1个的时候，只能加一个逗号进行区分


# 关键字可变参数
# ** 来定义
# 在函数体内 参数关键字是一个字典类型，key是一个字符串
def keyFunc(**kwargs):
    """
    关键字可变参数
    :param kwargs:
    :return:
    """
    print(kwargs)
    pass
# 调用
keyFunc() # {}
# keyFunc(1,2,3) # 不可以传递 TypeError: keyFunc() takes 0 positional arguments but 3 were given
dictA={'name': '李四', 'age': '30', 'pro': '软工', 'school': '浙大'}
# keyFunc(dictA) # TypeError: keyFunc() takes 0 positional arguments but 1 was given
keyFunc(**dictA) #
keyFunc(name='peter',age=26) #

def complexFunc(*args,**kwargs):
    """
    组合使用
    :param args:
    :param kwargs:
    :return:
    """
    print(args)
    print(kwargs)
    pass
complexFunc()
complexFunc(1,2,3,4)
complexFunc(1,2,3,4,name='alice',age=216)
complexFunc(age=216)

# def testMup(**kwargs,*args): # 不符合要求的
#     """
#     可选参数必须放到关键字可选参数之前
#     可选参数：接受的数据是一个元组类型
#     关键字可选参数：接受的数据是一个字典类型
#     :param kwargs:
#     :param args:
#     :return:
#     """
#     print(args)
#     print(kwargs)
#     pass



