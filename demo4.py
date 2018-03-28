#列表实现一个名片查询系统
print("-"*50)
print('名片查询系统')
print('1:add a new name')
print('2:delete a name')
print('3:find a name')
print('4:update a name')
print('5:exit')
print('-'*50)
name=[]
while True:
    num=int(input("请输入功能序号:"))
    if num==1:
        a1=input("input your name:")
        name.append(a1)
        print(name)
    elif num==2:
        a2=input("input your name:")
        name.remove(a2)
        print('already deleted!')
    elif num==3:
        a3=input("input your name")
        if a3 in name:
            print('has found:',a3)
        else:
            print('not found')
    elif num==4:
        a4=input('input the old name:')
        a5=input('input the new name:')
        index=name.index(a4)
        name[index]=a5
        print("has changed",name)
    elif num==5:
        break
    else:
        print('wrong!')