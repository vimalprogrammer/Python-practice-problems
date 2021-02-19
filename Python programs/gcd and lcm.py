#euclid algo
#time complexity = O(log(min(a,b)))
#product=lcm*gcd

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
def lcm(a,b):
    product=a*b
    hcf=gcd(a,b)
    lcm=product//hcf
    return lcm



t=int(input("Enter how many times : "))
while(t):
    n,m=map(int,input("Enter numbers : ").split(" "))
    print("gcd = {}  lcm = {}".format(gcd(n,m),lcm(n,m)))

    t-=1