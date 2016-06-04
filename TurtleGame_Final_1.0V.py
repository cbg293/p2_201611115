
# coding: utf-8

# In[1]:

import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
t2.shape("turtle")
t2.color("Brown")
wn.setup(450,800)


# In[2]:

def drawMap():
    t1.right(90)
    t1.penup()
    t1.fd(350)
    t1.pendown()
    t1.fillcolor("skyblue")
    t1.begin_fill()
    t1.right(90)
    t1.fd(200)
    t1.right(90)
    t1.fd(700)
    t1.right(90)
    t1.fd(400)
    t1.right(90)
    t1.fd(700)
    t1.right(90)
    t1.fd(200)
    t1.end_fill()


# In[3]:

def drawBlock1():
    frec=open('Block1.txt')
    mycoords=[]
    for line in frec:
        line1=line.split(',')
        mycoords.append([(line1[0],line1[1]),(line1[2],line1[3].strip())])
        for coord in mycoords:
            x1=int(coord[0][0])
            x2=int(coord[1][0])
            y1=int(coord[0][1])
            y2=int(coord[1][1])
        coord_li=((x1,y1),(x2,y1),(x2,y2),(x1,y2),(x1,y1))
        t1.penup()
        t1.setpos(coord_li[0])
        t1.pendown()
        t1.fillcolor("Black")
        t1.begin_fill()
        for c in coord_li:
            t1.goto(c)
        t1.end_fill()
    frec.close()


# In[4]:

def drawBlock2():
    frec=open('Block2.txt')
    mycoords=[]
    for line in frec:
        line1=line.split(',')
        mycoords.append([(line1[0],line1[1]),(line1[2],line1[3].strip())])
        for coord in mycoords:
            x1=int(coord[0][0])
            x2=int(coord[1][0])
            y1=int(coord[0][1])
            y2=int(coord[1][1])
        coord_li=((x1,y1),(x2,y1),(x2,y2),(x1,y2),(x1,y1))
        t1.penup()
        t1.setpos(coord_li[0])
        t1.pendown()
        t1.fillcolor("Black")
        t1.begin_fill()
        for c in coord_li:
            t1.goto(c)
        t1.end_fill()
    frec.close()


# In[5]:

def drawEndzone():
    t1.penup()
    t1.setpos(40,200)
    t1.pendown()
    t1.fillcolor("Yellow")
    t1.begin_fill()
    for i in range(0,4):
        t1.fd(80)
        t1.right(90)
    t1.end_fill()
    t1.penup()
    t1.fd(60)
    t1.right(90)
    t1.fd(40)
    t1.write("End Zone")


# In[6]:

def t2set():
    t2.penup()
    t2.setpos(0,-330)
    t2.write("Go to Endzone, avoiding mines")


# In[7]:

def GameStart():
    drawMap()
    drawBlock1()
    drawBlock2()
    drawEndzone()
    t2set()


# In[8]:

def out():
    (x,y)=t2.pos()
    if x<=-199:
        t2.goto(0,-330)
    if 199<=x:
        t2.goto(0,-330)
    if y<=-349:
        t2.goto(0,-330)
    if 349<=y:
        t2.goto(0,-330)
    if -109<=x<=-55 and -300<=y<=-150:
        t2.goto(0,-330)
    if 55<=x<=109 and -300<=y<=-150:
        t2.goto(0,-330)
    if -109<=x<=-55 and -50<=y<=150:
        t2.goto(0,-330)
    if 55<=x<=109 and -50<=y<=150:
        t2.goto(0,-330)


# In[9]:

def end():
    (x,y)=t2.pos()
    if -40<=x<=40 and 220<=y<=300:
        t1.penup()
        t1.speed(1000)
        t1.setpos(40,200)
        t1.pendown()
        t1.setheading(180)
        t1.fillcolor("Green")
        t1.begin_fill()
        for i in range(0,4):
            t1.fd(80)
            t1.right(90)
        t1.end_fill()
        t1.penup()
        t1.fd(60)
        t1.right(90)
        t1.fd(40)
        t1.write("End Zone")


# In[10]:

def mine():
    (x,y)=t2.pos()
    if -55<=x<=55 and -250<=y<=-200:
        t1.penup()
        t1.speed(1000)
        t1.setpos(-40,-250)
        t1.pendown()
        t1.setheading(0)
        t1.fillcolor("Red")
        t1.begin_fill()
        for i in range(0,4):
            t1.fd(80)
            t1.left(90)
        t1.end_fill()
        t1.penup()
        t1.fd(30)
        t1.left(90)
        t1.fd(30)
        t1.write(" BOOM!!!! ")
        t2.goto(0,-330)
    
    if 109<=x<=200 and -250<=y<=-200:
        t1.penup()
        t1.speed(1000)
        t1.setpos(124,-250)
        t1.pendown()
        t1.setheading(0)
        t1.fillcolor("Red")
        t1.begin_fill()
        for i in range(0,4):
            t1.fd(61)
            t1.left(90)
        t1.end_fill()
        t1.penup()
        t1.fd(20)
        t1.left(90)
        t1.fd(20)
        t1.write(" BOOM!!!! ")
        t2.goto(0,-330)
        
    if -200<=x<=-109 and 0<=y<=100:
        t1.penup()
        t1.speed(1000)
        t1.setpos(-185,0)
        t1.setheading(0)
        t1.pendown()
        t1.fillcolor("Red")
        t1.begin_fill()
        for i in range(0,4):
            t1.fd(61)
            t1.left(90)
        t1.end_fill()
        t1.penup()
        t1.fd(20)
        t1.left(90)
        t1.fd(20)
        t1.write(" BOOM!!!! ")
        t2.goto(0,-330)
        
    if -55<=x<=55 and 0<=y<=100:
        t1.penup()
        t1.speed(1000)
        t1.setpos(-40,0)
        t1.setheading(0)
        t1.pendown()
        t1.fillcolor("Red")
        t1.begin_fill()
        for i in range(0,4):
            t1.fd(80)
            t1.left(90)
        t1.end_fill()
        t1.penup()
        t1.fd(30)
        t1.left(90)
        t1.fd(30)
        t1.write(" BOOM!!!! ")
        t2.goto(0,-330)


# In[11]:

def keyup():
    t2.fd(50)
    out()
    end()
    mine()

def keydown():
    t2.back(50)
    out()
    end()
    mine()

def keyleft():
    t2.left(90)
    out()
    end()
    mine()

def keyright():
    t2.right(90)
    out()
    end()
    mine()

def addkeys():
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down")
    wn.onkey(keyleft,"Left")
    wn.onkey(keyright,"Right")


# In[12]:

GameStart()


# In[13]:

addkeys()
wn.listen()
turtle.mainloop()
wn.exitonclick()


# In[ ]:

t1.setpos(40,200)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



