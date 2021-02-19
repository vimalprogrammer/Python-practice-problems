# Reverse a number

a = int(input("Enter an integer: "))

reverse = 0

while (a!=0):
    rem = a % 10
    reverse = reverse * 10 + rem
    a //= 10

print("Reverse of the number is: ", reverse)
#print(3%10)