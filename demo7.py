dict = {1: 'apple', 2: 'banana', 3: "orange"}
for (a,b) in dict.items():
    print("dict[%s]" %a,b)

#按照key进行排序
print(sorted(dict.items(), key=lambda d:d[0]))
#按照value进行排序.
print(sorted(dict.items(), key=lambda d:d[1]))

print("%s, %(w)s,%(e)s" % {'w': 'purple', 'e': 'blue'})


#在列表中存储列表
movies=[
    "The holly Grail", 1975, "Terry Jones", 91,
    ["Graham Chapman",
     ["Micheal Palin", "Jone Cleese", "Eric"]]
]
for names in movies:
    if isinstance(names, list):
        for cha in names:
            if isinstance(cha, list):
                for ch in cha:
                    print(ch)
            else:
                print(cha)
    else:
        print (names)

print("*"*50)
#使用函数递归的去解决
"""
输出嵌套列表
"""

def _print(list_item):
    for each_item in list_item:
        if isinstance(each_item, list):
            _print(each_item)
        else:
            print(each_item)


_print(movies)





