def bitrep(n):#bruteforce approach TC=O(n)
    s = str(bin(n))[2:]
    #print("%s" % s)
    #print(s.__str__())
    #print(s)
    print('{}'.format(s))
    print(s.count('1'))

def cntbits(n):#O(log(n)) 
    cnt=0
    while n:
        cnt+=1
        n=n&(n-1)
    print(cnt)

bitrep(15)
cntbits(15)