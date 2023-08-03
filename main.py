import turtle as t
from turtle import Screen 
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

#thicker lines
#speed up turtle

screen = Screen()
# screen.onclick(tim.goto)

def isInScreen(wn,t):
  '''returns true if turtle still in screen, false if out of screen'''
  leftBound = -(wn.window_width() / 2)
  rightBound = wn.window_width() / 2
  topBound = wn.window_height() / 2
  bottomBound = -(wn.window_height() / 2)

  turtleX = t.xcor()
  turtleY = t.ycor()

  stillIn = True
  if turtleX > rightBound or turtleX < leftBound:
      stillIn = False
  if turtleY > topBound or turtleY < bottomBound:
      stillIn = False

  return stillIn



tim.hideturtle()
tim.pensize(10)
tim.speed(0)

# def stop():
#   screen.exitonclick()



#want it to continue until i click screen
for _ in range(0,500):
  # program stops when runs off screen
  # instead change directions so stays on screen
  while isInScreen(screen, tim):
    tim.color(random.choice(colors))
    tim.forward(random.randint(1, 50))
    tim.right(random.randint(1, 5)*90)



# def f():
#     tim.fd(50)

# screen.onkey(f, "Up")
# screen.listen()
