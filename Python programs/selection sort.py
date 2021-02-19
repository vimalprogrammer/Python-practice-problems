list=[4,2,9,7,1,5]
def sort(list):
    for i in range(5):
        minpos=i
        for j in range(i,6):
            if list[j]<list[minpos]:
                minpos=j
        temp=list[i]
        list[i]=list[minpos]
        list[minpos]=temp
        print(list)
sort(list)
print(list)