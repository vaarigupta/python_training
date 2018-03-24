
# coding: utf-8

# In[14]:


import numpy as np
import matplotlib.pyplot  as plt
x = np.arange(1,10)
y = np.sqrt(300-(x*x))
plt.title('numpy-program')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x,y, 'ro')
plt.show()

