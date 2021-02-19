from math import sqrt

def prime1(n):#TC=O(n)
    divcnt=0
    for i in range(1,n+1):
        if n%i==0:
            divcnt+=1
    print(divcnt)
    if divcnt==2:
        print("Prime")
        return True
    else:
        print("Not Prime")
        return False

def prime2(n):
    if n==0 or n==1:#TC=O(1)
        return False
    if n==2 or n==3:#TC=O(1)
        return  True
    if n%2==0 or n%3==0:#TC=O(1)
        return False
    for i in range(5,int(sqrt(n))+1):#TC=O(root(N))
        if n%i==0 or n%(i+2)==0:
            return False
    return True


t=int(input("Enter how many times : "))
while(t):
    n=int(input("Enter number to check prime or not : "))
    #print(prime1(n))
    print(prime2(n))
    print(prime1(n))
    t-=1

