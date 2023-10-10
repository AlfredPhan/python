#Program No.6 To draw a sun
from turtle import *
import turtle as t
color('red', 'yellow')
begin_fill()
while True:
    forward(90)
    left(70)
    #t.circle(90)
    if abs(pos()) < 1: #absolute value
        break
end_fill()
done()
