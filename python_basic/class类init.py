class Calculator:
    name='good calculator'
    price=18
    def __init__(self,name,price,height,width,weight):
        # 注意，这里的下划线是双下划线
        self.name=name
        self.price=price
        self.h=height
        self.wi=width
        self.we=weight
c=Calculator('bad calculator',18,17,16,15)

"""
在python shell中分别查看下面参数
c.name

c.price

c.h

c.wi

c.we
"""
class Calculator:
    name='good calculator'
    price=18
    def __init__(self,name,price,hight=10,width=14,weight=16): #后面三个属性设置默认值,查看运行
        self.name=name
        self.price=price
        self.h=hight
        self.wi=width
        self.we=weight
        self.add=(1,2)#也可以在init中定义函数，将类赋值到个体c中会自动输出
c=Calculator('bad calculator',12)#其余init参数已经固定

