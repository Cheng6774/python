a_tuple = (1, 3, 5, 7 , 9)
another_tuple = 12, 3, 5, 15 , 6
a_list = [2, 4, 6, 8, 10]

for content in a_list:
    print(content)

for content_tuple in a_tuple:
    print(content_tuple)

for index in range(len(a_list)):
    print("index = ", index, ", number in list = ", a_list[index])

for index in range(len(a_tuple)):
    print("index = ", index, ", number in tuple = ", a_tuple[index])
#index在元组列表中的起始位是0，按顺序为0,1,2,3...
