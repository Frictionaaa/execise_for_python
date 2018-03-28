names = [{'name': 'Tom', 'age': '19'}, {'name': 'Jack', 'age': '34'}
         ]
print(names)
while True:
    a1 = input('input the old name:')
    flag = True
    for lines in names:
        if lines['name'] == a1:
            flag = True
            a2 = input("the new name:")
            a3 = input("the new age:")
            lines['name'] = a2
            lines['age'] = a3
            break
    if flag:
        print('has changed!')
    else:
        print('not exist!')
    print(names)
