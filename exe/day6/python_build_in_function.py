# 3159页数
# builtins.py 里面有很多内置函数的方法，将所有的方法进行整理和疏通，切记切记
# 求绝对值
print(abs(-12))
# 求近似值
print(round(3.66,1))
print(round(3.66))
# 求次方
print(pow(3,3)) # 3的3次方
print(3**3)
# 最大值、最小值  可以是列表也可以是参数
print(max([1,2,2,3,4,5,6]))
print(max(11,2,2,3,4,5,6))

# sum(iterable[,start])
# iterable--可以是迭代对象如列表、元组、集合
# start--可以是指定参数，如果没有设置这个值，默认是0
print(sum(range(10),3))# 这里的3 是在求和的基础之上再加上3 比如原来是45，现在是48

# eval 执行表达式,可以是字符串
a,b,c=1,2,3
print('动态执行的函数={}'.format(eval('a+b+c-30'))) # 6
def TestFun():
    print('我执行了吗')
eval("TestFun") # 没有执行
eval("TestFun()") # 可以调用函数执行
