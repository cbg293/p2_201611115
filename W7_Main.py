
# coding: utf-8

# In[1]:

def drawSquareAtSave(size, pos):
    x=list()
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    track=list()
    for i in range(0,4):
        track.append(t1.pos())
        t1.forward(size)
        t1.right(90)
    return track

def drawSquareFrom(tracks):
    tracks=list()
    tracks.append((-50,-50))
    tracks.append((50,-50))
    tracks.append((50,50))
    tracks.append((-50,50))
    for i in range(0,4):
        t1.goto(tracks[i])
        
def SaveTracks():
    t1.speed(3)
    t1.penup()
    myTracks=list()
    t1.goto(-400,300)
    myTracks.append(t1.pos())
    t1.pendown()
    t1.right(90)
    t1.fd(400)
    myTracks.append(t1.pos())
    t1.backward(150)
    myTracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    myTracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    myTracks.append(t1.pos())
    t1.back(150)
    myTracks.append(t1.pos())
    t1.right(90)
    t1.fd(300)
    myTracks.append(t1.pos())
    t1.left(90)
    t1.right(90)
    t1.right(90)
    t1.fd(200)
    myTracks.append(t1.pos())
    t1.fd(300)
    myTracks.append(t1.pos())
    t1.back(100)
    myTracks.append(t1.pos())
    t1.left(90)
    t1.fd(200)
    myTracks.append(t1.pos())
    return myTracks
        
def replayTracks(myTracks):
    t1.clear()
    t1.speed(3)
    for t in myTracks:
        t1.goto(t)

def lab7():
    global wn
    global t1
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    mytrack=drawSquareAtSave(100,(0,0))
    print mytrack
    drawSquareFrom(100)
    
    myTracks=SaveTracks()
    replayTracks(myTracks)
    
def main():
    lab7()
    
if __name__=="__main__":
    main()


# In[ ]:



