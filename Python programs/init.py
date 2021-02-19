class coder:
    def __init__(self):
        print("hi vimal")#no need to call special methods
                         #it is like constructer

    def code(self):
        for i in range(4):
            for j in range(i+1):
                print('$',end=" ")
            print()
pro1=coder()
pro1.code()
