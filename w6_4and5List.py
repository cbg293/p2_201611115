
# coding: utf-8

# In[10]:

def sumList(aList):
    x=list()
    for i in range(0,aList):
        if (i%4== 0 and i%5 != 0):
            x.append(i)
    mysum = 0
    for o in range(0,len(x)):
        mysum = mysum+x[o]
    return mysum
    
def lab6():
    aList=1001
    labsum=sumList(aList)
    print labsum

def main():
    lab6()

if __name__=="__main__":
        main()


# In[13]:

main()

