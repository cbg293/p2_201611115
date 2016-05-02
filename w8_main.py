
# coding: utf-8

# In[1]:

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


# In[2]:

def lab1():
    word=raw_input("Input your words: ")
    charCount(word,dict)


# In[4]:

def main():
    lab1()


# In[ ]:



