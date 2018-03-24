
# coding: utf-8

# In[11]:


import math

l1 = [ i*i for i in range(11)if i%3==0 or i%5 ==0]
print(l1)

print()
l2 = [ i for i in "python" if i in "aioue"]
print(l2)

print()
l3 = [math.sqrt(200-(i*i)) for i in range(10)]
print(l3)


