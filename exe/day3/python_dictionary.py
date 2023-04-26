# 字典:也是python中重要的数据类型，字典是有 键值对 组成的集合，
# 通常使用键来访问数据，效率非常高，和list一样 支持对数据的添加、修改、删除
#
# 特点:
# 1. 不是序列类型 没有下标的概念，是一个无序的 键值集合，是内置的高级数据类型
# 2.用{}来表示字典对象，每个键值对用逗号分隔
# 3.键 必须是不可变的类型[元组、字符串] 值可以是任意的类型38
# 4.每个键必定是惟一的，如果存在重复的键，后者会覆盖前者

# 如何创建字典
dictA={} # 空字典

dictA['name']='李四' # key:value
dictA['age']='30' # key:value
dictA['pro']='软工' # key:value
dictA['school']='浙大' # key:value

# print(type(dictA))  # <class 'dict'>
print(dictA) # 输出完整的字典
# print(len(dictA)) # 数据项长度
# dictA['name']='王五'  # 修改键对应的值
# dictA['school']='安徽大学'  # 修改键对应的值
# print(dictA['name']) # 通过键获取对应的值

# # 获取所有的键
# print(dictA.keys()) # dict_keys(['name', 'age', 'pro', 'school'])
# # 获取所有的值
# print(dictA.values()) # dict_values(['李四', '30', '软工', '浙大'])
# # 获取所有的键值对
# print(dictA.items()) # dict_items([('name', '李四'), ('age', '30'), ('pro', '软工'), ('school', '浙大')])

# for item in dictA.items():
#     print(item)
    # ('name', '李四')
    # ('age', '30')
    # ('pro', '软工')
    # ('school', '浙大')

    # print(item,end=" ")
    # ('name', '李四')('age', '30')('pro', '软工')('school', '浙大')

#
# for key,value in dictA.items():
#     print('%s==%s'%(key,value))
    # name == 李四
    # age == 30
    # pro == 软工
    # school == 浙大

    # print(key+'=='+value)
    # name == 李四
    # age == 30
    # pro == 软工
    # school == 浙大
# dictA.update({'age':34}) # 更新操作 {'name': '李四', 'age': '30', 'pro': '软工', 'school': '浙大'}
# print(dictA)
# del dictA['name'] # 删除操作 {'age': 34, 'pro': '软工', 'school': '浙大'}
# print(dictA)
# dictA.pop('age') # 删除操作  {'pro': '软工', 'school': '浙大'}
# print(dictA)

# 如果排序
# 按照key排序
print(sorted(dictA.items(),key=lambda d:d[0]))
#[('age', '30'), ('name', '李四'), ('pro', '软工'), ('school', '浙大')]
# 按照values排序
print(sorted(dictA.items(),key=lambda d:d[1]))
# [('age', '30'), ('name', '李四'), ('school', '浙大'), ('pro', '软工')]