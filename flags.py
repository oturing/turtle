from turtle import *

SIZE = 200

def rect(width, height):
    for i in range(2):
        fd(width)
        rt(90)
        fd(height)
        rt(90)

def flag_e():
    color('blue', 'blue')
    begin_fill()
    rect(SIZE, SIZE/2)
    end_fill()
    pu()
    rt(90)
    fd(SIZE/2)
    lt(90)
    pd()
    color('red', 'red')
    begin_fill()
    rect(SIZE, SIZE/2)
    end_fill()
    pu()
    lt(90)
    fd(SIZE/2)
    rt(90)



speed(0)
flag_e()
done()
