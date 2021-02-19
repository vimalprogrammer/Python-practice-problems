#n^n=0
#n^0=n

def findsinglecurrency(arr):
    res=arr[0]
    for i in range(1,len(arr)):
        res=res^arr[i]
    return res
arr=list(map(int,input().split()))
print(findsinglecurrency(arr))