# 什么是集合？
# set是python中的一种数据类型，是一个无序且不重复的元素集合
# 不支持索引和切片，是一个无序的且不重复的容器
# 类似于字典 但是只有key 没有value
# 如何创建？
# 1、set1={"1","2"}
# 2、list1=['1','2','3','6']
# set2=set(list1)
# 函数
# add()
# clear()
# difference()
# intersection()
# union()
# pop()
# discard()
# update()

set1=["1","2"] # list
# print(type(set1))
t1={"1","2",1,2,3} # set
# print(type(t1))
# 添加操作
# t1.add('python')
# print(t1) # {'1', 'python', '2'}
# t1.add('python1')
# print(t1) # {'python1', '1', 'python', '2'}
# t1.add('python2')
# print(t1) # {'python2', '2', 'python1', 'python', '1'}
# t1.add('python3')
# print(t1) # {'python2', '2', 'python1', 'python3', 'python', '1'}
# 清空操作
# t1.clear()
# print(t1) # set()

# 取差集
set2={2,3,4}
# t1.difference(set2)
# print(t1) # {1, 2, 3, '2', '1'}
# print(t1.difference(set2))  # {1, '2', '1'}
# print(t1-set2)
# #  交集操作
# print(t1.intersection(set2)) # {2, 3}
# print(t1&set2)
# #  并集操作
# print(t1.union(set2)) # {1, 2, 3, '1', 4, '2'}
# print(t1 | set2)

# 移除数据
# pop集合pop随机移除某个元素并且获取那个参数，集合pop没有参数
# print(t1.pop()) # 1
# print(t1) # {2, 3, '2', '1'}
# print(t1.pop()) # 2
# print(t1) # {3, '2', '1'}
# # 指定移除
# print(t1.discard('1')) # None
# print(t1) # {3, '2'}

# 更新操作
t1.update(set2)
print(t1) # {1, 2, 3, '2', 4, '1'}



