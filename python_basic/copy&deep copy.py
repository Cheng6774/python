a=[1,2,3]
b=a
id(a)
id(b)
print(id(a))
print(id(b))
print(id(a)==id(b))#赋值后，两者的id相同，在shell中输入该语句为true
print('\n' * 2)

b[0]=222222  #此时，改变b的第一个值，也会导致a值改变。
print(a,b)#a,b值同时改变
print('\n' * 2)

import copy
a=[1,2,3]
c=copy.copy(a)  #拷贝了a的外围对象本身
print(id(c))
print(id(a)==id(c))  #id不相同false
c[1]=22222   #此时，我去改变c的第二个值时，a不会被改变。
print(a,c) #a值不变,c的第二个值变了，这就是copy和‘==’的不同
print('\n' * 2)


#copy.copy()
a=[1,2,[3,4]]  #第三个值为列表[3,4],即内部元素
d=copy.copy(a) #浅拷贝a中的[3，4]内部元素的引用，非内部元素对象的本身
print(id(a)==id(d))#id不相同为false
print(id(a[2])==id(d[2]))#数组id相同
a[2][0]=3333  #改变a中内部元素列表中的第一个值
print(d)      #这时d中的列表元素也会被改变
[1, 2, [3333, 4]]
print('\n' * 2)

#copy.deepcopy()
e=copy.deepcopy(a) #e深拷贝了a
a[2][0]=2222  #改变a中内部元素列表中的第一个值
print(a[2][0]) #查看a中内部元素列表第一个的值
print(e) #查看e中内部元素列表第一个的值
print(a[2][0]==e[2][0])#因为是深拷贝，这时e中内部元素[]列表的值不会因为a中的值改变而改变
print(id(a[2][0])==id(e[2][0]))
print('\n' * 2)

#浅拷贝值随原对象改变，id相同；深拷贝不随原对象值改变，id不同
