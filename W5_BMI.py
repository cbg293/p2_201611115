
# coding: utf-8

# In[13]:

def yourBMI():
    weight=raw_input('write your weight(kg): ')
    height=raw_input('write your height(m): ')
    BMI=float(weight)/(float(height)*float(height))
    if BMI>=18.5 and BMI<25:
        res="normal weight"
    elif BMI>=25 and BMI<30:
        res="overweight"
    elif BMI>=30 and BMI<40:
        res="obesity"
    else:
        res="over obesity"
    return res


# In[14]:

yourBMI()

