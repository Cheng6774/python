while True:
    b=input('type something')
    if b =='1':
        break#结束while循环，执行while循环外操作
        print('执行break操作')
    else:
        pass#仍然留在while循环中
        print('执行pass操作')
    print('stille in while')
print('finish run')


'''while True:
    b=input('type something')
    if b =='1':
        continue#直接进入下一次循环,不执行if语句后面的操作
        print('执行coninue操作')
    else:
        pass#完成else分支操作和if语句后面的操作并返回while
        print('执行pass操作')
    print('stille in while')

'''
