
# coding: utf-8

# In[2]:


a = input("enter the string")
for i in a:
    if(a == a[::-1]):
        flag = True
    else :
        flag = False
        print('NOT A PALINDROME')
        break

print("yes palindrome")





