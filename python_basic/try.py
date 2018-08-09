try:
    file = open('eeee.txt', 'r+')
except Exception as e:
    print('there is no file named as eeeee')
    response = input('do you want to create a new file')
    if response =='y':
        file = open('eeee.txt','w')
        file.write('first write')
    else:
        pass
else:
    file.write('second write')
file.close()
