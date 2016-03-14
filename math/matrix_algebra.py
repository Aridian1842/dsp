
# coding: utf-8

# In[1]:

import numpy as np


# #### Matrix Dimensions

# In[2]:

A = np.array([[1,2,3],[2,7,4]])


# In[3]:

A.shape
# (2,3)


# In[4]:

B = np.array(((1,-1),(0,1)))


# In[5]:

B.shape
#(2,2)


# In[6]:

C = np.array([[5,-1],[9,1],[6,0]])


# In[7]:

C.shape
#(3,2)


# In[8]:

D = np.array([[3,-2,-1],[1,2,3]])


# In[9]:

D.shape
#(2,3)


# In[10]:

u = np.array([6,2,-3,5])


# In[11]:

u.shape
#(4,)


# In[12]:

v = np.array([3,5,-1,4])


# In[13]:

v.shape
#(4,)


# In[14]:

w = np.array([[1],[8],[0],[5]])


# In[15]:

w.shape
#(4,1)


# #### Vector Operations

# In[16]:

print u + v
# [ 9 7 -4 9]


# In[17]:

print u - v
# [ 3 -3 -2 1]


# In[18]:

alpha = 6


# In[19]:

print alpha * u
# [ 36 12 -18 30]


# In[20]:

print np.dot(u,v)
#51


# In[21]:

print np.linalg.norm(u)
#8.60232526704


# #### Matrix Operations

# In[22]:

print A + C
#not defined


# In[23]:

print A - C.T
# [[-4 -7 -3] [ 3 6 4]]


# In[24]:

print C.T + 3 * D
# [[14 3 3] [ 2 7 9]]


# In[25]:

print np.dot(B,A)
# [[-1 -5 -1] [ 2 7 4]]


# In[26]:

print np.dot(B,A.T)
# not defined


# In[27]:

print np.dot(B,C)
# not defined


# In[28]:

print np.dot(C,B)
# [[ 5 -6] [ 9 -8] [ 6 -6]]


# In[29]:

print B**4
# [[1 1] [0 1]]


# In[30]:

print np.dot(A,A.T)
# [[14 28] [28 69]]


# In[31]:

print np.dot(D.T,D)
# [[10 -4 0] [-4 8 8] [ 0 8 10]]


# In[ ]:



