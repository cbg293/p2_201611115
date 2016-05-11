
# coding: utf-8

# In[2]:

def Coffee():

    allData=list()

    allData=[["Coffee","Water","Milk","Icecream"],
    ["Espresso","No","No","No"],
    ["Long Black","Yes","No","No"],
    ["Flat White","No","Yes","No"],
    ["Cappuccino","No","Yes - Frothy","No"],
    ["Affogato","No","No","Yes"]]

    Data=allData[1:]

    milk=0
    nomilk=0

    for i in Data:
        if i[2]=="No":
            nomilk=nomilk+1
        else:
            milk=milk+1

    print "milk :",float(milk)/len(Data)*100,"%"," nomilk :",float(nomilk)/len(Data)*100,"%"
    
def Marks():
        
    marks=list()

    marks=[["English",100],
          ["Math",200],
          ["English",200],
          ["Math",200],
          ["English",100],
          ["Math",300]]

    Eng=0
    Eng_sum=0
    Math=0
    Math_sum=0

    for i in marks:
        if i[0]=="English":
            Eng_sum+=i[1]
            Eng+=1

        elif i[0]=="Math":
            Math_sum+=i[1]
            Math+=1

    print "Sum of English:",Eng_sum
    print "Average of English:",Eng_sum/Eng
    print "Sum of Math:",Math_sum
    print "Average of Math:",Math_sum/Math

def Letitbe():
        
    lyrics=list()

    lyrics=[

        "When I find myself in times of trouble",

        'Mother Mary comes to me',

        'Speaking words of wisdom let it be',

        'And in my hour of darkness',

        'She is standing right in front of me',

        'Speaking words of wisdom let it be',

        'Let it be let it be',

        'Let it be let it be',

        

        'Whisper words of wisdom let it be',

        'And when the broken-hearted people',

        'Living in the world agree',

        'There will be an answer let it be',

        'For though they may be parted',

        'There is still a chance that they will see',

        'There will be an answer let it be',

     

        'Let it be let it be',

        'Let it be let it be',

        'Yeah there will be an answer let it be',

        'Let it be let it be',

        'Let it be let it be',

        'Whisper words of wisdom let it be',

     

        'Let it be let it be',

        'Ah let it be yeah let it be',

        'Whisper words of wisdom let it be',

     

        'And when the night is cloudy',

        'There is still a light that shines on me',

        'Shine on until tomorrow let it be',

        'I wake up to the sound of music',

        'Mother Mary comes to me',

        'Speaking words of wisdom let it be',

     

        'Let it be let it be',

        'Let it be yeah let it be',

        'Oh there will be an answer let it be',

        'Let it be let it be',

        'Let it be yeah let it be',

        'Whisper words of wisdom let it be']

     

    doc=lyrics

    d=dict()

    for line in doc:
        for c in line.split():
            if c not in d:
                d[c]=1
            else:
                d[c]=d[c]+1
                
                
    under20=list()
    over20=list()

    for i in d:
        if d[i]>=20:
            over20.append(i+"("+str(d[i])+")")

        else:
            under20.append(i+"("+str(d[i])+")")

    print "Word that comes more than 20 times : ",over20
    print "Word that comes less than 20 times : ",under20
    
def lab9():
    Coffee()
    Marks()
    Letitbe()
    
def main():
    lab9()

if __name__=="__main__": 
    main()  


# In[ ]:



