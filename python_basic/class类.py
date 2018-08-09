class Calculator:
    name='good calculator'
    price=18
    def add(self,x,y):
        print(self.name)
        result = x + y
        print(result)
    def minus(self,x,y):
        result=x-y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)
cal=Calculator()  #注意这里运行class的时候要加"()",否则调用下面函数的时候会出现错误,导致无法调用.
cal.name

cal.price

cal.add(10,20)

cal.minus(10,20)

cal.times(10,20)

cal.divide(10,20)
