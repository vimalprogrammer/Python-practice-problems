#sum of n numbers

def sum1(n):#TC=O(1)
    return n*(n+1)//2

def sum2(n):#TC=O(n)
    sum = 0
    for i in range(1,n+1):#[1,n] n is inclusive
        sum+=i
    return sum


t=int(input("Enter how many times : "))
while(t):
    n=int(input("Enter number that upto sum: "))
    print("sum1 executed value {}".format(sum1(n)))
    print("sum2 executed value {}".format(sum2(n)))

    t-=1
