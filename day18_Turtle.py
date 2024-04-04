from turtle import Turtle, Screen, colormode
# from turtle import * #se usa para importar todo los metodos del modulo, pero no es usado en la comunidad por general confison
import random

jaime = Turtle()
jaime.shape('turtle')
jaime.color('chartreuse')
colormode(255)
# for i in range(4):
#     jaime.forward(100)
#     jaime.left(90)

# for i in range(100):
#     jaime.pendown()
#     jaime.forward(10)
#     jaime.penup()
#     jaime.forward(10)

colores_turtle = ["red", "orange", "yellow", "green", "blue", "purple", "brown", "black", "gray", "pink"]

# n= 3
# finish = False
# while not finish:
    
#     for i in range(n):       
#         jaime.forward(100)
#         jaime.right(360/n)
#     n+=1
#     jaime.color(random.choice(colores_turtle))
#     if n == 13 :
#         finish = True    


def change_color():    
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tuple = (r, g, b)
    return tuple
    

# angles = [90, 180, 270, 360 ]
# jaime.pensize(5)
jaime.speed('fastest')
# for i in range (1000):
#     jaime.forward(30)
#     jaime.setheading(random.choice(angles))
#     jaime.color((change_color()))


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        jaime.circle(120)
        jaime.left(size_of_gap)
        jaime.color(change_color())

draw_spirograph(5)


screen = Screen()
screen.exitonclick()
