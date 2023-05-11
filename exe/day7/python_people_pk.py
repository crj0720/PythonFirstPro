# 决战紫禁之巅有两个人物，西门吹雪以及叶孤城·属性:
# ·name玩家的名字
# ·blood 玩家血量
# ·方法:
# ·tong0捅对方一刀,对方掉血10滴
# kanren()砍对方一刀，对方掉血15滴
# ·chivao()吃一颗药，补血10滴
# str_打印玩家状态
import  time

# 第一步 需要定义一个类【角色类】
class Role:
    def __init__(self,name,hp):
        """
        构造初始化函数
        :param name: 角色名
        :param hp: 血量
        """
        self.name=name
        self.hp=hp
        pass

    def tong(self,enemy):
        """
        捅一刀
        :param enemy: 敌人
        :return:
        """
        # 敌人减掉10滴血
        enemy.hp-=10
        info='【%s】捅了【%s】一刀'%(self.name,enemy.name)
        print(info)
        pass

    def kangren(self,enemy):
        """
        砍一刀
        :param enemy: 敌人
        :return:
        """
        # 敌人减掉15滴血
        enemy.hp-=15
        info='【%s】砍了【%s】一刀'%(self.name,enemy.name)
        print(info)
        pass

    def chiyao(self,enemy):
        """
        吃药
        :param enemy: 敌人
        :return:
        """
        # 自己增加15滴血
        enemy.hp+=15
        info='【%s】吃了一棵补血药，增加15滴血'%(self.name)
        print(info)
        pass
    def __str__(self):
        return '%s还剩下%s的血量'%(self.name,self.hp)

# 第二步 创建两个实例化对象 菠萝吹雪、叶哭城
# xmcx=Role("菠萝吹雪",100)
# ykc=Role("叶哭城",100)
# xmcx.tong(ykc) # 菠萝吹雪 捅 叶哭城
# print(xmcx.hp)
# print(ykc.hp)
# print(xmcx)
# print(ykc)
# 【菠萝吹雪】捅了【叶哭城】一刀
# 100
# 90
# 菠萝吹雪还剩下100的血量
# 叶哭城还剩下90的血量

# xmcx.tong(ykc) # 菠萝吹雪 捅 叶哭城  叶90
# print(xmcx)
# print(ykc)
# print('***************************************')
# xmcx.tong(ykc) # 菠萝吹雪 捅 叶哭城  叶80
# print(xmcx)
# print(ykc)
# print('***************************************')
# xmcx.tong(ykc) # 菠萝吹雪 捅 叶哭城  叶70
# print(xmcx)
# print(ykc)
# print('***************************************')
# ykc.tong(xmcx) # 叶哭城 捅 菠萝吹雪  叶70  菠萝 90
# print(xmcx)
# print(ykc)
# print('***************************************')
# ykc.chiyao(xmcx) # 叶哭城吃了药  叶85  菠萝 90
# xmcx.chiyao(ykc)
# print(xmcx)
# print(ykc)
# print('***************************************')
# # 【菠萝吹雪】捅了【叶哭城】一刀
# # 菠萝吹雪还剩下100的血量
# # 叶哭城还剩下90的血量
# # ***************************************
# # 【菠萝吹雪】捅了【叶哭城】一刀
# # 菠萝吹雪还剩下100的血量
# # 叶哭城还剩下80的血量
# # ***************************************
# # 【菠萝吹雪】捅了【叶哭城】一刀
# # 菠萝吹雪还剩下100的血量
# # 叶哭城还剩下70的血量
# # ***************************************
# # 【叶哭城】捅了【菠萝吹雪】一刀
# # 菠萝吹雪还剩下90的血量
# # 叶哭城还剩下70的血量
# # ***************************************
# # 【叶哭城】吃了一棵补血药，增加15滴血
# # 【菠萝吹雪】吃了一棵补血药，增加15滴血
# # 菠萝吹雪还剩下105的血量
# # 叶哭城还剩下85的血量
# # ***************************************


xmcx=Role("菠萝吹雪",100)
ykc=Role("叶哭城",100)
while True:
    if xmcx.hp <=50 or ykc.hp<=50:
        # 满足条件 就退出循环
        break
    xmcx.tong(ykc) # 菠萝吹雪 捅 叶哭城  叶90
    print(xmcx)
    print(ykc)
    print('***************************************')
    xmcx.tong(ykc) # 菠萝吹雪 捅 叶哭城  叶80
    print(xmcx)
    print(ykc)
    print('***************************************')
    xmcx.tong(ykc) # 菠萝吹雪 捅 叶哭城  叶70
    print(xmcx)
    print(ykc)
    print('***************************************')
    ykc.tong(xmcx) # 叶哭城 捅 菠萝吹雪  叶70  菠萝 90
    print(xmcx)
    print(ykc)
    print('***************************************')
    time.sleep(1)
    pass
print('对战结束')

# day7-10 07:19从头开始写