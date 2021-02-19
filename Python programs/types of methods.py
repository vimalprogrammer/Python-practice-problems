class home:
    leaader="mani"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get(self):#accessor method
        return self.name

    def set(self,alt_name):#mutator method
         self.name = alt_name
    @classmethod
    def head(cls):
        return cls.leaader
    @staticmethod
    # import math
    # n=int(input("Enter number:  "))
    # print(math.factorial(n))
    def factorial(n):
        fact = 1
        i = 1
        while i <= n:
            fact = fact * i
            i += 1
        return fact




c1=home('vimal',12)
print(c1.name)
c1.set("vijay")
print(c1.name)
print(c1.get())
print(home.head())
print(home.factorial(6))