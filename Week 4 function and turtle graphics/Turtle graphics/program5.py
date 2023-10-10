#Program No.5 Creating the night view starts
import turtle as t
import random
t.color("white")
t.bgcolor("grey")
t.speed(0)
t.hideturtle()

def starmaker(step,angle):
    for iter in range(5):
        t.forward(step)
        t.right(angle)

for i in range(50):
    t.penup()
    t.setpos(random.randint(-450,450), random.randint(-100,100))
    t.pendown()
    starmaker(30,144)
t.exitonclick()


