#Program No.8 To draw a bowtie
#from turtle import *
import turtle as t
t.bgcolor("pink")
t.pensize(10)
t.penup()
t.goto(-200, -100)
t.pendown()
t.fillcolor("RED")
t.begin_fill()
t.goto(-200, 100)
t.goto(200, -100)
t.goto(200, 100)
t.goto(-200, -100)
t.end_fill()

t.exitonclick()
