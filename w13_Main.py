
# coding: utf-8

# In[1]:

def File():
    try:
        fin1=open('python.txt','a')
        fin2=open('outputNum.txt','r')
        for line in fin2:
            fin1.write(line)
        fin1.close()
        fin2.close()
    except Exception as e:
        print e



# In[2]:

import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def getCoordsFromFile():
    fout=open('reccoords.txt')
    mycoords=[]
    for line in fout:
        line1=line.split(',')
        mycoords.append([(line1[0],line1[1]),(line1[2],line1[3].strip())])
        for coord in mycoords:
            x1=int(coord[0][0])
            x2=int(coord[1][0])
            y1=int(coord[0][1])
            y2=int(coord[1][1])
        coordlist=((x1,y1),(x2,y1),(x2,y2),(x1,y2),(x1,y1))
        t1.penup()
        t1.setpos(coordlist[0])
        t1.pendown()
        for c in coordlist:
            t1.goto(c)   
    fout.close()


# In[ ]:

def lab1(): 
    File()
    
def lab2():
    getCoordsFromFile()
    wn.exitonclick()
    
def main(): 
    lab1()
    lab2()
    
if __name__=="__main__":  
    main()  

