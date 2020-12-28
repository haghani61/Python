#Do, or do not. There is no try. --Yoda
###############
# CHAPTER 3
##############

# list and tubles: elements can be different types of Python object. 

## tubles: are immutables while list: is mutables


################
# List
################

# Create with [] or list()

empty_list= []

weekdays =['Monday','Tuesday', 'Wednesday','Thursday','Friday']

another_empty_list = list()

big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']

# Convert Other Data Types to Lists with list()
list('abc')
 
a_tuple=('ready','fire','aim')

list(a_tuple)

name='majid'

name.split('m')

birthday= '1/6/1952'

birthday.split('/') # will give a list

# Get an Item by Using [ offset ]

marxes = ['Groucho', 'Chico', 'Harpo']

marxes[2]
marxes[-1]

### Lists of Lists, # remember, elements in list can be any Python type!!

small_birds= ['hummingbird','finch']

extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]

all_birds

all_birds[0][0]
all_birds

# change item in list: 
marxes = ['Groucho', 'Chico', 'Harpo']

marxes[2]='haha' # Change an Item by [ offset ]

marxes[0:2] # select

marxes[::2]
marxes[::-2]

marxes[::-1] # reverse a list:

# Add an Item to the End with append()

marxes.append('zeppo')

marxes= ['Groucho', 'Chico', 'Harpo', 'Zeppo']

others = ['Gummo','Karl']

marxes.extend(others) # combine 
marxes +=others 

# there is diffence between extend(), and append()
# If we had used append(), others would have been added as a single list item rather than merging its items:
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
marxes

marxes.insert(3,'Gummo') # insert 'Gummo' in list
marxes.insert(10, 'Karl')
# Delete an Item by Offset with del

del marxes[-1] # del is a Python statement, not a list method—you don’t say marxes[-2].del().

marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']

marxes.remove('Gummo')

marxes.pop() # So, pop(0) returns the head (start) of the list, and pop() or pop(-1) returns the tail (end)

marxes.pop(1)

# Find an Item’s Offset by Value with index()

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']

marxes.index('Chico') # index will give position of an item in list

# Test for a Value with in

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']

'Bob' in marxes
'Chico' in marxes
word= 'Harpo'

word in marxes

#  Count Occurrences of a Value by Using count()

marxes = ['Groucho', 'Chico', 'Harpo']

marxes.count('Harpo')

# convert to a string with join()

marxes= ['Groucho', 'Chico','Harpo']

','.join(marxes)

# Reorder Items with sort()

marxes = ['Groucho', 'Chico', 'Harpo']

so=sorted(marxes)
marxes.sort()
marxes.sort(reverse=True)

# get length with len()

len(marxes)

# Assign with =, Copy with copy()

a= [1,2,3]

a

a[2]= 'majid'
a
# using "copy" and "list" lead to no concetion with a. if a change, other will NOT change
b=a.copy()
c=list(a)
c
b

###################
# Tuples
###################
# Similar to lists, tuples are sequences of arbitrary items. Unlike lists, tuples are immutable,
# meaning you can’t add, delete, or change items after the tuple is defined. So, a tuple
# is similar to a constant list.

#  Create a Tuple by Using ()

empty_tuple =()

one_ma= 'Hr',

marx_tuple = 'Groucho', 'Chico', 'Harpo'

a, b, c = marx_tuple # tuple unpacking

# convert list to tuple: 

marx_list= ['majid','mahsa']

tuple(marx_list)

######################3
# Dictionaries
###########################

# Dictionaries are simillar to list but the order of items does not matter. Also, dictionaries use Index


empty_dict={}

bierce= {
        "day" : "A period",
        "positive": "Mistaken",
        "mis": "the"
        }

# Convert by Using dict()

lol = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]

dict(lol)

lot = [ ('a', 'b'), ('c', 'd'), ('e', 'f') ] # list
dict(lot)
tol = ( ['a', 'b'], ['c', 'd'], ['e', 'f'] ) # tuple
dict(tol)

#  Add or Change an Item by [ key ]
pythons = {
... 'Chapman': 'Graham',
... 'Cleese': 'John',
... 'Idle': 'Eric',
... 'Jones': 'Terry',
... 'Palin': 'Michael',
... }
pythons

pythons['Gilliam'] = 'Gerry' # add 

# in dict, key is unique 
some_pythons = {
... 'Graham': 'Chapman',
... 'John': 'Cleese',
... 'Eric': 'Idle',
... 'Terry': 'Gilliam',
... 'Michael': 'Palin',
... 'Terry': 'Jones',
... }

# Combine Dictionaries with update()
pythons = {
... 'Chapman': 'Graham',
... 'Cleese': 'John',
... 'Gilliam': 'Terry',
... 'Idle': 'Eric',
... 'Jones': 'Terry',
... 'Palin': 'Michael',
}

others = { 'Marx': 'Groucho', 'Howard': 'Moe' }

# now combine two: 

pythons.update(others)
# if second dic has same key as first dic, then second key will keep and key in first will be drop

# Delete an Item by Key with del

del pythons['Marx']

pythons.clear() # will clear all elements in dirc

pythons = {'Chapman': 'Graham', 'Cleese': 'John',
'Jones': 'Terry', 'Palin': 'Michael'}

'Chapman' in pythons # use "in" to see if a key is  in dict

pythons['Cleese']
pythons['majid'] # error in Python are exception 

pythons.get('majid','not availabe') # use get function for dict.


pythons.get('Cleese','not availabe')

## Get All Keys by Using keys()
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}

signals.keys() # to get all keys
# Get All Values by Using values()
list(signals.values())

#  Get All Key-Value Pairs by Using items()

list(signals.items()) # each key and values is returned as a tuple. 

#  Assign with =, Copy with copy()
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
save_signals = signals
signals['blue'] = 'confuse everyone' # same as list, make a change to a dict, will be reflected in all. 

# to aviod this, use "copy()" function

signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
signals
original_signals

######################
# Sets
######################

#A set is like a dictionary with its values thrown away, leaving only the keys. As with a
#dictionary, each key must be unique. You use a set when you only want to know that
#something exists, and nothing else about it. Use a dictionary if you want to attach some
# information to the key as a value.

#  Create with set()

empty_set=set()
empty_set

# Convert from Other Data Types with set()

set('letters')

# a set from a list: 

set( ['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'] )

#This time, a set from a tuple:
set( ('Ummagumma', 'Echoes', 'Atom Heart Mother') )

# When you give set() a dictionary, it uses only the keys:
set( {'apple': 'red', 'orange': 'orange', 'cherry': 'red'} )


###### Test for Value by Using in

drinks = {
... 'martini': {'vodka', 'vermouth'},
... 'black russian': {'vodka', 'kahlua'},
... 'white russian': {'cream', 'kahlua', 'vodka'},
... 'manhattan': {'rye', 'vermouth', 'bitters'},
... 'screwdriver': {'orange juice', 'vodka'}
... }
#Which drinks contain vodka?
for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)
        
#We want something with vodka but are lactose intolerant, and think vermouth tastes like kerosene:        
# page : 62
for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)
 
bruss = drinks['black russian']       

wruss = drinks['white russian']

# 
a = {1,2}
b = {2,3}

a & b # intersection (members common to both sets) 
a.intersection(b) # intersection (members common to both sets) 

bruss & wruss

a|b # the union (members of either set)
a.union(b) # the union (members of either set)

a-b # difference (members of the first set but not the second)

a.difference(b)

a ^ b # exclusive or (items in one set or the other, but not both)
a.symmetric_difference(b) # exclusive or (items in one set or the other, but not both)

a<=b # subset of another (all members of the first set are also in the second set) by using <= or issubset():
a.issubset(b)

a<b # To be a proper subset: the second set needs to have all the members of the first and more

a >= b #A superset is the opposite of a subset (all members of the second set are also members of the first).
a.issuperset(b)

a > b # proper superset (the first set has all members of the second, and more)

########### Compare Data Structures

## you make a list by using square brackets ([]), a tuple by using commas, and
# a dictionary by using curly brackets ({}).

marx_list = ['Groucho', 'Chico', 'Harpo']
marx_tuple = 'Groucho', 'Chico', 'Harpo'
marx_dict = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}

## For the list and tuple, the value between the square brackets is an integer offset. For the
# dictionary, it’s a key. For all three, the result is a value.

marx_list[2]
marx_tuple[2]
marx_dict['Harpo']


########################
# Exercise: Things to Do
########################
#3.1 

years_list = [1982,1983,1984,1985,1986]
years_list[0]
years_list[4]

things_list=['mozzarella','cinderella','salmonella']

things_list[1]=things_list[1].capitalize()
print(things_list)
things_list[0]=things_list[0].upper()


del things_list[-1]
things_list.remove('salmonella')

surprise=['Groucho','Chico','Harpo']
surprise[2]=surprise[2].lower()
surprise[2]=surprise[2].upper()
surprise[2]=surprise[2].capitalize()

e2f={'English':'French'}
type(e2f)
e2f={'dog':'chien','cat':'chat','walrus':'morse'}

e2f['walrus']
f2e= dict([(value,key) for key, value in e2f.items()])

set(e2f) # will give Key

life={'animals':{'cats':{'Henri','Grumpy','Lucy'},'octopi': '', 'emus':''},
      'plants':'',
      'other':''}
life['animals']
life['animals']['cats']
