from turtle import *

def tree(size, angle=45):
    if size < 2:
        return
    lt(angle)
    fd(size)
    tree(size/2, angle)
    bk(size)
    rt(angle*2)
    fd(size)
    tree(size/2, angle)
    bk(size)
    lt(angle)


pencolor('green')
speed(10)
lt(90)
tree(120, 15)
done()
