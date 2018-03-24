
# coding: utf-8

# In[10]:


import pandas as pd
data=[['SALONI ',19] , ['preeti',20]]
df = pd.DataFrame(data )
print(df)










# In[12]:


df = pd.DataFrame(data , columns = ['Name' , 'Age'])
print(df)






# In[16]:


df["Name"]

