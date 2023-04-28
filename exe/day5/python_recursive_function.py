# 求阶乘
# 用循环的方法去实现
def jiecheng(n):
    result=1
    for item in range(1,n+1):
        result*=item
        pass
    return result
print('10的阶乘{}'.format(jiecheng(10)))
# 递归满足的条件：
# 自己调用自己
# 必须有一个明确的结束条件
# 优点：逻辑简单，定义简单
# 缺点：容易导致栈溢出，内存资源紧张，甚至内存泄漏
# 递归方式去实现
def digui(n):
    """
    递归实现
    :param n:阶乘参数
    :return:
    """
    if n == 1:
        return 1
    else:
        return n*digui(n-1)
    pass

# 递归调用
print(digui(5))
print('5的阶乘{}'.format(digui(5)))

# 递归案例 模拟实现 树形结构的遍历
import os # 引入文件操作模块
def findFile(file_Path):
    listRs=os.listdir(file_Path) # 得到该路径下所有的文件夹
    for fileItem in listRs:
        full_path=os.path.join(file_Path,fileItem) # 获取完整的文件路径
        if os.path.isdir(full_path): # 判断是否是文件夹
            findFile(full_path)# 如果是一个文件夹，再次去递归
        else:
            print(fileItem)
            pass
        pass
    else:
        return
    pass

# 调用搜索文件夹对象
findFile('C:\\crj\\尚硅谷Kubernetes（k8s）新版\\视频')