#####Turtle Intro######
'''
import turtle as t

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.forward(100)
timmy_the_turtle.backward(200)
timmy_the_turtle.right(90)
timmy_the_turtle.left(180)
timmy_the_turtle.setheading(0)

'''
######## Challenge 1 - Draw a Square ############
from turtle import Turtle, Screen

turt = Turtle()
turt.shape("turtle")
turt.color("olive drab")
for _ in range(0,4):
  turt.forward(25)
  turt.rt(90)

screen = Screen()
screen.exitonclick()
