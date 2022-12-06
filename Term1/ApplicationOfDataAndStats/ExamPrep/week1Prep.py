# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 16:20:56 2022

@author: AndreMota
"""

#%%

##note to self this bloody languaggue only returns the last returned function
## whyyyyyyyyyyyyyyyy
##Also remember I changed F9 to run current cell and the ctr+return to run the selected
##line because what type of self respecting human being will reach all the way to F9 for that

################################ data types ################################################


## data type retardaded edition, number 9 will make you understand the name

##declaring the classic int
myInt = 23

##declaring the classic float
myFloat = 23.0

myBaitFloat = 23

##type function returns the type of the variable don't forget that you can change a variable
##type just by declaring another type to the same name #ficaADica

type(myFloat) ## is a float because it was declared with a number with decimal cases
type(myBaitFloat) ##not a float because it was not declared with numerical decimal cases
## and this is loosly typed languague just to fuck with you. PHP and .js flashbacks

myString = "Bull"
myString2 = "Crap"

myMood = myString + myString2

print(myMood) 

type(myMood)

myInting, myFloating = 23, 23.5

print(myInting, myFloating)

##this is bool
type(True)

##this type has literally nothing associated with it
##this is literally NULL but they had to get a unique and way less cool name
##virgin None vs chad NULL
type(None)

##list type
type([1,2])

#%%
 ################################ list dictionaries #######################################


myList = []

myList

myList.append(27)

myList

myList = [1,2,2,27]

myList

myList[0]

myList[3]

##hey kid are you intered in key-pair values and hasmaps with extra? steps
## declaring a list in a dictionary is kinda cool and based though
myDictionary = {'first':'João',
                'last':'Mota', 'age':'23',
                'hotel?':'trivago', 
                'smoking':['after sex', 'after acing a test', 'dia de São nunca à tarde']}

#whoami
myDictionary['first']
myDictionary['last']

## accessing the hotel
myDictionary['hotel?']

myDictionary['smoking']


#%%

############################################ math operation ################################

##arithmetic / algebra / quick mafs

1 * 2 **3

## * multiplicar
## ** exponencial aka 2 ** 3 = 2^3

##string concanetation

'hello' + ' ' + 'there'

## we can multiply the string 
9* 'na' + ' batman'

################################ list operations ###########################################

list = [1,2,3,3,3]

list.append(4)

##number of times a certain value appears on the list
list.count(1)

##check the index of first occurance of that value in the list
list.index(3)

##inserts a value at the specified position
#list.insert(index, object)
list.insert(0, -1)

##reverse the order of the entire list
list.reverse()

##sort a list (at least in numerical order, need to investigate when it non numerical)

list.sort()

################################# range and slicing lists ##################################

##remember to use english
##creates a list from 0 to 10 that doesn't become declared

##removing the object type list called list because it will then fuck up with the inbuilt
## list function. thank you so much steffan fffffffffffffs
del(list)

## the range function takes two values, i and j, it then creates a list starting from i that
## is incremented with i++ until reaching j
range(0,10)

#list?

list(range(5,26))

## we can also just use a portion of the list by selecting the starting and ending list
## of the slice we want to use

listBilha = list(range(100,201))

##listing ther first 50 numbers like this
listBilha[0:50]

##all the pair numbers by chosing by how much we increment (for pair is 2)
listBilha[0:101:2]

## the third number will be the incrementor that is by default 1

##all multiples of 5
listBilha[0:101:5]

## we also leave it empty to signify to start from the first or to not have a ending
## besides the automatic end of the list of course

#starting from the first index to 100
listBilha[:100]

#starts from the index 50 and ends when there are no more indexes on the list
listBilha[50:]

## list all indexes aka starts and on the first and ends on the last index
listBilha[::]

## we can still signal the steps when we have 
##increments of 2
listBilha[::2]
##increments of 5
listBilha[::5]

## increments of 5 starting from 25
listBilha[25::5]

listBilha[:25:5]


######################################### boolean gaming ##################################

x = 23

x == 23

x == 24

x > 27

x <= 24

## basic shit with the good old || and != as well

x in [23,43]

23 in [23,123,1234412]

1 in [12]

##toca a bilha e passa a outro

##we are no in the can't be bothered this is too basic mode
##if you are reading and you aren't me sounds like a u problem to me #estudasses


############################################## loops ########################################

for i in range(0,10):
    print(i)


numbers = []

for i in range(0,10):
    print(i)
    numbers.append(i)


while 0:
    print( 'we do a little trolling')

i = 0
while  i < 10:
    i = i +1
    print(i)
    

i = 0
while True:
    i = i +1
    print(i)
    if i > 9:
        break
        
        
########################################## functions ######################################

def myFunction():
    print('cringe from myCringeFunction')

myFunction()


def myFunction2ElectricBoogaloo(greeting, cringePhrase):
    print(greeting + ', ' +cringePhrase + '!')

myFunction2ElectricBoogaloo('hello there', 'general kenobi')


def add(x,y):
    return(x+y)


add(1,2)


######################################## numpy ###########################################

import numpy as np

##now we can use np to call functions in the numpy library
## 5 per 5 matrix with 1 on the diagonal
np.identity(5)

## however always having to use np is very annoying we what can do is imitate what a 
## proper programming language does and import those specific functions to the global
## loaded up enviroment

from numpy import identity

identity(3)

## dear god this exists, got to save on those clicks

## eveb better tho alias that as well

from numpy import identity as ident

ident(4)

from matplotlib import pyplot as plt

#plt.plot([1,2,3], [1,4,1], 'or')

## numpy arrays are basically just better lists and they make sure all objects inside it
## are of the saem type

arrayNp = np.array([1,2,3.45,-123])

arrayNp

## multiply all the numbers inside the array
2 * arrayNp

## all numbers get +1 added
arrayNp + 1

##elevetaing all numbers by 2

arrayNp ** 2

arr1 = np.array([1,2,3,4])

##adds up the numbers of both arrays
arr1 + arrayNp

## evelvates arr1 by the corresponding index of arrayNp

arr1 ** arrayNp

## it gives the sin (seno) of each of values in the array
np.sin(arr1)

collection = np.array([[1,2,3], [22,44,11]])

collection 

## we can see how much rows and collumns there are on our objects
collection.shape

collection.shape = 6

collection

## convert it to a 2 per 3 array
collection.shape = [3,2]

collection


## array of eros

np.zeros([2,3])


## Array of ones

np.ones([2,10])


## create an array of floating points
#np.arange(starting value,stopping value, increments )
np.arange(0.1, 0.2, 0.01)

## instead of taking the number of increment it takes the number of values
## to create that amount of numbers that are equally spaced
np.linspace(0.1,0.2, 20)



a = np.array([1,2,3])
b = np.array([3,4,5])

np.stack([a,b])

np.vstack([a,b])


## generating random numbers

np.random?
## here we can see all the distrivutions we can use to generate numbers

##generated 5 numbers with the 2 entry values of the normal distribution
randomAr = np.random.normal(1,2,5)

np.average(randomAr)

np.var(randomAr)


randomArrays = np.random.normal(0,5,[5,4])

np.average(randomArrays)

## we can select by axis as well, x for 0 and y for 1
np.average(randomArrays, axis = 0)

matrix1 = np.matrix([[1,2],
          [5,6]])


## couldn't be bothered to look this one up
np.linalg.eig(matrix1)


############################################ week 2 ########################################
############################################ week 2 ########################################
############################################ week 2 ########################################


# Beginner

# Create a list with the integers from 1 to 5.

listaExemplo = [1,2,3]

# Create a list with the integers from 1 to 1000.

listaExemplo1 = list(range(1,1001))
                     
listaExemplo1[::]

# Create a list with the even integers from 1 to 1000.

listaExemplo2 = listaExemplo1[::2]

listaExemplo2

# How do you calculate 42 ^23 # in python?

42 ** 23

# How do you determine the length of a list?

len(listaExemplo1)

# How do you reverse a list?

list.reverse(listaExemplo1)

listaExemplo1

# Use string addition and multiplication to create the string 'nanananananananana, batman!'

9*'na' + ' batman!'

# How do you concatenate two lists?

listaExemplo + listaExemplo1[0:20]

# How do you check if a value exists in a list?

##number of times a certain value appears on the list

##see the number of times
listaExemplo.count(5)
##check the index of first occurance of that value in the list, and first if it exists
listaExemplo.index(5)

# How do you extract the keys from a dictionary?

myDictionaryLec = {'Data':'Mark',
                'Stats':'Dorka',
                'This':'ben',
                'hotel?':'trivago', 
                'smoking':['after sex', 'after acing a test', 'dia de São nunca à tarde']}

myDictionaryLec['hotel?']
myDictionaryLec['This']
myDictionaryLec['Stats']


# How do you write comments in python code?
##like this lmao

# Intermediate

# Fizzbuzz: Write out the numbers from 1 to 100, and replace every number that is
# divisible by 3 by "Fizz", every number divisible by 5 by "Buzz" and every number
# that is divisible by both 3 and 5 by "FizzBuzz". (Hint: Use the modulo operator % .)

i = 0
for i in range(100):
    print(i)
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
        continue
    if i % 3 == 0:
        print("Fizz")
    if i % 5 == 0:
        print("Buzz")


# Draw the curve of the function log(x + 10).
import matplotlib.pyplot as plt

x = np.linspace(0.1, 20, 100)

y = np.log(x+10)

##remember to switch to the plots view near the variable explorer
plt.plot(x,y)
plt.show()

# Write a function that checks whether a given string is a palindrome.

def funcIsPalindrome(argsPalindrome):
    aux = len(argsPalindrome)
    if aux % 2 == 0:
        return
    if aux % 2 != 0:
        return
        
 def is_palindrome(inp):
    inp = list(inp)
    rev = list(inp)[::-1]
    return inp == rev    

is_palindrome("racecar")

# How do you create a 3 by 4 matrix filled with random numbers generated from a normal distribution?

## to make it a 3 per 4 what matters is what you put in the last argument
matrix = np.random.normal(2,7,[3,4])

matrix

# What is mylist[-1] if mylist is a list containing the numbers 1, 4, 10, and 23?

mylist = [1,4,10,23]

## the last index, when you use negative it goes backward so -1 is the last index, 
## -2 is the second to last index, kinda as if it the index worked as linkedList in java
mylist[-1]

# What are the main differences between a list and a numpy array?





































