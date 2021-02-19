# Python Program to find the L.C.M. of two input number

a=int(input("Enter first number: "))
b=int(input("Enter seconf number: "))

def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
print("The L.C.M. is", lcm(a, b))