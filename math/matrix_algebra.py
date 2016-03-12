# Matrix Algebra


# coding: utf-8

# In[1]:

import numpy as np


# #### Matrix Dimensions

# In[2]:

A = np.array([[1,2,3],[2,7,4]])


# In[3]:

A.shape


# In[4]:

B = np.array(((1,-1),(0,1)))


# In[5]:

B.shape


# In[6]:

C = np.array([[5,-1],[9,1],[6,0]])


# In[7]:

C.shape


# In[8]:

D = np.array([[3,-2,-1],[1,2,3]])


# In[9]:

D.shape


# In[10]:

u = np.array([6,2,-3,5])


# In[11]:

u.shape


# In[12]:

v = np.array([3,5,-1,4])


# In[13]:

v.shape


# In[14]:

w = np.array([[1],[8],[0],[5]])


# In[15]:

w.shape


# #### Vector Operations

# In[16]:

print u + v


# In[17]:

print u - v


# In[18]:

alpha = 6


# In[19]:

print alpha * u


# In[20]:

print np.dot(u,v)


# In[21]:

print np.linalg.norm(u)


# #### Matrix Operations

# In[22]:

print A + C


# In[23]:

print A - C.T


# In[24]:

print C.T + 3 * D


# In[25]:

print np.dot(B,A)


# In[26]:

print np.dot(B,A.T)


# In[27]:

print np.dot(B,C)


# In[28]:

print np.dot(C,B)


# In[29]:

print B**4


# In[30]:

print np.dot(A,A.T)


# In[31]:

print np.dot(D.T,D)


# In[ ]:




