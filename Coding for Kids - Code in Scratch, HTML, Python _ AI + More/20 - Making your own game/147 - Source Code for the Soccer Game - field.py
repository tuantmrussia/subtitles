import turtle

def drawField():   #drawing the soccer field.
    
    field = turtle.Turtle()  #creating turtle to draw the soccer field lines.
    field.shape("circle")
    field.hideturtle()
    
    #moving the field turtle around to draw the field.
    field.pencolor("white")
    field.speed(0)
    field.penup()
    field.pensize(3)
    field.goto(400,0)
    field.pendown()
    field.goto(400,275)
    field.goto(-300,275)
    field.goto(-300,-200)
    field.goto(0,-200)
    field.goto(0,60)
    for x in range(180):  #drawing the semi circle.
        field.forward(1)
        field.right(1)    
    field.goto(0,200)
    field.goto(-300,200)
    field.goto(-300,150)
    field.goto(-150,150)
    field.goto(-150,-150)
    field.goto(-300,-150)
    field.pensize(6)
    field.goto(-350,-150)
    field.goto(-350,150)
    field.goto(-300,150)
    field.goto(-300,-150)
    field.pensize(3)
    field.goto(-300,-275)
    field.goto(400,-275)
    field.goto(400,0)
    field.fillcolor("white")
    field.shapesize(2)
    field.showturtle()
    field.stamp()
    field.shapesize(1)
    field.goto(400,114)
    field.setheading(180)
    for x in range(180):
            field.forward(2)
            field.left(1)    
    field.penup()
    field.goto(-75,0)
    field.pensize(6)
    field.stamp()
    field.hideturtle()
    
drawField()  #calling the function.
