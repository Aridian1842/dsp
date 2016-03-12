
# coding: utf-8

# In[1]:

import string

import pandas as pd

from pandas import Series


# #### Q1. Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

# In[2]:

df = pd.read_csv('faculty.csv', skipinitialspace=True)


# In[3]:

df.head()


# In[4]:

#clean the degree column by addressing certain issues with the data (degree='0' and differences in punctuation)
def clean_degree(degree_str):
    if degree_str == '0':
        degree_str = 'None'
    else:
        exclude = set(string.punctuation)
        degree_str = ''.join(ch for ch in degree_str if ch not in exclude)
    return degree_str


# In[5]:

#make a copy of the df for use in later steps
df2 = df


# In[6]:

#standardize/clean the degree column
df2['degree_list'] = df2['degree'].map(clean_degree)


# In[7]:

df2['degree_list']


# In[8]:

#create a stacked series that results from splitting the degree column, maintaining the reference to the original
#df index so can re-join to the original df
#taken from http://stackoverflow.com/questions/17116814/pandas-how-do-i-split-text-in-a-column-into-multiple-rows
s = df2['degree_list'].str.split(' ').apply(Series, 1).stack()


# In[9]:

#make sure the series indexes align with the original df indexes
s.index = s.index.droplevel(-1)


# In[10]:

#give the series a name so we can join to it
s.name = 'degree_list'


# In[11]:

#delete the degree_list column and re-add it with the join
del df2['degree_list']

df2 = df2.join(s)



# In[13]:

#print frequency of degrees
print df2['degree_list'].value_counts()


# In[14]:

#use describe to get summary info, including the number of unique degrees
print df2['degree_list'].describe()


# #### Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

# In[15]:

df['title'].value_counts()


# In[16]:

#Fix "Assistant Professor is Biostatistics" to "Assistant Professor of Biostatistics" for consistency
def clean_title(title):
    return title.replace(' is ', ' of ')


# In[17]:

df['title_clean'] = df['title'].map(clean_title)


# In[18]:

#print frequency of titles
print df['title_clean'].value_counts()


# In[19]:

#use describe to get summary info, including the number of unique titles
df['title_clean'].describe()


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


# In[25]:

print df['email_domain'].value_counts()


# In[26]:

print df['email_domain'].describe()
