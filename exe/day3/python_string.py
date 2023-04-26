# 序列: 在python当中 序列就是一组按照顺序排列的值[数据集合]
# 在python中 存在三种内置的序列类型:
# 字符串、列表、元组
# 优点:可以支持索引和切片的操作
# 特征:第一个正索引为0，指向的是左端，第一个索引为负数的时候，指向的是右端

# 切片：【高级特性】可以根据下表来获取序列对象的任意[部分]数据
# 语法结构：[start:end:step] step默认是1
# 切片是指截取字符串中的其中一段内容。切片使用语法[起始下标:结束下标:步长]
# 切片截取的内容不包含结束下标对应的数据，步长指的是隔几个下标获取一个字符。
# 注意：下标会越界，切片不会
# 1.capitalize() # 首字母变大写
# 2.endswith/starts with() # 是否x结束/开始
# 3.find()  #检测x是否在字符串中
# 4.isalnum() #判断是否是字母和数字
# 5.isalpha() #判断是否是字母
# 6.isdigit() #判断是否是数字'abc123'isdigit0
# 7islower()  #判断是否是小写
# 8.join()    #循环取出所有值用xx去连接
# 9.lower/up per #大小写转换
# 10.swapcase #大写变小写，小写变大写
# 11.lstrip/rstrip/strip#移除左/右/两侧空百
# 12.split() #切割字符串
# 13.title() #把每个单词的首字母变成大写
# 14.replace(old,new,count=None) #old被换字符串，new替换字符串count换多少个。无count表示全部替换。
# 15.count() #统计出现的次数

# test = 'python'
# print(type(test))
# print("第一个字符%s"%test[0])
# print("第二个字符%s"%test[1])
# for item in test:
#     print(item,end=' ')


# name='paper'
# print("姓名首字母转大写%s"%name.capitalize())
# print("姓名首字母转大写%s"%name.title())
# a100='  12  '
# b100=a100.strip()
# print("去掉两边的空格%s"%b100)
# print("去掉两边的空格%s"%a100.strip())
# print("去掉左边的空格%s"%a100.lstrip())
# print("去掉右边的空格%s"%a100.rstrip())
# # 复制字符串
# print("a100的内存地址%d"%id(a100))
# b101=a100 # 只是把a100对象的内存地址赋给了b101
# print("b100的内存地址%d"%id(b100))
# print("b101的内存地址%d"%id(b101))

# dataStr='I love python'
# print(dataStr.find('p')) # 7 fin 可以查找目标对象在序列对象中的的位置
# print(dataStr.find('o')) # 3
# print(dataStr.find('I')) # 0 序列对象从0开始
#
# print(dataStr.index('I')) # 0
# print(dataStr.index('v')) # 4 # index 检查字符串中是否包含子字符串，返回的是下标值
# # index如果没有找到对象的数据，便会报异常，而find函数不会，找不到返回-1
# print(dataStr.startswith("I")) # 开头是否为I
# print(dataStr.endswith("pI")) # 结尾是否为n,返回为True或者False
# print(dataStr.endswith("n"))
# print(dataStr.lower()) # 转换为小写
# print(dataStr.upper()) # 转化为大写

strMsg='hello world'
#slice [start:end:step]
print(strMsg) # 输出完整的数据
print(strMsg[0])
print(strMsg[2:5]) #llo 从第三个开始到第五个,左闭右开
print(strMsg[2:6]) #llo  从第三个开始到第五个,左闭右开,包含一个空格
print(strMsg[2:]) #llo world 从第三个开始到最后一个,左闭右开
print(strMsg[0:3]) #hel
print(strMsg[:3]) #hel
print(strMsg[::-1]) #dlrow olleh 倒叙输出,负号表示方向,从右边开始输出

