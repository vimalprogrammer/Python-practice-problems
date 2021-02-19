#bitwise and &
#bitwise or |
#bitwise not ~
#bitwise xor ^
#bitwise rightshift >> [is divide in power of 2]
#bitwise leftshift << [is multiply in power of 2]
#n&1==1 refers odd
#n&1==0 refers even

def evenodd(n):
    if n&1==1:
        print("Odd")
    else:
        print("even")
def mulpow(x,y):
    #x=400 y=4  --> 400*(2**4)=400*16=6400
    return x<<y

def divpow(x,y):
    #x=400 y=4  --> 400//(2**4)=400//16=25
    return x>>y



t=int(input("enter nums: "))
while t:
    #n=int(input())
    x,y=map(int,input().split())
    #evenodd(n)
    print(mulpow(x,y))
    print(divpow(x, y))
    t-=1
