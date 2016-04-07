
# coding: utf-8

# In[8]:

def HighLowGame():
    print 'Think your number (1~10)'
    print 'you have to answer question using yes or no'
    FQ=raw_input("Your number is higher than 5?: ")
    if FQ=="yes":
        SQ1=raw_input("Your number is lower than 7?: ")
        if SQ1=="yes":
            print "6"
        elif SQ1=="no":
            SA1=raw_input("Your number is 7?: ")
            if SA1=="yes":
                print "7"
            elif SA1=="no":
                TQ1=raw_input("Your number is lower than 9?: ")
                if TQ1=="yes":
                    print "8"
                elif TQ1=="no":
                    TA1=raw_input("Your number is 9?: ")
                    if TA1=="yes":
                        print "9"
                    elif TA1=="no":
                        print "10"
    elif FQ=="no":
        SQ2=raw_input("Your number is 5?: ")
        if SQ2=="yes":
            print "5"
        elif SQ2=="no":
            SA2=raw_input("Your number is higher than 3?: ")
            if SA2=="yes":
                print "4"
            elif SA2=="no":
                TQ2=raw_input("Your number is 3?: ")
                if TQ2=="yes":
                    print "3"
                elif TQ2=="no":
                    TA2=raw_input("Your number is higher than 1?: ")
                    if TA2=="yes":
                        print "2"
                    elif TA2=="no":
                        print "1"


# In[9]:

HighLowGame()

