
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
import math 

l1 = range(10)
l2 =[]
for i in l1:
    if (i<5 and i!=0):
        l2.append(4)
    elif (i>=5):
        l2.append(i*i)
    elif (i==0):
        l2.append(0)
    
plt.plot(l1,l2)
plt.show()











