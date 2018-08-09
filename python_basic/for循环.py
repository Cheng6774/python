example_list=[1,2.3,4,45,6,477,85,56,8]
for i in example_list:
  print(i)
  print(i+1)
print('oue of list')



for i in range(1,10):
    print(i)

for i in range(1,10,2):
    print(i)

#高级主题
tup = ('python', 2.7, 64)
for i in tup:
    print(i)

dic = {}
dic['lan'] = 'python'
dic['version'] = 2.7
dic['platform'] = 64
for key in dic:
    print(key, dic[key])

s = set(['python', 'python2', 'python3','python'])
for item in s:
    print(item)
