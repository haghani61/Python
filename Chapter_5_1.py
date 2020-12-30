#Do, or do not. There is no try. --Yoda
###############
# CHAPTER 5:Py Boxes: Modules, Packages, and Programs
##############


##  Code has a bottom-up organization: data types are like words, statements are like sentences,
# functions are like paragraphs, and modules are like chapters

###
# Import a Module: A module is just a file of Python code
###
import random

def get_description():
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return random.choice(possibilities)

# use a name that is more mnemonic or shorter
import random as wr

# import only one or more parts of module: 
from random import choice as ch

# Using the dictionary get() function to return
# The setdefault() function is like get(), but also assigns an item to the dictionary if
# the key is missing: 
periodic_table = {'Hydrogen': 1, 'Helium': 2}
periodic_table.setdefault('Carbon', 12)
periodic_table

helium = periodic_table.setdefault('Helium', 947) # different value to existing, original value is returned 
periodic_table

# Create dict with using defaultdict function
from collections import defaultdict
periodic_table = defaultdict(int) # will return 0 for missing value 

periodic_table['test'] = 1
periodic_table['test_1'] = 2
periodic_table['test_2']

periodic_table

# another example: 

from collections import defaultdict

def no_idea():
    return 'huh?' 

bestt= defaultdict(no_idea) # will return huh for missing value

bestt['Ahaha'] = 'Ahaha'
bestt['bhahah'] = 'bhahah'
bestt['c']
bestt

bestt = defaultdict(lambda: 'huh?') # use lambda instead of func.

# 

food_c = defaultdict(int) 

for food in ['spam','spam','eggs','spam']: # if we donot use defaultdict, will get an exception
    food_c[food] +=1

for x, y in food_c.items():
    print(x,y)
    
###
# Count Items with Counter()
###

from collections import Counter

breakfast = ['spam', 'spam','eggs','spam']
breakfast = Counter(breakfast)

#  most_common() function

breakfast.most_common()

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
lunch_counter

breakfast+lunch_counter # combine the two counters is by addition, using + 
breakfast - lunch_counter # breakfast not lunch
lunch_counter - breakfast # lunch not breakfast
breakfast & lunch_counter # intersection 
breakfast | lunch_counter # get all items by using the union operator |:

###
# Order by Key with OrderedDict()
###
from collections import OrderedDict

quotes = OrderedDict([
        ('Moe', 'A wise guy, huh?'),
        ('Larry', 'Ow!'),
        ('Curly', 'Nyuk nyuk!'),
        ])
    
###
# Stack + Queue == deque: is a double-ended queue, which has features of both a stack and a queue
###

# popleft() removes the leftmost item from the deque and returns it
# pop() removes the rightmost item and returns it. 
dq = deque('radar')
dq.popleft() 
dq.pop()
def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
        return True

   
palindrome('a')
palindrome('racecar')
palindrome('')
palindrome('radar')
# reverse a string with a slice
def another_palindrome(word):
    return word == word[::-1]

another_palindrome('racecar')

###
# Iterate over Code Structures with itertools
###
import itertools 
for item in itertools.chain([1, 2], ['a', 'b']): # chain() runs through its arguments as a single iterable
    print(item)

for item in itertools.cycle([1, 2]): # cycle() is an infinite iterator
    print(item)
  
 
for item in itertools.accumulate([1, 2, 3, 4]): # accumulate() calculates accumulated values
    print(item)
# function as the second argument to accumulate()
def multiply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)
###
# Print Nicely with pprint()
###
from pprint import pprint

quotes = OrderedDict([
      ('Moe', 'A wise guy, huh?'),
      ('Larry', 'Ow!'),
      ('Curly', 'Nyuk nyuk!'),
      ])

print(quotes)
pprint(quotes)

#################
# Things to Do
#################

# Make a dictionary called plain with the key-value pairs 'a': 1, 'b': 2, and 'c':
 # 3, and then print it.
plain = {'a': 1, 'b': 2, 'c': 3}

# Make an OrderedDict called fancy from the same pairs and print it. Did it print in
  # the same order as plain?
from collections import OrderedDict
fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
fancy

# Make a defaultdict called dict_of_lists and pass it the argument list. Make the
  # list dict_of_lists['a'] and append the value 'something for a' to it in one assignment.
  # Print dict_of_lists['a'].
  
from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
dict_of_lists['a']

