
# coding: utf-8

# In[2]:

my2dlist=[
[74425, 76326],
[61164, 61636],
[109688, 115744],
[144796, 146776],
[174996, 181676],
[177841, 177434],
[204630, 205980],
[223373, 232245],
[161055, 166130],
[171576, 176735],
[279169, 293772],
[239450, 251066],
[148690, 156510],
[182977, 196992],
[237792, 242641],
[283869, 296762],
[209344, 210282],
[118965, 114441],
[186503, 186856],
[195734, 203014],
[254381, 249472],
[212401, 229111],
[271654, 295354],
[319197, 335045],
[229829, 231671]]

Gu=['Jongno','Jung','Yongsan','Seongdong',
    'Gwangjin','Dongdaemun', 'Jungnang', 
    'Seongbuk','Gangbuk','Dobong','Nowon',
    'Eunpyeong','Seodaemun','Mapo','Yangcheon',
    'Gangseo','Guro','Geumcheon','Yeongdeungpo',
    'Dongjak','Gwanak','Seocho','Gangnam',
    'Songpa', 'Gangdong']

sumM=0
sumW=0
sum=0
for i in my2dlist:
    sumM=sumM+i[0]
print "Man:",sumM
for i in my2dlist:
    sumW=sumW+i[1]
print "Woman:",sumW
averageM=sumM/25
print "Man average:",averageM
averageW=sumW/25
print "Woman average:",averageW

print "Gu:"
for i in my2dlist:
    sum_gu=i[0]+i[1]
    print sum_gu,
    
print "Gu average:"
for i in my2dlist:
    average_gu=(i[0]+i[1])/2
    print average_gu,


# In[3]:

d=dict()
for i in range(25):
    d.update({Gu[i]:my2dlist[i][0]+my2dlist[i][1]})
    
import matplotlib 
import matplotlib.pyplot as plt 
plt.bar(range(len(d)),d.values(), align='center') 
plt.xticks(range(len(d)), d.keys()) 
plt.show() 

