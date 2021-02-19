#Swap two numbers without using third variable

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

a = a + b;
b = a - b;
a = a - b;

print("Swapping of numbers are: ", a, "and", b)