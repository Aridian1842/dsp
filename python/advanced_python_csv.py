
# coding: utf-8

# In[1]:

import string

import pandas as pd

from pandas import Series


# #### Q1. Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

# In[2]:

df = pd.read_csv('faculty.csv', skipinitialspace=True)


# #### Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

# In[20]:

df['email'].str.cat(sep=', ')


# In[21]:

print df['email'].tolist()


# #### Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

# In[22]:


def get_domain(email):
    at_loc = email.find('@')
    return email[at_loc+1:]


# In[23]:

# test get_domain function
get_domain('bellamys@mail.med.upenn.edu')


# In[24]:

df['email_domain'] = df['email'].map(get_domain)


# #### Q5.  Write email addresses from Part I to csv file

# In[27]:

df['email'].to_csv(path='emails.csv', index=False)