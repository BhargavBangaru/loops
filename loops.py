#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(5):
    for j in range(5-i):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    print()


# In[2]:


for i in range(5):
    for j in range(5-i):
        print("* ",end="")
    print()


# In[9]:


n=int(input("enter a num:"))
for i in range(2,n):
    for j in range(2,i):
        if (i%j==0):
            break
    else:
        print(i)
    


# In[13]:


n=int(input("enter a num:"))
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(n))


# In[22]:


f=int(input("enter a num:"))
fact=1
for i in range(1,f+1):
    fact*=i
fact


# In[21]:


#while loop


# In[20]:


hungry="yes"
while hungry=="yes":
    print("eat more")
    hungry=input("are you still hungry?")
print("eating done")


# In[26]:


f=int(input("enter a num:"))
fact=1
while f>1:
    fact*=f
    f-=1
fact


# In[ ]:




