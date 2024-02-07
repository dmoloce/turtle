import random
import turtle
from turtle import Turtle, Screen
import colorgram

turtle.colormode(255)
timmy = Turtle()
timmy.shape("turtle")
timmy.color("lime")
timmy.speed(3)


def rectangle():
    for _ in range(4):
        timmy.forward(100)
        timmy.left(90)


def dashed_line():
    timmy.right(90)
    for _ in range(10):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()



# # create triangle, square pentagon etc all with same base
def moving(num_sides):
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(360 / num_sides)

def same_base():
    timmy.right(90)
    shapes = 3
    while shapes < 8:
        moving(shapes)
        shapes += 1
# ---------------------------------------
# spirograph():

timmy.right(180)
timmy.penup()
timmy.forward(200)
timmy.pendown()




def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def spirograph():
    gap = 10
    timmy.speed(0)
    timmy.width(10)
    for _ in range(int(360 / gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)


# hirst dot painting
# extract colors
rgb_colors = []
colors = colorgram.extract('hirst.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

# delete first tuples as they are white / background
rgb_colors = [(35, 19, 15), (197, 144, 123), (30, 106, 155), (142, 85, 55), (9, 21, 45), (236, 213, 85),
              (196, 135, 155), (156, 62, 90), (221, 85, 66), (153, 17, 37), (202, 79, 104), (14, 54, 30),
              (162, 163, 35), (118, 172, 196), (41, 125, 79), (77, 12, 22), (120, 188, 160), (18, 92, 53),
              (11, 58, 137), (23, 201, 179), (23, 174, 206), (139, 222, 208), (149, 23, 16), (223, 172, 191),
              (233, 172, 162), (238, 206, 8)]


#timmy.dot(30, (35, 19, 15))
timmy.setheading(225)
timmy.penup()
timmy.forward(250)
timmy.setheading(0)
#timmy.pendown()



def hirst_line():
    for _ in range(10):
        color = random.choice(rgb_colors)
        timmy.dot(30,color)
        timmy.penup()
        timmy.forward(60)
        #timmy.pendown()

def hirst_column():
    timmy.hideturtle()
    for _ in range(10):
        hirst_line()
        timmy.left(90)
        #timmy.penup()
        timmy.forward(60)
        timmy.left(90)
        timmy.forward(600)
        timmy.left(180)
        #timmy.pendown()
    timmy.showturtle()





#rectangle()
#dashed_line()
#same_base()
hirst_column()

screen = Screen()
screen.exitonclick()
