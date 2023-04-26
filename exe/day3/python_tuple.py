# 元组与列表类似，不同之处在于元组的元素不能修改。元组使用小括号，元组也是通过下标进行访问
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可
# 元组的内置方法count，统计元素在元组中出现的次数
# 元组的内置方法index 查找指定元素在元组中的下标索引

# 元组:是一种不可变的序列，在创建之后不能做任何的修改
# 1.不可变:
# 2.用 () 创建元组类型，数据项用逗号来分割
# 3.可以是任何的类型
# 4.当元组中只有一个元素时，要加上逗号，不然后解释器会当做整型来处理
# 5.同样可是支持切片操作

# 当元组中只有一个数据项的时候，必须要在第一个数据项后面加一个逗号
# tupleC=('a',)   # <class 'tuple'>
# tupleD=('a')    # <class 'str'>
# print(type(tupleC))
# print(type(tupleD))

tupleA=() #空元组
print(id(tupleA))
tupleA=('aaca',98.2,12,'peter',[123,12,33])
# print(type(tupleA))
# print(tupleA)
# 不能修改

# 元组的查询
# for item in tupleA:
#     print(item,end=" ")

# print(tupleA[2]) # 12
# print(tupleA[2:4]) # (12, 'peter')
# print(tupleA[::-1]) # ([123, 12, 33], 'peter', 12, 98.2, 'aaca')
# print(tupleA[::-2]) # ([123, 12, 33], 12, 'aaca') 每隔两个取一个，反转字符串
# print(tupleA[::-3]) # ([123, 12, 33], 98.2) 每隔三个取一个，反转字符串
# print(tupleA[::-6]) # ([123, 12, 33],) 每隔六个取一个，反转字符串

# print(tupleA[-2:-1:]) # ('peter',) 倒着取下标 为-2 到 -1 区间的
# print(tupleA[-4:-1:]) # (98.2, 12, 'peter') 倒着取下标 为-4 到 -1 区间的

# # # # tupleA[0]='qwe' # TypeError: 'tuple' object does not support item assignment
# tupleA[4][0]=23 # 元组下的列表类型的数据进行修改，不可以对元组中其他数据类型不可以进行修改
# print(tupleA)
# print(type(tupleA[4][0])) # <class 'int'>
# print(type(tupleA[4]))      #  <class 'list'>

tupleE=(1,2,3,4,3,2,4,5,2,1)
print(tupleE.count(1)) # 2  可以统计出现元素出现的次数
print(tupleE.count(4))
print(tupleE.count(3))

