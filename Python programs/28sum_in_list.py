n=int(input("How many nums : "))
lst=[]
for i in range(n):
    nums=int(input("Enter "+str(i+1)+" number : "))
    lst.append(nums)
print("sum of them : ",sum(lst))
