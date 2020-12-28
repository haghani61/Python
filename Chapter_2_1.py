#Do, or do not. There is no try. --Yoda
###############
# CHAPTER 2: Py Ingredients: Numbers, Strings, and Variables
##############

# booleans: whihc have the value True and False: 

# integeres: whole number such as 42 adn 10000000

# floats : numbers with decimal points such as 3.12 or sometimes exponents line 10.0e8

# strings: sequences of text characters

# these are, In a way, they’re like atoms.!

# variables: names that refe to valies in the computer's memory that can define for use

x= 7
print(x)
# variables are just names
# variables are just names' 

b=x 
b
# 
## use "type()" function to understand the type of anything = same as  "class()" function in R

type(b)

#Finally, don’t use any of these for variable names, because they are Python’s reserved
#words:
#False class finally is return
#None continue for lambda try
#True def from nonlocal while
#and del global not with
#as elif if or yield
#assert else import pass
#break except in raise

##################3
# "%"  modulus (remainder), 7%3 whihc will give 1

5
# / carries out floating-point (decimal) division
# // performs integer (truncating) division

9/5
9//5

5/0

a=95
a= a -3

a
# or: You can combine the arithmetic operators with assignment by putting the operator before the =.
a -=3
a *= 2
a +=8
a /=  3

a= 13
a //=4
a

# to get reminder of divided use  "%"

9 % 5

# use // as module to get quatient : 

9 // 5

# to have both reminder and get truncated : 

divmod(9,5)

# To change other Python data types to an integer, use the int() function: 

int(True)
int(8.3)
int('8.4')
int('99')

## The boolean value False is treated as 0 or 0.0 when mixed with integers or floats, and 
# True is treated as 1 or 1.0:

True+1
False+1

########
# Floats:
########

# to convert other types into to float use "float()" function:

float(True)
float(8)
float('33')
float('1.0e4')
float('-22')

###########
## Strings:
###########

# Unlike other languages, strings in Python are immutable

# You make a Python string by enclosing characters in either single quotes or double
# quotes, as demonstrated in the following: 

'haha'
"haha"
'"hah"'
# if we have mutli lines then use '''hashsh  ahschalhsf '''

poem2 = '''I do not like thee, Doctor Fell.
... The reason why, I cannot tell.
... But this I know, and know full well:
... I do not like thee, Doctor Fell.
... '''
poem2
print(poem2) # useing print() function cause that to excape with \m
# 
bottles = 99
base = ''
base += 'current inventory: '
base += str(bottles)
base
# use "str() to convert Python data types to strings

str(8)

####
# Escape with \
# 

# using "\n" means to begin a new line: 

palindrome= 'A man,\nA plan,\nA Canal: \nPanama:'
print(palindrome)

# use "\t" to scape seguence :

print('\tabd')
print('a\tbc')
print('abc\t')

# to have  " and ' inside a string, should use \' and \" and  \\ for \. 

testimony= "\"I did nothing!\" he \""
print(testimony)
fact= "The word  54' "
print(fact)
test2= 'Todya is first day \\'
print(test2)

# Combine with + : to combine two strings: 

' majid ' + ' mahsa'
# Duplicate with *

start= 'na ' *4 + '\n'
end='goodby.'
print(start+end)
# Extract a Character with []

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters)

letters[0]
letters[-1]
#
name= 'majid'
name[0]='M' # will give erro to address this error, use these: 

name.replace('m','M') # or :
'M' + name[1:]

# Slice with [ start : end : step ]

letters = 'abcdefghijklmnopqrstuvwxyz'

letters[:]
letters[:5]
letters[2:4]
letters[-3:]
letters[-6:-2]

letters[::2]
letters[4:20:3]

letters[:21:5] # From the start to offset 20 by 5: the end needs to be one more than the actual offset

letters[-1::-1] # backward

letters[::-1]

letters[-51:-50]

letters[:2]

letters[:70]

# Get Length with "len()"  to get number of characters, use for strings

len(letters)

# Split with split()

todos = 'get gloves,get mask,give cat vitamins,call ambulance'

todos.split(',')
todos.split(' ')
todos.split()

#  Combine with join() for stirng

crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']

crypto_string = ', '.join(crypto_list)

tst= 'test'

tst2=','.join(tst)

# Playing with Strings
poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

poem[:6]

len(poem)

poem.startswith('All')
poem.startswith('majid')
poem.endswith('test')

poem.find('the')
poem.rfind('the') # find the last "the" in sentence

poem.count("the")

poem.isalnum() # are all of the characters in the sentence either letters and numbers

######## Case and Alignment

steup ='a duck goes into a bar ...'

steup.strip('.') # will remove ...

steup.capitalize()

steup.title() # capitalize all the elphabet of each word

steup.upper() # capitalize all words

steup.lower()

steup.swapcase() # Swap upper- and lowercase

len(steup)

steup.center(30) # put sentence in center of 30 . Aligned

steup.ljust(30)

steup.ljust(len(steup))

steup

steup.rjust(40)

# Substitute with "replace()" to replace in stings


steup.replace('duck','marmoset')

steup.replace('a ','a famous ', 100) # change up to 100 of them. 

##############
# Things to Do
##############
#1-how many second in 1 hour

60 * 60
# 2- Assign the result from the previous task (seconds in an hour) to a variable called seconds_per_hour.
seonds_per_hour=3600

# 3 :How many seconds are in a day? Use your seconds_per_hour variable.
seconds_per_day=24* seonds_per_hour

# 5: Divide seconds_per_day by seconds_per_hour. Use floating-point (/) division. 
seconds_per_day/seonds_per_hour

# 6: Divide seconds_per_day by seconds_per_hour, using integer (//) division. 
seconds_per_day//seonds_per_hour
 
 






