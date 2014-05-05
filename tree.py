from turtle import *

def tree(size):
	if size < 2:
		return
	lt(45)
	fd(size)
	tree(size/2)
	bk(size)
	rt(90)
	fd(size)
	tree(size/2)
	bk(size)
	lt(45)


pencolor('green')
speed(10)
lt(90)
tree(160)
done()
