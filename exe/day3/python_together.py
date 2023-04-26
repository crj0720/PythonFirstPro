# 共有方法 + * in
# 字符串合并
strA='人生苦短'
strB='我用python'
print(strA+strB)
# 列表合并
listA=list(range(10))
listB=list(range(11,20))
print(listA+listB)
# 复制 *
print((strA+strB)*3)
print((listA+listB)*3)

# in 对象是否存在
print('生' in strA) # True
print('生s' in strA) # False
print('5' in listA) # False
print(5 in listA)  # True
print('生s' in listA) # False

dictA={'name':'peter'}
print("name" in dictA)  # True
