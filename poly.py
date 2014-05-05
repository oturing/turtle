from turtle import *

def poly(side, angle):
    fd(side)
    rt(angle)
    poly(side, angle)

def polyspi(side, angle, increment=10):
    if side > 500:
        return
    fd(side)
    rt(angle)
    polyspi(side+increment, angle)

pencolor('blue')
speed(10)
polyspi(5, 144)
done()
