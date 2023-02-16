#!/usr/bin/env python
# coding: utf-8

# In[5]:


pac = '''<>,.#@!%^&*(){}[]|\/*"";:/?`~$#@!&'''
A  = input('Entrr the extension = ')
empty = ''
for i in A:
    if i not in pac:
        empty=empty+i
print('empty',empty)


# In[6]:


A = []
size =  int(input("Entr the value "))
for i in range(size):
    val= eval(input("Enter the value add = "))
    A.append(val)
print("origal",A)
lef = A[0]
for i in range(1,size):
    A[i-1]=A[i]
A[i]=lef
print(A)


# In[ ]:




