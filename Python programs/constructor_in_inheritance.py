class Group1:
    def __init__(self):
        print("vimal is the one")
    def sayhi(self):
        print("hi vimal..!")
class Group2():
    def __init__(self):
        print("sharmila is the two")# due to MRO
    def sayhi(self):

        print("hi sharmila")
class Group3(Group1,Group2):
    def __init__(self):
        print("harini is the three")
        super().__init__()
    def sayhi(self):

        print('hi harini')
        super().sayhi()#dont use init in methods
a1=Group3()

a1.sayhi()
