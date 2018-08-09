a=[1,2,3]
b=[4,5,6]
ab=zip(a,b)
print(zip(ab)) #需要加list来可视化这个功能

a=[1,2,3]
b=[4,5,6]
ab=zip(a,b)
print(list(ab))
for i,j in zip(a,b):
     print(i/2,j*2)

'''fun=lambda x,y:x+y
x=int(input('x='))
y=int(input('y='))
print(fun(x,y))
'''
def fun(x,y):
  return(x+y)
print(list(map(fun,[1],[2])))
print(list(map(fun,[1,2],[3,4])))
     
