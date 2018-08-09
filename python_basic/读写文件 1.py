text='This is my first test. This is the second line. This the third '
print(text)  # 无换行命令


text='This is my first test.\nThis is the second line.\nThis the third line'
print(text)   # 输入换行命令\n，要注意斜杆的方向。注意换行的格式和c++一样

file=open('my file.txt','w')
file.write(text)
file.close()

text='\tThis is my first test.\n\tThis is the second line.\n\tThis is the third line'
print(text)  #延伸使用 \t 对齐
