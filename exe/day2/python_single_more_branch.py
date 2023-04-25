
"""
单分支
if 条件表达式：比较运算符 逻辑运算符 符合的条件表达式
    代码指令
"""

score = 60
if score >= 60:
    print("恭喜你及格了")
    pass # 空语句
print('单分支语句执行结束')

"""
双分支
if 条件表达式：比较运算符 逻辑运算符 符合的条件表达式
    代码指令
else :
    代码指令
必定会执行其中一个
"""
if score<60:
    pass
else:
    print('成绩合格')
print('双分支语句执行结束')

"""
多分支
if 条件表达式：比较运算符 逻辑运算符 符合的条件表达式
    代码指令
elif 条件表达式 :
    代码指令
else :
特征：
1、只要满足其中一个分支，就会退出本层if语句结构【必然会执行其中一个分支】
2、至少有2种情况可以选择
elif 后面必须的写上条件和语句
else 是个选配，根据实际情况来填写
"""
score=int(input('请输入你的成绩'))
if score>90:
    print('优秀')
    pass
elif score>=80:
    print("中等")
    pass
elif score>=60:
    print("良")
    pass
else: # 选配
    print('成绩不合格')
print('多分支语句执行结束')

# 多分支的演练
# 猜拳小游戏
# 0：石头 1：剪刀 2：布
import random # 产生随机数的模块
people = int(input("请出拳：【0：石头 1：剪刀 2：布】"))
computer = random.randint(0,2)
print("计算机出拳%s",computer)
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




