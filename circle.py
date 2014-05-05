from turtle import *
from math import pi

def circle0():
    for i in range(360):
        fd(1)
        rt(1)

def circle1(size):
    for i in range(360):
        fd(size)
        rt(1)

def circle(diameter):
    circle1(diameter * pi / 360)


def polygon(sides, size):
    for i in range(sides):
        fd(size)
        rt(360./sides)

speed(0)
ht()
#circle0()
#circle1(2)
#circle1(.5)
circle(100)
polygon(4, 100)
st()
done()
