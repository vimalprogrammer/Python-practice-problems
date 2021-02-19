#import math
#n=int(input("Enter number:  "))
#print(math.factorial(n))
def factorial(n):
    fact=1
    i=1
    while(i<=n):
        fact=fact*i
        i+=1
        print(fact)
factorial(5)
