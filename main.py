import turtle as t
from turtle import Screen

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########
tim.penup()
tim.setpos(-150,-150)
tim.setheading(45)

# tim.pendown()
# for _ in range(15):
#   tim.pencolor("black")
#   tim.forward(10)
  
#   tim.pencolor("white")
#   tim.forward(10)

for _ in range(15):
  tim.pendown()
  tim.forward(10)
  
  tim.penup()
  tim.forward(10)

screen = Screen()
screen.exitonclick()

