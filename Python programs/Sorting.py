#bubble sort

list=[5,2,9,1,4,3]
i=0
def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp

sort(list)
print(list)
