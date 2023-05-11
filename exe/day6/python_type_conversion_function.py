# 类型转化函数
# int()
# float()
# str()
# ord()
# chr()
# bool()
# bin()数字转字符
# hex()
# oct()
# list()
# tuple()
# dict()
# bytes()


# 十进制转二进制
print(bin(10)) # 十进制转二进制0b1010
print(hex(23)) # 十进制转十六进制0x17
# 元组转换为列表
tup=()
li=list(tup)
print(type(tup))
print(type(li))
# 列表转换为元组
tupList=tuple([1,2,23,4])
print(type(tupList))
# dict()创建字典也可以转换字典
dic=dict()
dic1=dict(name='小明1', age=118) # 创建一个字典
print(type(dic))
dic['name']='小明'
dic['age']=18
print(dic)
print(dic1)
# bytes转换
print(bytes('我喜欢python',encoding='utf-8'))