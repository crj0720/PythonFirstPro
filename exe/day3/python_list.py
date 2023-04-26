# list python当中非常重要的数据结构,是一种有序的数据集合
# 特点:
# 1.支持增删改查
# 2.列表中的数据是可以变化的[数据项可以变化,内存地址不会改变]
# 3.用[]来表示列表类型,数据项之间用逗号来分割,注意:数据项可以是任何类型的数据
# 3.支持索引和切片来进行操作
# 常见方法:
# append      在列表后面追加元素
# count       同级元素出现的次数
# extend      扩展,相当于批量添加
# index       获取指定元素索引号
# insert      在指定位置插入
# pop         删除最后一个元素
# remove      移除左边找到的第一个元素
# reverse     反转列表
# sort        列表排序;reverse=True

# li = [] # 空列表
# li = [1,2,3,'你好']
# print(type(li))
# print(len(li)) # len可以获取到列表对象中的数据个数
# print(li.count(1)) # count()可以获取到列表对象中的某个元素的个数
# 查找
listA=['abs',278,38,293.2,True]
# print(listA) #输出完整的列表 ['abs', 278, 38, 293.2, True]
# print(listA[0]) #输出第一个元素 abs
# print(listA[1:2]) #输出第二个元素 [278]
# print(type(listA[1:2])) #输出第二个元素 [278] <class 'list'>
# print(type(listA[1])) #输出第二个元素 278 <class 'int'>
# print(listA[1:3]) #输出第二个元素到第三个元素 [278, 38]
# print(listA[2:]) #输出第二个元素到最后一个元素 [38, 293.2, True]
# print(listA[::-1]) # 负数从右边向左边输出 [True, 293.2, 38, 278, 'abs']
# print(listA*2) # 输出多次数据【复制】  ['abs', 278, 38, 293.2, True, 'abs', 278, 38, 293.2, True]
# print(listA-list(1))


print('--------------增加-----------------')
# print('追加之前',listA)
# listA.append(99)
# listA.append([12,'23sf'])
# print('追加之后',listA)
# listA.insert(1,'这个我刚插入的数据') # 第二个位置插入新的数据
# print(listA)
# print(list(range(10)))
# rsData=list(range(5)) # 强制转换为list对象
# listA.extend(rsData) # 扩展 等于批量添加
# listA.extend([1,2,2.3,1]) # 扩展 等于批量添加
# print(listA)
# print('--------------修改-----------------')
# print('修改之前',listA)
# listA[0]='alice'
# print('修改之后',listA)
# print('--------------删除-----------------')
listB=list(range(5,10))
print('删除之前',listB) # 删除之前 [5, 6, 7, 8, 9]
# del listB[0]
# print('删除之后',listB) # 删除第一个元素 删除之后 [6, 7, 8, 9]
# del listB[1:3]# 批量删除多项数据
# print('删除之后',listB) # 删除第一个元素 删除之后 [6, 9]
# listB.remove(5) # 移除指定元素，具体的数据值 比如要移除元素5， 移除之后 [6, 7, 8, 9]
# listB=listB*2 # 移除之后 [6, 7, 8, 9, 6, 7, 8, 9]
# print('移除之后',listB)
# listB.remove(1)  # list.remove(x): x not in list
# listB.remove(6,7)  # 移除多个元素不可以
# listB.remove(7)  # 移除之后 [6, 8, 9, 6, 7, 8, 9] 若相同元素在一个列表中，只会移除第一个元素
# print('移除之后',listB)
# listB.pop(1) # 移除指定的项 参数是索引值 移除之后 [6, 9, 6, 7, 8, 9]
# print('移除之后',listB)

print(listB.index(8)) # 3  元素8，在列表中位于第四个位置，索引下标是3
print(listB.index(7,0,6)) # 2  index(查找元素，起始查找索引下标，结束索引下标)
print(listB.index(7,5,19)) # 查找元素不在查找索引下标的范围内，会报错   7 is not in list侧