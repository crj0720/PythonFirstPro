"""
循环的分类：while \ for
while 语法结构
while 条件表达式：
    代码指令
语法特点：
1、有初始值
2、条件表达式
3、变量【循环体内计数变量】的自增或者自减，否则会造成死循环
使用条件：循环的次数不确定，是依靠循环条件来结束
目的：为了将相似或者相同的代码操作变得更加简洁，使得代码可以重复利用

"""

"""
# 输出1到100的数据
index = 1
while index<=100:
    print(index)
    index+=1
    pass
# 玩4局猜拳
import random # 产生随机数的模块
count=1
while count<=4:
    # people = int(input("请出拳：【0：石头 1：剪刀 2：布】"))
    people = random.randint(0,2)
    computer = random.randint(0,2)
    print("人类出拳：",people)
    print("计算机出拳：",computer)
    if people==0 and computer==1 :
        print("恭喜你，你赢了")
        pass
    elif people==1 and computer==2 :
        print("恭喜你，你赢了")
        pass
    elif people == 2 and computer == 0:
        print("恭喜你，你赢了")
        pass
    elif people == computer :
        print("差一点点，是平局")
        pass
    else :
        print("好可惜，我赢了")
    count+=1
    pass
# 打印九九乘法表
row = 1
print(type(row))
while row <= 9:
    col = 1
    # print(type(col))
    while col <= row:
        print("%d*%d=%d"%(row, col, row*col),end=" ")
        col+=1
        pass
    print()
    row+=1
    pass

# 1*1=1 
# 2*1=2 2*2=4 
# 3*1=3 3*2=6 3*3=9 
# 4*1=4 4*2=8 4*3=12 4*4=16 
# 5*1=5 5*2=10 5*3=15 5*4=20 5*5=25 
# 6*1=6 6*2=12 6*3=18 6*4=24 6*5=30 6*6=36 
# 7*1=7 7*2=14 7*3=21 7*4=28 7*5=35 7*6=42 7*7=49 
# 8*1=8 8*2=16 8*3=24 8*4=32 8*5=40 8*6=48 8*7=56 8*8=64 
# 9*1=9 9*2=18 9*3=27 9*4=36 9*5=45 9*6=54 9*7=63 9*8=72 9*9=81 



row = 9
print(type(row))
while row >= 1:
    col = 1
    # print(type(col))
    while col <= row:
        print("%d*%d=%d"%(row, col, row*col),end=" ")
        col+=1
        pass
    print()
    row-=1
    pass

# 9*1=9 9*2=18 9*3=27 9*4=36 9*5=45 9*6=54 9*7=63 9*8=72 9*9=81 
# 8*1=8 8*2=16 8*3=24 8*4=32 8*5=40 8*6=48 8*7=56 8*8=64 
# 7*1=7 7*2=14 7*3=21 7*4=28 7*5=35 7*6=42 7*7=49 
# 6*1=6 6*2=12 6*3=18 6*4=24 6*5=30 6*6=36 
# 5*1=5 5*2=10 5*3=15 5*4=20 5*5=25 
# 4*1=4 4*2=8 4*3=12 4*4=16 
# 3*1=3 3*2=6 3*3=9 
# 2*1=2 2*2=4 
# 1*1=1 


# 打印直角三角形
row1 = 1
while row1 <= 7:
    j=1
    while j<=row1:
        print("*",end=" ")
        j+=1
        pass
    print() # 换行
    row1+=1
    pass
# 改造 方向相反的直角三角形

row1 = 7
while row1 >= 1:
    j=1
    while j<=row1:
        print("*",end=" ")
        j+=1
        pass
    print() # 换行
    row1-=1
    pass

# 打印一个等腰三角形
row2=1
while row2<=5:
    j2=1
    while j2<=5-row2:
        print(' ',end='')
        j2+=1
        pass
    k2=1
    while k2<=2*row2-1:
        print('*',end='')
        k2+=1
        pass
    print()
    row2+=1
    pass
"""


# for 循环
#语法特点:遍历操作，依次的取集合容器中的每个值
# for 临时变量 in 容器:执行代码块#tags='我是一个中国人’#字符串类型本身就是一个字符类型的集合
# for item in tags:
#     print(item)
#     pass
# range 此函数可以生成一个数据集合列表
# range(起始:结束:步长) 步长不能为0
# sum = 0
# for data in range(1,11): # 左边包含右边不包含
#     sum+=data # 求累加和
#     print(data,end=' ')
#     pass
# print("sum%d:"%sum)
# print('-------------for------------')
# for data in range(50,201):
#     if data%2==0:
#         print("%d是偶数"%data)
#         pass
#     else:
#         print("%d是奇数"%data)

# break 退出循环，中断结束的意思
# continue 跳过本次循环，继续的进行下次循环（当continue的条件满足的时候，本次循环剩下的语句将不再执行，后面的循环继续）
# 这两个关键字只能用在循环中








