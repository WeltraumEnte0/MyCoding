import turtle

box = turtle.Turtle()

def house():
    box.forward(200)
    box.left(90)
    box.forward(200)
    box.left(90)
    box.forward(200)
    box.right(135)
    box.forward(141.42)
    box.right(90)
    box.forward(141.42)
    box.right(90)
    box.forward(282.84)
    box.right(135)
    box.forward(200)
    box.right(135)
    box.forward(282.84)
    box.left(45)

    turtle.exitonclick
    
for i in range(1):
    house()