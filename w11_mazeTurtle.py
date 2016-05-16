
# coding: utf-8

# In[ ]:

import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
wn.bgpic("myMaze.gif")

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


# In[ ]:



