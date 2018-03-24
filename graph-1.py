
# coding: utf-8

# In[7]:


get_ipython().run_line_magic('matplotlib', 'notebook')


import math as m1
import matplotlib.pyplot as plt
y1 = []
x1 = range(1,10)
for j in x1:
    y = m1.sqrt(500- j*j)
    y1.append(y)

plt.plot(x1,y1)
plt.show()







