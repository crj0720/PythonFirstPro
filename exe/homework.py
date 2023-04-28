#
# 猜年龄小游戏，有三点需求
# 1许用户最多尝试3次
# 2.每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y， 就继续让其猜3次，以此o往复，如果回答N或n，就退出程序
# 3.如何猜对了，就直接退出
#
# 小王身高1.75，体重80.5kg。请根据BMI公式(体重除以身高的平方)帮小王计算他的BMI指数，并根据BMI指数:
# 低于18.5      过轻
# 正常18.5-25   正常
# 25-28        过重
# 28-32        肥胖
# 高于32        严重肥胖
# 用if-elif判断并打印结果

# 写函数，接收n个数字，求这些参数数字的和
# 写函数，找出传入的列表或元组的奇数位对应的元素，并返回一个新的列表
# 写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。PS:字典中的value只能是字符串或列表

def sumFunc(*args):
    # 处理接收的数据
    result=0
    for item in args:
        result+=item
        pass
    return result
    pass
# 调用
rs=sumFunc(1,2,3,43,32,2)
print('rs={0}'.format(rs)) # format 格式化输出


def proFunc(con):
    """
    处理列表数据
    :param con: 接收的是一个列表或者元组
    :return: 新的列表对象
    """
    listNew=[]
    index=1
    for i in con:
        if i%2==1: # 判断奇数位
            listNew.append(i)
            pass
        index+=1
        pass
    return listNew
    pass
rs3=proFunc([1,2,3,4,5,6,7])
print('rs3={0}'.format(rs3)) # format 格式化输出

rs4=proFunc(tuple(range(10,30)))
print(rs4)
print('rs4={0}'.format(rs4)) # format 格式化输出

rs5=proFunc(tuple(range(10,30)))
print(rs5)
print('rs3={0}'.format(rs5)) # format 格式化输出

def dictFunc(dicParms): # **kwargs
    """
    处理字典类型的数据
    :param dicParms: 字典
    :return:
    """
    result1={} # 空字典
    for key,value in dicParms.items():
        if len(value)>2:
            result1[key]=value[:2] # 向字典去添加数据
            pass
        else:
            result1[key]=value
            pass
        pass
    return result1
    pass

# 函数调用
dictA={'name': '李四666', 'age': '30999', 'pro': '软工工程', 'school': ['浙大11','北22大','a1n11da']}

print(dictFunc(dictA))