import turtle as t
import random
from turtle import Screen

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

def draw_shape(num_sides):
  angle = 360/num_sides
  for _ in range(num_sides):
    tim.forward(50)
    tim.right(angle)

colors = ["cornflower blue",
         "deep sky blue",
         "pale green",
         "medium aquamarine",
         "wheat",
         "peach puff",
         "light sky blue"]

for shape_side_n in range(3,11):
  tim.color(random.choice(colors))
  draw_shape(shape_side_n)


'''
# color = random.choices(range(256), k=3)
# tim.pencolor(color[0], color[1], color[2])

# r = random.randint(0, 255)
# g = random.randint(0, 255)
# b = random.randint(0, 255)
# random_color = (r, g, b)
# tim.pencolor(random_color)

screen = Screen()
screen.colormode(255)

for sides in range(3,11):
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  tim.pencolor(r, g, b)
  
  for _ in range(sides):
    tim.forward(40)
    tim.right(360/sides)

'''
