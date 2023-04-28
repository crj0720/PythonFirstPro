# 局部变量 就是在函数内部定义的变量：【作用域仅仅局限在函数的内部】
# 不同的函数 可以定义相同的局部变量，但是各自用各自的 不会产生影响
# 局部变量的作用：为了临时的保存数据 需要在函数中定义来进行存储
# --------------------全局变量------------------------------
# 全局变量，作用域不同
# 当全局变量和局部变量出现重复定义的时候，程序会优先执行函数内部定义的变量【地头蛇】
# 如果在函数的内部要向对全局变量进行修改的话，必须要使用global关键字进行声明，自它起始到结束，都是该变量
pro='计算机信息管理'
name='吴老师'
# 以下两个是局部变量
def printInfo():
    name='peter'
    print('{},{}'.format(name,pro))
    pass

def TesMethod():
    name='liudehua'
    print(name,pro)
    pass

def changeGlobal():
    """
    修改全局变量
    :return:
    """
    global pro
    pro="市场营销" #局部变量
    pass

changeGlobal()
TesMethod() # NameError: name 'name' is not defined
printInfo()
changeGlobal()
print(pro)
# print(changeGlobal())
