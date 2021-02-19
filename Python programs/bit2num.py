def num(n):
    print("%d" % n)
#num(0b1110)
def num1(n):
    print(int(n,2))
#num1('1011')
def kthbit(n,k):
    print(str(bin(n))[2:])
    if n&(1<<(k-1)):
        print("SET")
    else:
        print("NOT SET")
kthbit(6,1)
kthbit(6,3)
kthbit(6,2)