#Program 4 Turtle Program Using Function
import turtle as t
def draw_square(length):  #length is called Formal Parameter
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
draw_square(50) #-> 50 is called as Actual Parameter

t.penup()
t.forward(150)
t.pendown()

draw_square(70)

t.penup()
t.forward(350)
t.pendown()

draw_square(20)

t.penup()
t.forward(450)
t.pendown()

draw_square(40)

t.exitonclick()

print()
input("Press return to continue ...")
