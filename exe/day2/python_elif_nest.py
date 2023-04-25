"""
if-else的嵌套使用
"""
score = float(input("请输入你的学分"))  # 10.3这种的数据类型要选择float()
grade = int(input("请输入你的成绩"))
if score > 10:
    if grade>=80:
        print("你可以升班了..恭喜")
        pass
    else:
        print("很遗憾，你的成绩不达标")
        pass
    pass
else:
    print("你的表现也太差了吧...")