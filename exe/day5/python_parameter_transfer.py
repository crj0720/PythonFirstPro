a=1 # 不可变类型
def func(x):
    print('x的地址：{}'.format(id(x)))
    x=2
    print('x的地址修改之后：{}'.format(id(x)))
    pass

# 调用函数
print('a的地址：{}'.format(id(a)))
func(a)

# 可变类型
li = []
def testRenc(parms):
    print(id(parms))
    li.append([1,2,2,4])
    pass
print(id(li))
testRenc(li)
print(li)

# 小结
# 1.在python当中， 万物皆对象，在函数调用的时候，实参传递的就是对象的引用
# 2.了解了原理后，就可以更好的去把控 在函数内部的处理是否会影响到函数外部的数据变化
# 参数传递是通过对象引用来完成
