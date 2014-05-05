from turtle import *

def box():
    fd(200)
    rt(90)
    fd(100)
    rt(90)
    fd(200)
    rt(90)
    fd(100)
    rt(90)

def pinwheel():
    for i in range(8):
        rt(45)
        box()
    rt(90)
    fd(450)

speed(0)
pinwheel()
done()
