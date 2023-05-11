# 序列操作函数 str 元组 list
# all()
# any()
# sorted()
# reverse()
# range()
# zip()
# enumerate()

# 空元组、空列表和0、false都为false
# all() 对象中的元素除了是0、空(None)、false外都算true
# print('---------all-------')
# print(all([]))
# print(all({}))
# print(all(()))
# print(all((1,2,3,False)))
# print(all((1,2,3,0)))
# print(all())

# any() # 全部为false 才会返回false,相当于any()
# print('---------any-------')
# print(any((1,2,3,0))) # True
# print(any(('',False))) # False
# print(any(('',False,0))) # False

# sorted
# print('---------sort-------')
# sort 与 sorted 区别：
# 1、sort是应用在list上的方法，sorted可以对所有可迭代的对象进行排序操作
# 2、list的sort方法返回的是对已经存在的列表进行操作，
# 而内建函数sorted方法返回的是对一个新的list，而不是在原有的基础上进行的操作
# 语法：
#     sorted(iterable[,cmp[,key[,reverse]]])
# 参数：
#     iterable --可迭代对象
#     cmp -- 比较的函数，这个具体有两个参数，参数的值都是从可迭代对象中取出，此函数必须
#     遵守的规则为，大于则返回1，小于则返回-1，等于则返回0
#     key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，
#     指定可迭代对象中的一个元素来进行排序
#     reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）
# 返回值：返回重新排序的列表
li = [2,3,42,32,34,56,1] # 列表格式
# li.sort() #list的排序方法,直接修改的是原始对象，永久排序
# print('排序之前：{}'.format(li))
# print(li.sort()) # None 元组下无法使用sort方法，因为元组无法修改
# varlist=sorted(li,reverse=True) # 降序排列
# print('排序之后：{}'.format(li))
# print('排序之后：{}'.format(varlist)) # [56, 42, 34, 32, 3, 2, 1]

# tupArray=(2,3,42,32,34,56,1) # 元组格式
# varRS=sorted(tupArray,reverse=False)
# print('排序之后：{}'.format(varRS)) # 升序排序  [1, 2, 3, 32, 34, 42, 56]


# reverse() 函数用于反向列表中元素
# 语法：list.reverse()
# 返回值：该方法没有返回值，但是会对列表的元素进行反向排序,数据位置完全颠倒过来

lis1 = [2,3,42,32,34,56,1] # 列表格式
# 错误用法
    # reList=li.reverse()
    # print(reList) # None
    # print(lis1.reverse()) # None
# print(lis1) # [1, 56, 34, 32, 42, 3, 2]

# range()函数可创建一个整数列表，一般用于在for循环中

# zip()函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组
# 组成的列表。
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用*号操作符，可以将元组解压为列表
# 就是用来打包的

s1=['a','b','v']
s2=[1,2,3,4,5,6]
print(zip(s1)) # print(zip(s1)) #
print(list(zip(s1))) # 想看原来的数值是怎么样的  [('a',), ('b',), ('v',)]
print(zip(s1,s2)) # <zip object at 0x000001C7EAF3B740>
print(list(zip(s1,s2))) # [('a', 1), ('b', 2), ('v', 3)]
zipList=zip(s2,s1)
print(list(zipList)) # [(1, 'a'), (2, 'b'), (3, 'v')]
# 如果可迭代对象的元素个数不一样，那么按照最少的那个迭代压缩最少元素进行可迭代对象结束后退出
def printBookInfo():
    """
    zip()函数的使用
    :return:
    """
    books=[] # 存储所有的图书信息
    id =input('请输入编号：每个项以空格分隔') # str
    bookName =input('请输入书名：每个项以空格分隔')
    bookPro =input('请输入位置：每个项以空格分隔')
    idList=id.split(' ')
    nameList=bookName.split(' ')
    bookList=bookPro.split(' ')

    bookInfo=zip(idList,nameList,bookList) # 打包处理
    for bookItem in bookInfo:
        """
        遍历图书信息进行存储
        """
        dictInfo={'编号':bookItem[0],'书名':bookItem[1],'位置':bookItem[2]}
        books.append(dictInfo) # 将字典对象添加到list容器中
        pass
    for item in books:
        print(item)

printBookInfo()
# 请输入编号：每个项以空格分隔1 2 3
# 请输入书名：每个项以空格分隔c1 c2 c3
# 请输入位置：每个项以空格分隔w1 w2 w3
# {'编号': '1', '书名': 'c1', '位置': 'w1'}
# {'编号': '2', '书名': 'c2', '位置': 'w2'}
# {'编号': '3', '书名': 'c3', '位置': 'w3'}