
from threading import *
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(5):
           print('hello')
           sleep(1)


class hi(Thread):
    def run(self):
        for i in range(5):
            print('hiiiii')
            sleep(1)

a1=Hello()
b1=hi()
a1.start()

sleep(.3)
b1.start()
a1.join()
b1.join()
print('bye')
print('bye...bye')
