#冒泡排序

def bubblesort(numbers):
    for j in range(len(numbers)-1):
        for i in range(j):
            if numbers[i+1]<numbers[i]:
                numbers[i],numbers[i+1]=numbers[i+1],numbers[i]
    print(numbers)
if __name__=='__main__':
    numbers=[23,1,234,45,6]
    bubblesort(numbers)


