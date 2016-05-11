import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
t2.penup()
t2.goto(0,95)
t2.pendown()
t2.fd(50)

def keyup():
    t1.fd(50)

def keydown():
    t1.back(50)

def keyleft():
    t1.left(90)

def keyright():
    t1.right(90)

def gomouse(x,y):
    t1.setpos(x,y)
    t1.pos=(x,y)
    if 0<x<50 and 90<y<100:
        print "Correct"

def addkeys():
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down")
    wn.onkey(keyleft,"Left")
    wn.onkey(keyright,"Right")

def addmouse():
    wn.onclick(gomouse)

addmouse()
addkeys()
wn.listen()
turtle.mainloop()