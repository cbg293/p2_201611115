
# coding: utf-8

# In[1]:

def gamestart():
    import turtle
    t1=turtle.Turtle()
    wn=turtle.Screen()
    def right():
        t1.right(90)
    def left():
        t1.left(90)
    def down():
        t1.back(10)
    def up():
        t1.fd(10)
    def drawTriangle(size,pos):
        t1.penup()
        t1.setpos(pos)
        t1.pendown()
        for i in range(3):
            t1.fd(size)
            t1.right(120)
    def drawSquare(size,pos):
        t1.penup()
        t1.setpos(pos)
        t1.pendown()
        for i in range(4):
            t1.fd(size)
            t1.right(90)
    def drawStar(size,pos):
        t1.penup()
        t1.setpos(pos)
        t1.pendown()
        for i in range(5):
            t1.fd(size)
            t1.right(144)
    def shape():
        drawTriangle(30,(-100,100))
        drawSquare(30,(0,100))
        drawStar(30,(100,100))
    shape()
    score=0
    t1.penup()
    t1.home()
    
    wn.onkey(right, "d")
    wn.onkey(up, "w")
    wn.onkey(left, "a")
    wn.onkey(bac, "s")
    wn.listen()
    wn.exitonclick()

