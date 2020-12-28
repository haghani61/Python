#Do, or do not. There is no try. --Yoda
###############
# CHAPTER 4: Py Crust: Code Structures
############## 

 # Comment with #
 
# Continue Lines with \
 
alphabet = 'ahdhahfa' +\
 'ahsdhahfa' +\
 'ahdhafhalf'
  
##### Compare with if, elif, and else
 
disaster = True

if disaster: # if forget to type ":", python will give an error
    print("woe!")
else:
    print("whee!")

furry= True
samll= True

if furry:
    if samll:
        print("It is a cat.")
    else:
        print("It is a bear!")
else:
    if small:
        print("It is a skink!")
    else:
        print("it is human")

# elif (meaning else if), and else
color = "puce"

if color == "red":
    print("tomato")
elif color == "green":
    print("its a tomato")
elif color == "bee purple":
    print("I donot know")
else:
    print("I near heard", color)
    
# Python’s comparison operators are:
    # equality ==
    # inequality !=
    # less than <
    # less than or equal <=
    # greater than >
    # greater than or equal >=
    # membership in …
    
    ## Note that two equals signs (==) are used to test equality; remember, a single equals sign
    #   (=) is what you use to assign a value to a variable.


# What Is True?

some_list=[]

if some_list:
    print("there is something in here")
else:
    print("Hey, it is empty!")

# # Repeat with while
count=1

while count <=5:
 print(count)
 count +=1    

# Cancel with break

while True:
    stuff= input("String to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())
        
# Skip Ahead with continue

while True:
    value = input("Integer, please [q to quit]:")
    if value == 'q':
        break
    number = int(value)
    if number % 2 == 0:
        continue
    print(number, "squared is", number*number)

# Check break Use with else

numbers = [1,3,5]
position = 0 
# If the while loop ended normally (no break call), control passes to an optional else.
while position < len(numbers):
    number = numbers[position]
    if number % 2 ==0:
        print('Found even number', number)
        break
    position +=1
else:
    print('No even number found')


# Iterate with for
rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']

current = 0

while current < len(rabbits):
    print(rabbits[current])
    current +=1
# or
for x in rabbits:
     print(x)

word = 'cat'
for x in word:
    print(x)
# example for dict

accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
'person': 'Col. Mustard'}

for card in accusation: # or, for card in accusation.keys():
    print(card)

# To iterate over the values rather than the keys, you use the dictionary’s values() function:
    
for value in accusation.values():
    print(value)

# to return both key and value: 

for x in accusation.items():
    print(x)
    
# For each tuple returned by
# items(), assign the first value (the key) to card and the second (the value) to contents:

for x, y in accusation.items():
    print(x,y)

# Cancel with break: A break in a for loop breaks out of the loop, as it does for a while loop.
    
# skip with "continue": Inserting a continue in a for loop jumps to the next iteration of the loop, as it does for
#a while loop 

# Check break Use with else
    
cheeses =[]

for cheese in cheeses:
    print('This shop has', cheese)
    break
else: # no break means no cheese
    print('This is not much of a cheese shop, is it')

cheeses = []
found_one = False


for cheese in cheeses:
    found_one = True
    print('This shop has some lovely', cheese)
    break

if not found_one:
    print('This is not much of a cheese shop, is it?')
    
# Iterate Multiple Sequences with "zip()" function: 
    
days = ['Monday', 'Tuesday', 'Wednesday']

fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
    
    
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts): # 
 print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert) # zip() stops when the shortest sequence is done
 
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'

list(zip(english,french))
dict(zip(english,french))
    
# Generate Number Sequences with range()

# The range() function returns a stream of numbers within a specified range

# range(start, stop, step)

for x in range(0,3):
    print(x)

list(range(0,3))

for x in range(2,-1,-1):
    print(x)
    
##############
#Comprehensions
##############

# List Comprehensions

number_list=[]

for number in range(1,6):
    number_list.append(number)

number_list = [number for number in range(1,6)]
number_list = list(range(1,6))    
number_list = [number-1 for number in range(1,6)]  

a_list = [number for number in range(1,6) if number % 2 ==1] # only odd numeber, 1, 3, 5

a_list = []

for number  in range(1,6):
    if number % 2 == 1:
        a_list.append(number)
        

rows = range(1,4)
cols = range(1,3)

for row in rows:
    for col in cols:
        print(row,col)
        
# making it a list of (row, col) tuples

rows= range(1,4)
cols = range(1,3)
cells = [(row,col) for row in rows for col in cols]
for cell in cells:
    print(cell)
# 
for row, col in cells:
    print(row,col)

######
#  Dictionary Comprehensions : { key_expression : value_expression for expression in iterable }
######

word= 'letters'
letter_cpunts = {letter: word.count(letter) for letter in word}

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
letter_counts

# Set Comprehensions: { expression for expression in iterable }

a_set = {number for number in range(1,6) if number % 3 == 1}


# Generator Comprehensions

number_thing = (number for number in range(1,6))

type(number_thing) # A generator is one way to provide data to an iterator.

for number in number_thing:
     print(number)

number_list = list(number_thing)
number_list

#####################
# Functions
#####################
# two things with a function
# Define it
# Call it

#To define a Python function, you type def, the function name, parentheses enclosing
#any input parameters to the function, and then finally, a colon (:).

# def  function name():
  # indent code
  
def do_nothing():
    pass

do_nothing()

def make_a_sound():
    print('quak')

make_a_sound()

def agree():
    return True

agree()

if agree():
    print('Splendid!')
else:
    print('that was unexpected.')

def echo(anything):
    return anything + ' ' + anything

echo('majid')
#

def commentary(color):
    if color == 'red':
        return "it is a tomato"
    elif color == ';green':
        return "ir is a green pepper"
    elif color == 'bee purple':
        return "I donot know what it is"
    else:
        return "I have never heard of the color" + color + "."
    

comment = commentary('blue')  

print(comment) 
# 
print(do_nothing())


##### None Is Useful: 
# Remember that zero-valued integers or floats, empty strings (''), lists ([]), tuples ((,)), dictionaries ({}), 
# and sets(set()) are all False, but are not equal to None.

def is_none(thing):
    if thing is None:
        print("it is none")
    elif thing:
        print("it is True")
    else:
        print("It is False")
        

is_none(True)
is_none(False)
is_none(())
is_none(None)

###########
# Positional Arguments

def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

menu('chardonnay','chicken', 'cake')

# Keyword Arguments
menu(entree='beef', dessert='bagel', wine='bordeaux')

# Specify Default Parameter Values

def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

menu('chardonnay', 'chicken')

# there’s a bug: it’s empty only the first time it’s called. The second time, result still has
# one item from the previous call:
def buggy(arg, result = []):
    result.append(arg)
    print(result)

buggy('a')
buggy('b') 

# re write againg: 

def buggy(arg):
    result =[]
    result.append(arg)
    return result
buggy('a')
buggy('b') 

# to fix this: 

def nonbuggy(arg, result = None):
    if result is None:
        result =[]
        result.append(arg)
        print(result)
buggy('a')
buggy('b') 

##############
## Gather Positional Arguments with *

# Python doesn’t have pointers

def print_args(*args):
    print('Positional argument tuple:', args)

print_args()

print_args(3, 2, 1, 'wait!', 'uh...')

# If your function has required positional arguments as well, *args goes at
# the end and grabs all the rest:

def print_more(required1, required2, *args): # *args: will merge arguments
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')

################
# Gather Keyword Arguments with **

# You can use two asterisks (**) to group keyword arguments into a dictionary, where the
# argument names are the keys, and their values are the corresponding dictionary values

def print_kwargs(**kwargs):
    print('keyword arguments:', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')


# Docstrings

def echo(anything):
    'echo returns its input argumnet'
    return anything

echo('maji')

def print_if_true(thing, check):
    '''
    Prints the first argumnet if a second argument is true.
    the operation is:
        1. Check whether the *second* argument is true.
        2. If it is, print the *first* argument.
    '''
    if check:
        print(thing)

help(echo)

print(echo.__doc__)

###
# Functions Are First-Class Citizens
###
def answer():
    print(42)
def run_something(func):
    func()
    
run_something(answer)

def add_args(arg1, arg2):
    print(arg1+arg2)

type(add_args)
# this function will get arg1 and arg2 argument and call func as function.
def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_something_with_args(add_args, 5, 9)
#

def sum_args(*args):
    return sum(args)

# a function and any number of positional arguments to pass to it:
  
def run_with_positional_arg(func, *args):
    return func(*args)

run_with_positional_arg(sum_args, 1,2,3,4)

#######
# Inner Functions: a function that is dynamically generated by another function

def outer(a,b): # tow functions 
    def inner(c,d):
        return c + d
    return inner(a,b)

outer(3,7)

def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)

knights('Ni!')

# Closures: a dynamically created function that remembers where it came from.
def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2

a = knights2('Duck')
b = knights2('Hasenpfeffer')

a()
b()

############################################
# Anonymous Functions: the lambda() Function
############################################

#  A lambda function is an anonymous function expressed as a single statement.

def edit_story(words, func): # words: a list of words
    for word in words:       # func: a function to apply to each word in words
        print(func(word))


stairs= ['thud', 'meow', 'thud', 'hiss']
def enliven(word): # give that prose more punch
    return word.capitalize() + '!'

edit_story(stairs, enliven) # two function

edit_story(stairs, lambda word: word.capitalize() + '!')
edit_story(stairs, lambda x: x.capitalize() + '!')


######

# Generators: A generator is a Python sequence creation object.
######

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number  # instead of return, use yield
        number += step
ranger= my_range(1,5)

for x in ranger:
    print(x)

# Decorators: A decorator is a function that takes one function as input and returns another function.

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

def add_ints(a,b):
    return a + b
add_ints(3,5)

cooler_add_ints = document_it(add_ints) # manual decorator assignment

cooler_add_ints(3, 5)

# alternative : 

@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

@document_it
@square_it
def add_ints(a,b):
    return a + b

add_ints(3, 5)

# reversing the decorator order
@square_it
@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)

## Namespaces and Scope

animal = 'fruitbat'

def print_global():
    print('inside print_global:', animal)

print('at the top level:', animal)

print_global()

# will get an error
def change_and_print_global():
    print('inside change_and_print_global:', animal)
    animal = 'wombat'
    print('after the change:', animal)   
change_and_print_global()
# 
def change_local():
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))
    
############
animal = 'fruitbat'
def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)

# locals() returns a dictionary of the contents of the local namespace.
    
# globals() returns a dictionary of the contents of the global namespace.
animal = 'fruitbat'

def change_local():
    animal = 'wombat' # local variable
    print('locals:',locals())

change_local()


print('globals:', globals()) # reformatted a little for presentation

# Uses of _ and __ in Names
# Names that begin and end with two underscores (__) are reserved for use within Python,

###
# Handle Errors with try and except
###


## Python uses exceptions: code that is executed when an associated error occurs

short_list = [1, 2, 3]
position = 5
short_list[position]

short_list = [1, 2, 3]
position = 5
#use "try" to wrap your code, and "except" to provide the error handling
try:
    short_list[position]
except:
        print('Need a position between 0 and', len(short_list)-1, 'but got', position)



##########################
# Things to Do
##########################
#1: Assign the value 7 to the variable guess_me. Then, write the conditional tests (if,
# else, and elif) to print the string 'too low' if guess_me is less than 7, 'too high' if
# greater than 7, and 'just right' if equal to 7.

guess_me = 7

if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just right')

guess_me = 7
start = 1
#2: Assign the value 7 to the variable guess_me and the value 1 to the variable start.
#Write a while loop that compares start with guess_me. Print 'too low' if start is less than guess me. 
#If start equals guess_me, print 'found it!' and exit the loop. If start
# is greater than guess_me, print 'oops' and exit the loop. Increment start at the end of  the loop.
while True:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it')
        break
    elif start > guess_me:
        print('oops')
        break
    start += 1
# 3: Use a for loop to print the values of the list [3, 2, 1, 0].
for value in [3,2,1,0]:
    print(value)

# 4: Use a list comprehension to make a list called even of the even numbers in range(10).
even= [number for number in range(10) if number %2 ==0]

even_list=[]
for number in range(10):
    if number % 2 ==0:
        even_list.append(number)
# 5: Use a dictionary comprehension to create the dictionary squares. Use range(10) to
# return the keys, and use the square of each key as its value.
square = {key: key*key for key in range(10)}

# 6: Use a set comprehension to create the set odd from the odd numbers in range(10).
odd_set= {number for number in range(10) if number % 2 ==1}

# 7: Use a generator comprehension to return the string 'Got ' and a number for the
# numbers in range(10). Iterate through this by using a for loop.
for thing in ('Got %s' % number for number in range(10)):
    print(thing)

# 8:  Define a function called good() that returns the list ['Harry', 'Ron', 'Hermione'].
def good():
    return['Harry','Ron','Hermione']
    
# 9: Define a generator function called get_odds() that returns the odd numbers from
 # range(10). Use a for loop to find and print the third value returned.
def get_odds():
    for number in range(10):
        if number % 2 == 1:
            print(number)

def get_oddss():
    for number in range(1,10,2):
        yield number

for count, number in enumerate(get_oddss(),1):
    if count ==3:
        print("The third odd numver is", number)
        break

# 10: Define a decorator called test that prints 'start' when a function is called and 'end' when it finishes.

def test(func):
    def new_func(*arg, **kwargs):
        print('start')
        result = func(*arg, **kwargs)
        print('end')
        return result
    return new_func

@test
def greeting():
    print("Greetings, Earthiling")
    
greeting()

# 11: Define an exception called OopsException. Raise this exception to see what happens.
# Then, write the code to catch this exception and print 'Caught an oops'.

class OopsException(Exception):
    pass

raise OopsException()

try:
    raise OopsException
except OopsException:
    print('Cought an oops')
    
# 12 Use zip() to make a dictionary called movies that pairs these lists: titles =
#['Creature of Habit', 'Crewel Fate'] and plots = ['A nun turns into a mon
# ster', 'A haunted yarn shop'].

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']

movie = dict(zip(titles, plots)) 
    



    

        
        
    

















      










