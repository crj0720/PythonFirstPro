print('hello python')
print('人生苦短，我用python')
print('一起加油吧！python')
# 变量如何定义和使用
# a就是变量的名字，对应一个盒子，里面装的数据就是10
a = 10
print(10) # 使用变量 先定义变量，才能够使用变量
# 变量是可以多次赋值的【在程序执行的过程中，值可以改变的量】
# 变量就是用来存储数据
print(type(a))

a = 10.23
print(type(a))
a = '陈仁杰'
print(type(a))
a = True
print(type(a))
a = () #tuple 元组
print(type(a))
a = [] # list 列表
print(type(a))
a = {} # dict 字典
print(type(a))



# 变量的命名规则
"""
1、变量必须以字母（a-z,A-Z）或者下划线（_）开头
2、其他字符可以是字母，数字或者_
3、变量区分大小写
4、Python关键字不能用作变量名
查看python关键字
>>> import keyword
>>> keyword.kwlist

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def'
, 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""
Name='刘德华'
_age='30'
name='周星驰'
# True = 123 # 不能这样定义 因为True是关键字
print(Name,_age,name)
"""
命名规范:
>见名知意，尽量使用有语义的单词命名。如使用password用作密码，username 用户名。
>小驼峰式命名法: 第一个单词首字母小写其他单词首字母大写，如userName
>大驼峰式命名法: 全部单词首字母都用大 写，如 UserName
>下划线命名法:每个单词用_下划线连接，如user_name
"""
computerAge = 11
ComputerName = 'lilei'
computer_age = 2



