
# coding: utf-8

# In[7]:


import numpy as np
a = np.array([1,2,3])
a.shape = (3,1)
print(a)
print()

b = np.array([[1,2,3],[4,5,6]], dtype = 'float')
b.shape = (3,2)
print(b)
print()

c = np.array([[5,6],[44,55],[43,78]],dtype = 'complex')
print(np.transpose(c))
print()
print(c)


