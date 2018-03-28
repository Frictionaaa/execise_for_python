#在列表里嵌套字典，如何实现删除

names = [{'name': 'Jack', 'age': '18'}, {'name': 'Tom', 'age': '21'}
         ]
while True:
    a1 = input("please input the name which will be deleted:")
    flag = True
    for lines in names:
        if lines['name'] == a1:
            flag = True
            names.remove(lines)
    if flag:
        print('has deleted')
    else:
        print('not exist')
    print(names)