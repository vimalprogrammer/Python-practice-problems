#ispowerof2
#512 ->True =2**9
#1024 ->True =2**10
#513 ->False
def ispowerof2(n):
    #TC=O(n)
    if n<=0:
        return False
    x=n
    y=not(n&(n-1))
    return x and y
t=int(input("times "))
while(t):
    n=int(input("Enter "))
    print(ispowerof2(n))
    t-=1