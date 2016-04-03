
# coding: utf-8

# In[8]:

def GawiBawiBo():
    A=raw_input('A input Gawi or Bawi or Bo: ')
    B=raw_input('B input Gawi or Bawi or Bo: ')
    if A=='Gawi':
        if B=='Bo':
            print "A is win"
        if B=='Bawi':
            print "B is win"
    if A=='Bawi':
        if B=='Bo':
            print "B is win"
        if B=='Gawi':
            print "A is win"
    if A=='Bo':
        if B=='Gawi':
            print "B is win"
        if B=='Bawi':
            print "A is win"
    if A==B:
        print "draw"

    



# In[9]:

GawiBawiBo()

