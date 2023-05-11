# enumerate 函数用于将一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列，
# 同时列出数据和数据下标，一般用在for循环当中
listObj=['1','b','c']
# for item in enumerate(listObj,6):
#     print(item)
#     pass
# (0, '1')
# (1, 'b')
# (2, 'c')

# (6, '1')
# (7, 'b')
# (8, 'c')

dicObj={}
dicObj['name']='张三'
dicObj['age']='99'
dicObj['pro']='软件工程'
# print(dicObj)
for item in enumerate(dicObj):
    print(item[1])
# name
# age
# pro

for index,item in enumerate(dicObj):
    print(index)
    print(item)
