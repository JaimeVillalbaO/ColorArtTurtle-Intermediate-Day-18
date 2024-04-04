import  random
from turtle import Turtle, Screen, colormode


colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(300)]
# print(colors)


jaime = Turtle()
colormode(255)
jaime.hideturtle()

x= -250
y = -250
end_picture = False
while not end_picture:
    for _ in range (10) :
        for _ in range (10):
            jaime.penup()
            jaime.goto(x, y)
            jaime.dot(20, random.choice(colors))
            x += 50            
        x = -250
        y += 50
    end_picture = True


screen = Screen()
screen.exitonclick()