# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

####Similarities
- Sequence of values
- Values can be any type
- Indexed by integers
- Share similar operators (e.g., bracket, slice, relational)

####Differences
- Lists are mutable. Tuples are immutable
- Can use tuples as keys in dictionaries but not lists, because dictionary keys need to be immutable
- In some contexts, like a return statement, it is syntactically simpler to create a tuple than a list.
- If you are passing a sequence as an argument to a function, using tuples reduces the potential for unexpected behavior due to aliasing (as opposed to lists)
- Lists have built-in methods of sort and reverse while tuples do not (because the methods modify the existing sequence)



---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?


####Similarities
- Collections of values
- Mutable
- Cannot be used as keys to a dictionary

####Differences
- Lists keep order, sets do not
- Sets do not support indexing, slicing, or other sequence-like behavior that lists support
- Set requires items to be hashable, list doesn't
- set forbids duplicates, list does not
- Finding an element in a set is significantly faster, O(1), than in a list which takes time proportional to the list's length in the average and worst cases, O(n)

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

A `lambda` function is a small anonymous function that can be used wherever function objects are required, such as passing a function as a argument to another function. They are a form of a higher-order function which allows us to abstract over actions, not just values.

example:

```python
student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions provide a concise and readable way to create lists, such as making new lists where each element is the result of some operations applied to each member of another sequence or iterable. Another use-case is creating a subsequence of those elements that satisfy a certain condition.

```python
import numpy as np

squares = []

#creating an array of the first ten positive integer squares without using list comprehensions, map, or filter
for x in range(10):
     squares.append(x**2)

print squares
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#creating an array of the first ten positive integer squares using a list comprehension
squares = [x**2 for x in range(10)]

print squares
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#creating an array of the first ten positive integer squares using map
def square(x):
    return x**2

squares = map(square, range(10))
print squares
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#creating an array of the first ten positive integer squares using filter (knowing that squares of first 10 integers are all less than 100)
squares = filter(lambda x: np.sqrt(x).is_integer(),range(100))
print squares
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#set comprehension example
a = {x for x in 'abracadabra' if x not in 'abc'}
print a
#set(['r', 'd'])

#dictionary comprehension example
d = {n: n**2 for n in range(5)}
print d
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.
a.

```
date_start = '01-02-2013'
date_stop = '07-28-2015'
```

>> 937 days

b.
```
date_start = '12312013'
date_stop = '05282015'
```

>> 513 days

c.
```
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





