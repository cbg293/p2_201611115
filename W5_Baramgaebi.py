
# coding: utf-8

# In[1]:

import turtle
wn=turtle.Screen()
t1=turtle.Turtle()


# In[2]:

def Baramgaebi(size,sides,bigger,angle):
    for i in range(0,sides):
        if(1%2):
            size=size+bigger
            t1.right(angle)
            t1.fd(size)

    


# In[4]:

t1.home()
t1.clear()
Baramgaebi(30,20,50,90)

