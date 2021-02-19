# Python program to determine whether
# the number is Armstrong number or not

# Function to calculate x raised to
# the power y
def power(x, y):
    return x**y


# Function to calculate order of the number
def order(x):
    # Variable to store of the number
    n = 0
    while (x != 0):
        n = n + 1
        x = x // 10

    return n
def isArmstrong(x):
    n = order(x)
    temp = x
    sum1 = 0

    while (temp != 0):
        r = temp % 10
        sum1 = sum1 + power(r, n)
        temp = temp // 10

    # If condition satisfies
    print(str(x)+" "+str(sum1))
    return (sum1 == x)


x = 54748
print(isArmstrong(x))

x = 12
print(isArmstrong(x))