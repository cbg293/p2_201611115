
# coding: utf-8

# In[1]:

import turtle
import math
wn=turtle.Screen()
t1=turtle.Turtle()

def drawSquare():
    t1.penup()
    t1.goto(100,100)
    t1.pendown()
    for i in range(0,4):
        t1.fd(100)
        t1.left(90)
    t1.penup()

def drawLine():
    t1.setheading(0)
    t1.penup()
    t1.goto(0,350)
    t1.pendown()
    t1.fd(100)
    t1.penup()
 
def drawCircle():
    t1.penup()
    t1.home()
    t1.pendown()
    t1.circle(100)
    t1.penup()

def cl(curpos):
    if 330<curpos[0]<390 and -250<curpos[1]<-150:
        t1.goto(-320,300)
        print "Good"

coord = [(100,100),(200,200)]
xs=coord[0][0]
ys=coord[0][1]
xe=coord[1][0]
ye=coord[1][1]

def isinRectangle(coord,curpos):
    if xs<=curpos[0]<=xe and ys<=curpos[1]<=ye:
        t1.color("blue")

line=[(0,350),(0,350)]
x1=line[0][0]-5
y1=line[0][1]-5
x2=line[1][0]+5
y2=line[1][1]+5
pos1=(x1,y1)
pos2=(x2,y2)

def isOnLine(curpos,pos1,pos2):
    if x1<=curpos[0]<=x2 and y1<=curpos[1]<=y2:
        t1.color("Green")

circlepos=(0,100)
radious=100


def isinCircle(curpos,radious,circlepos):
    if math.sqrt(math.pow(curpos[0]-circlepos[0],2) + math.pow(curpos[1]-circlepos[1],2))<=100:
        t1.color("yellow")

def Draw():
    drawSquare()
    drawLine()
    drawCircle()

def keyup():
    t1.fd(50)
    curpos=t1.pos()
    cl(curpos)
    isinRectangle(coord,curpos)
    isOnLine(curpos,pos1,pos2)
    isinCircle(curpos,radious,circlepos)

def keydown():
    t1.back(50)
    curpos=t1.pos()
    cl(curpos)
    isinRectangle(coord,curpos)
    isOnLine(curpos,pos1,pos2)
    isinCircle(curpos,radious,circlepos)
    
def turnright():
    t1.right(90)
    curpos=t1.pos()
    cl(curpos)
    isinRectangle(coord,curpos)
    isOnLine(curpos,pos1,pos2)
    isinCircle(curpos,radious,circlepos)
    
def turnleft():
    t1.left(90)
    curpos=t1.pos()
    cl(curpos)
    isinRectangle(coord,curpos)
    isOnLine(curpos,pos1,pos2)
    isinCircle(curpos,radious,circlepos)

def mousegoto(x,y):
    t1.setpos(x,y)
    curpos=t1.pos()
    cl(curpos)
    isinRectangle(coord,curpos)
    isOnLine(curpos,pos1,pos2)
    isinCircle(curpos,radious,circlepos)

def addkeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keydown, "Down")
    wn.onkey(turnright, "Right")
    wn.onkey(turnleft, "Left")
def addmouse():
    wn.onclick(mousegoto)
    
Draw()
addkeys()
addmouse()
wn.listen()
turtle.mainloop()

