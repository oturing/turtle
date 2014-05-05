from turtle import *
def square(side=50):
    for i in range(4):
        fd(side)
        right(90)

def flower(n=10, side=200):
    for i in range(n):
        square(side)
        right(360/n)

speed(0)
flower()
done()
