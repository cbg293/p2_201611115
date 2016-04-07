
# coding: utf-8

# In[7]:

def calculateyear():
    year=int(raw_input('input user year: '))
    if (year%4 == 0) and (year%100 !=0 or year%400==0):
        print 'this year is yoon year'
    else:
        print 'this year is not yoon year'


# In[8]:

calculateyear()

