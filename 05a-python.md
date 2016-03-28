# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?
```
Lists and tuples are both sequences of elements of any type. However, lists are mutable and tuples are not mutable, which basically means list elements can be motified after initialization (ex: cheeses[0] = "Cheddar") and tuples cannot. Lists can leverage keys in dictionaries due to this.
```
---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?
```
Lists and sets are both sequences of elements of any type and are mutable. However lists cannot have duplicate data and have no index. Lists perform better on iterating over values (looping) but sets are better for checking values in a set or common operations across sets.
```
---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.
```
Lambda is an anonymous function in Python that can be used to build functions and are resticted to a single expression. They are generally used for one-off functions only used once. For instance, a lambda function can directly specify a function in the `key` argument in the sorted function. The example below shows this for sorting from A to Z regardless of lower or uppercase in the list:

sorted(['red', 'Orange', 'Green', 'blue'], key = lambda word: word.lower())
['blue', 'Green', 'Orange', 'red']
```
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.
```
List comprehensions provide a way to create lists using bracket operators, expression inside the brackets that specifies the elements of a list and a for clause that indicates the sequence to be traversed. List comprehensions example below and equivalent results using `map` and `filter`:

LIST

cubes = [x**3 for x in range (5)]
print cubes


MAP

def cube(x):
   return x**3

cubes = map(cube, range(5))
print cubes


FILTER (not sure what equivalent list or map function, but showed filter example here)

cubes_adj = filter(lambda x: x > 20, cubes)
print cubes_adj


SET COMPREHENSION

set = [x**3 for x in range(5)]
print set
```

DICTIONARY COMPREHENSION
```
dict = {k:v for (k,v) in zip(keys, values)}
print dict
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





