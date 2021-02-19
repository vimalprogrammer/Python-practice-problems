class A:
    def parent(self):
        print("arumugam")
        print('kalaiarasi')

class B:
    def subparent(self):
        print('mani')
        print('sasi')

class C(A,B):
    def child(self):
        print('vimal')
        print('sharmila')
        print('harini')


a1=A()
a1.parent()
b1=B()
b1.subparent()
c1=C()
c1.parent()
#single level
#multi level
#multiple level