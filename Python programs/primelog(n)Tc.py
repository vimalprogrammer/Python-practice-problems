#Seive of Eratosthenes theorem

from math import *
n=int(input("Enter "))
prm=[True]*(n+1)
prm[0]=False
prm[1]=False

for p in range(2,int(sqrt(n))+1):
    if(prm[p]==True):
        for i in range(p*p,n+1,p):
            prm[i]=False
for i in range(0,len(prm)):
        if prm[i]==True:
            print(i,end=" ")
