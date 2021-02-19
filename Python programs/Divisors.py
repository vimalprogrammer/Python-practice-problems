from math import *


def fun1(n):#TC=O(n)=24
    div1 = []
    for i in range(1,n+1):#(1,n)
        if n%i==0:
            div1.append(i)
    return div1
def fun2(n):#TC=O(root(n))=4.89 analogy used
    div2=set()
    for i in range(1,int(sqrt(n))+1):#[1,root(1)]
        if n%i==0:
            div2.add(i)
            div2.add(n//i)#debug to uderstand
    return list(div2)

t=int(input("How many times u going to execute: "))
while t:
    n=int(input("Enter number: "))
    div2 = fun2(n)
    print(*div2)
    div1 = fun1(n)
    print(*div1)
    t-=1
