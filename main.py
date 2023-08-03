import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

tim.speed(0)
tim.hideturtle()

def draw_spirograph(size_of_gap):
  for _ in range(int(360/ size_of_gap)):
    tim.color(random_color())
    tim.circle(50)
    tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(15)

# only draw as many circles as we need
# for _ in range(100):
#   tim.color(random_color())
#   tim.circle(50)
#   tim.setheading(tim.heading() + 10)

# for i in range(36):
#   tim.color(random_color())
#   tim.circle(50)
#   tim.left(10)

  
# for num in range(1,361):
#   if num%3 == 0:
#     tim.color(random_color())
#     tim.circle(50, num)

