#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

# In[1]:

import random
import sys


# In[2]:

def read_txt_to_array(filename):
    data = ''
    with open(filename, 'r') as myfile:
        data = myfile.read().replace('\n', ' ')
    return data.split()


# In[3]:

#create markov table
def generate_table(arr, shift):
    table = {}

    for x in range(len(arr)-shift):
        new_val = arr[x+shift]
        key = ()
        for z in range(shift):
            key += (arr[x+z],)
        if key in table:
            table[key].append(new_val)
        else:
            table[key] = [new_val]
    return table


# In[4]:

#randomly generate output text
def get_output(table, num_words, shift):
    output = ''
    #choose random key to start with and add the key values to output
    key = random.choice(table.keys())
    for x in key:
        output += x + ' '

    #randomly step through markov table and generate the next value
    for y in range(num_words-shift):
        val = random.choice(table[key])
        output += val + ' '
        key = key[1:]+(val,)
    return output


# In[5]:

def generate_markov_text(filename='markov.txt',num_words=40):
    shift = 2

    txt_array = read_txt_to_array(filename)
    markov_table = generate_table(txt_array, shift)
    output = get_output(markov_table, num_words, shift)
    print output


generate_markov_text(sys.argv[1],int(sys.argv[2]))