
# coding: utf-8

# In[2]:


import pandas as pd
data = [ ["a",10 , "a@gmail.com" , 1234] , ["b", 12 , "b@gmail.com " , 1254 ] , ["c", 13 , "c@gmail.com", 2345]]
df = pd.DataFrame(data , columns = ["NAme" , "age" , "email", "phone_no"])
print(df)







