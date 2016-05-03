
# coding: utf-8

# In[17]:

def charCount(word,dict):
    sentence=word
    d=dict()
    for c in sentence:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    print d
    import matplotlib
    import matplotlib.pyplot as plt

    plt.bar(range(len(d)),d.values())
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()


# In[18]:

def alphadigitcount(words):
    d=dict()
    d={"wordtime":0,"numbertime":0}
    for c in words:
        if c.isdigit()==True:
            d["wordtime"]+=1
        elif c.isalpha()==True:
            d["numbertime"]+=1
    import matplotlib
    import matplotlib.pyplot as plt

    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()


# In[19]:

def findDifference():
    mhouse=set()
    fhouse=set()
    mhouse={'TV','notebook','microwave','robot cleaner','air conditional','refrigerator','vacuum cleaner','hometheater','headset','coffee fort'}
    fhouse={'computer','standing lamp','gas stove','notebook','headset','coffee fort','microwave','TV','charger','robot'}
    print mhouse
    print fhouse
    difference=mhouse.difference(fhouse)
    difference2=fhouse.difference(mhouse)
    intersection=mhouse.intersection(fhouse)
    union=mhouse.union(fhouse)
    print difference
    print difference2
    print intersection
    print union
    d=dict()
    for c in mhouse:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    for c in fhouse:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    print d


# In[20]:

def lab1():
    word=raw_input("Input your words: ")
    charCount(word,dict)


# In[21]:

def lab2():
    words=raw_input("input your words: ")
    alphadigitcount(words)


# In[22]:

def lab3():
    findDifference()


# In[23]:

def main():
    lab1()
    lab2()
    lab3()


# In[24]:

main()

