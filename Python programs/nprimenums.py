#Seive Theorem
#TC-0(n*log(logn))

from math import *
def nprime(n):
    prime=[True]*(n+1)
    prime[0]=False
    prime[1]=False
    for p in range(2,int(sqrt(n))+1):
        if prime[p]==True:
            for i in range(p*p,n+1,p):
                prime[i]=False

    for i in range(0,len(prime)):
        if prime[i]==True:
            print(i,end=" ")









t=int(input("Enter times: "))
while t:
    n=int(input("\nEnter no to check prime nums upto: \n"))
    nprime(n)
    t-=1