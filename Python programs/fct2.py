
def factorial(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    print(f)


t = int(input("enter times"))
while t:
    n = int(input())
    #print("Factorial of", n, "is", factorial(n))
    fact(n)
    # Driver Code

