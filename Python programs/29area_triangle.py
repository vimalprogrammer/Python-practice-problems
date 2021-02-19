a=float(input("Enter the side1: "))
b=float(input("Enter the side2: "))
c=float(input("Enter the side3: "))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area is: %0.2f" %area)
