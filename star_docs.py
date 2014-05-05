"""
Turtle star example from the official docs_

.. _docs: https://docs.python.org/3.4/library/turtle.html

"""

from turtle import *
speed(0)
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
