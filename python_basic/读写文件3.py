text='This is my first line. \nThis is the second line.\nThis the third line '
file=open('my file.txt','w')
file.write(text)
file.close()


file=open('my file.txt','r')
content=file.readline()
print(content)
file.close()

file=open('my file.txt','r')
content=file.readline()
content=file.readline()#读取第二行
print(content)
file.close()

file=open('my file.txt','r')
content=file.readlines()
print(content)
file.close()
          
