
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


# #### Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

# In[15]:

df['title'].value_counts()


# In[16]:

#Fix "Assistant Professor is Biostatistics" to "Assistant Professor of Biostatistics" for consistency
def clean_title(title):
    return title.replace(' is ', ' of ')


# In[17]:

df['title_clean'] = df['title'].map(clean_title)


# #### Q6.  Create a dictionary in the below format:
# ```
# faculty_dict = { 'Ellenberg': [\
#               ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
#               ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
#                             ],
#               'Li': [\
#               ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
#               ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
#               ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
#                             ]
#             }
# ```
# Print the first 3 key and value pairs of the dictionary

# In[28]:

def get_last_name(name):
    last_name_loc = name.rfind(' ') + 1
    return name[last_name_loc:]


# In[29]:

df['last_name'] = df['name'].apply(get_last_name)


# In[30]:

df['list_info']=df[['degree','title_clean','email']].values.tolist()


# In[31]:

# use a dictionary comprehension to structure the dictionary format
faculty_dict = {k: g['list_info'] for k,g in df.groupby("last_name")}


# In[32]:

def print_first_three_dict(dictionary):
    counter = 0
    for key, val in dictionary:
        print 'Key: ' + str(key)
        for v in val:
            print 'Value: ' + str(v)
        counter += 1
        if counter >= 3:
            break


# In[33]:

# Print the first 3 key and value pairs of the dictionary
print_first_three_dict(faculty_dict.items())


# #### Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:
#
# ```
# professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
#                 ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],\
#                 ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
#                 ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
#                 ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
#             }
# ```
#
# Print the first 3 key and value pairs of the dictionary

# In[34]:

def get_first_name(name):
    first_name_end_loc = name.find(' ')
    return name[:first_name_end_loc]


# In[35]:

df['first_name']= df['name'].apply(get_first_name)


# In[36]:

# use a dictionary comprehension to structure the new dictionary format
professor_dict = {k: g['list_info'] for k,g in df.groupby(['first_name','last_name'])}


# In[37]:

# Print the first 3 key and value pairs of the dictionary

print_first_three_dict(professor_dict.items())


# #### Q8.  It looks like the current dictionary is printing by first name.  Sort by last name and print the first 3 key and value pairs.

# In[38]:

print_first_three_dict(sorted(professor_dict.items(), key=lambda t: t[0][1]))