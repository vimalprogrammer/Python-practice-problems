class computer:
    def __init__(self):
        self.name="vimal"
        self.age = 56

    def compare(self,c1):
        if self.age==c1.age:
            return True
        else:
            return False




c1=computer()
c1.age=56
c2=computer()
if c2.compare(c1):
    print("same")
else:
    print("different")


