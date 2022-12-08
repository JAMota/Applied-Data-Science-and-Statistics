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

#%%
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

#%%
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
        
#%%     
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

#%%
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

#np.random?
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

#%%
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
listaExemplo.count(3)
##check the index of first occurance of that value in the list, and first if it exists
listaExemplo.index(3)

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


#%%
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
        return argsPalindrome
    if aux % 2 != 0:
        return argsPalindrome

        
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

##lists can have any type of object while numpy arrays will make sure all the values have
## the same type in the array, also multiplication and addition operations work differently
## between lists and numpy arrays


# Advanced

# 99 Bottles: Write a python program that generates the song lyrics to “99 bottles”, i.e.

#     99 bottles of beer on the wall, 99 bottles of beer. If one of those bottles should happen to fall, 98 bottles of beer on the wall.

#     98 bottles of beer on the wall, 98 bottles of beer. If ...

#     ...

#     2 bottles of beer on the wall, 2 bottles of beer. If one of those bottles should happen to fall, 1 bottle of beer on the wall.

#     1 bottle of beer on the wall, 1 bottle of beer. If one of those bottles should happen to fall, no bottles of beer on the wall.

i = 99
while i != -1:
    print(i, " bottles of beer on the wall, ", i,
          "  bottles of beer. If one of those bottles should happen to fall, ",
          i-1 , " bottles of beer on the wall.")
    i = i-1


# Write a function to calculate the median of a list of numbers?

def medianFunc(list):
    return np.median(list)


medianFunc(listBilha)

#%%
###################################### week 1 traffic problems ############################

# Set up

# Download and unzip the csv file “Road Safety Data - Accidents 2019” from the module ELE page.

# Read the csv file into a pandas DataFrame named accidents using the function pd.read_csv (consult the help page for that function to see what options there are.)
# Warm-up problems

import pandas as pd

a = "C:/AppliedDataScienceAndStatistics/Applied-Data-Science-and-Statistics/Term1/ApplicationOfDataAndStats/week7/accidents2019.csv"

dataFrame = pd.read_csv(a)

# How many rows and columns does accidents have?

#[117536 rows x 32 columns]
dataFrame.count

# Create a new data frame locations that only consists of the Latitude and Longitude column of accidents.

dataFrameLatLong = dataFrame[['Latitude','Longitude']].copy

# Transform the Date column to the data type datetime. Be careful to check that the dates
# have been parsed correctly (which depends on the format of the date in the raw dataset).

##check type of each variable/collum in the data frame
dataFrame.dtypes

#dataFrame['Date'] = dataFrame['Date'].astype(datetime)
dataFrame['Date'] = pd.to_datetime(dataFrame['Date'], format="%d/%m/%Y")


# Permanently remove the columns Accident_Index, Location_Easting_OSGR,
# Location_Northing_OSGR from accidents.

del dataFrame['Accident_Index']
del dataFrame['Location_Easting_OSGR']
del dataFrame['Location_Northing_OSGR']

# Reorder the rows of the data frame by increasing Date and Time.

dataFrame.sort_values(['Date','Time'])

# Add an index column with increasing integer values 1,2,3,...

dataFrame['index'] = range(1, len(dataFrame)+1)


# Advanced problems

# Add a column hour with values 0,1,2,. . . ,23 corresponding to the time of day.


dataFrame['hour'] = 0
i = 0
for i in range(len(dataFrame)):
    aux = dataFrame['Time'][i]
    aux = str(aux).split(":")[0] ##we have to stringify here or else we get problems parsing
    dataFrame['hour'][i] = aux
    i = i +1
    

# Add a column weekend which is True for accidents that happened on the weekend,
# and False otherwise.

## since monday is day 2 the weekend is day 1 and 7
dataFrame['isWeekend'] = False
i = 0
for i in range(len(dataFrame)):
    if dataFrame['Day_of_Week'][i] == 1 or dataFrame['Day_of_Week'][i] == 7:
        dataFrame['isWeekend'][i] = True
    i = i +1
    
##check of much of each value
dataFrame.value_counts(['isWeekend'])


# Create a new data frame with columns Date (in format ‘YYYY-MM-DD’),
# Accidents (total number of accidents per day) and Casualties (total number of casualties
# per day).

dataFrameAccidents = dataFrame

dataFrameAccidents = dataFrameAccidents[['Date','Number_of_Casualties']]   

## we got to parse all the dates here to get what we want
i = 0
for i in range(len(dataFrameAccidents)):
    
    auxString = dataFrame['Date'][i]
    auxYear = str(auxString).split("-")[0]
    auxMonth = str(auxString).split("-")[1]
    auxDay = str(auxString).split("-")[2]
    auxDay = str(auxDay).split(" ")[0]
    
    dataFrameAccidents['Date'][i] =  auxYear + '-' + auxMonth + '-' + auxDay
        
    i = i +1

## just like in SQL    


numberOfAcidents = dataFrameAccidents.groupby(['Date'])['Number_of_Casualties'].count()
 
numberOfCasualties = dataFrameAccidents.groupby(['Date'])['Number_of_Casualties'].sum()

##merging / joining two different data frames
dataFrameDaily = pd.merge(left=numberOfAcidents, right=numberOfCasualties, on='Date') 
##or
dataFrameDaily = pd.concat([numberOfAcidents, numberOfCasualties], axis=1, join='inner')


# Verify that Casualties is always greater than or equal to Accidents.

i= 0
for i in range(len(dataFrameAccidents.groupby(['Date'])['Number_of_Casualties'].count())):
    numberOfAcidents = dataFrameAccidents.groupby(['Date'])['Number_of_Casualties'].count()[i]
     
    numberOfCasualties = \
        dataFrameAccidents.groupby(['Date'])['Number_of_Casualties'].sum()[i]
    
    if numberOfAcidents >= numberOfCasualties:
        print(" you have fucked up")
    
    i = i +1

# Create a time series plot showing the number of accidents per day.


dataFrameDaily.plot() ## this is auto plot from pandas
plt.plot('Number_of_Casualties_y', data=dataFrameDaily)
plt.show()

# Summarise and plot the number of accidents for each weekday.

dataFrameAccidentsWeekday = dataFrame[['Date','Number_of_Casualties','Day_of_Week']]

#gringo1 = dataFrameAccidentsWeekday.groupby(['Date'])['Day_of_Week'].count()  

weekdayAccidents = dataFrameAccidentsWeekday.groupby(['Day_of_Week']).count()  

weekdayAccidents.plot()

plt.figure(figsize=[8,4])
plt.bar(weekdayAccidents.index, weekdayAccidents.Number_of_Casualties)



# What was the day of the week of the 10 days with the highest number of casualties?


dataFrameAccidentsSums = dataFrame[['Date','Number_of_Casualties']]
dataFrameAccidentsSums = dataFrameAccidentsSums.groupby(['Date']).sum()


dataFrameAccidentsDayOfWeek = dataFrame[['Date','Day_of_Week']]

##removes all duplicate rows
dataFrameAccidentsDayOfWeek = dataFrameAccidentsDayOfWeek.drop_duplicates()

dataFrameAccidentsSumsWeek = \
    pd.merge(left=dataFrameAccidentsSums, right=dataFrameAccidentsDayOfWeek,how='inner', on='Date')

## we have it ordered by ascending order 
dataFrameAccidentsSumsWeek.sort_values(['Number_of_Casualties'], ascending=[True])

##so now we will orderby descending

dataFrameAccidentsSumsWeek = dataFrameAccidentsSumsWeek.sort_values(['Number_of_Casualties'], ascending=[False])

dataFrameAccidentsSumsWeek.head(n=10)
print(dataFrameAccidentsSumsWeek.head(n=10))


#%%
################################################ week 2 ####################################
################################################ week 2 ####################################
################################################ week 2 ####################################
################################################ week 2 ####################################
################################################ week 2 ####################################






# Load the gapminder.csv data using pandas.

a = "C:\AppliedDataScienceAndStatistics\Applied-Data-Science-and-Statistics\Term1\ApplicationOfDataAndStats\week8\gapminder.csv"

dataFrameGapMinder = pd.read_csv(a)


# Examine the first 10 rows of your dataset.
## first 10 top rows
dataFrameGapMinder.head(n=10)

# Using Matplotlib, plot life expectancy over time for the United Kingdom.

##Select Rows of pandas DataFrame by Condition
## getting the rows with the value we want

dataFrameUnitedKingdom = \
    dataFrameGapMinder.loc[dataFrameGapMinder['country'] == "United Kingdom"]

plt.plot(dataFrameUnitedKingdom["year"], dataFrameUnitedKingdom["lifeExp"])
##or //same thing
## this has to be executed at the same time in the same block dingus #ficaADica
plt.plot(dataFrameUnitedKingdom.year, dataFrameUnitedKingdom.lifeExp, label='UK')
plt.xlabel("year")
plt.ylabel("life expectancy, years")
plt.legend() ## to show the labels
plt.show()

# Again, using Matplotlib, overlay on the same plot, life expectancy plots for the UK 
#and Burkina Faso. Add a legend which indicates which plot corresponds to which country.

dataFrameBurkinaFaso = \
    dataFrameGapMinder.loc[dataFrameGapMinder['country'] == "Burkina Faso"]
    
plt.plot(dataFrameBurkinaFaso.year, dataFrameBurkinaFaso.lifeExp, label='UK')
plt.plot(dataFrameUnitedKingdom.year, dataFrameUnitedKingdom.lifeExp, label='Burkina Faso')
plt.xlabel("year")
plt.ylabel("life expectancy, years")
plt.legend()  ## to show the labels
plt.show()

# Now, we are going to use plotnine's ggplot function to produce the same plot:
# life expectancy over time for both the UK and Burkina Faso. First create a data 
#frame that keeps only those rows for the UK and Burkina Faso.

dataFrameBurkinaFaso
dataFrameUnitedKingdom

## append still works but now to add one data frame to the other we should use concat
dataFrameUKBF = dataFrameUnitedKingdom.append(dataFrameBurkinaFaso)
## the new proper way to concatenate data frames
dataFrameUKBF = pd.concat([dataFrameBurkinaFaso, dataFrameUnitedKingdom])

from plotnine import *
import matplotlib.pyplot as plt

# Next run the following code to plot the life expectancies over time:

# (ggplot(df_uk_bf, aes(x='year', y='lifeExp', colour='country')) +
# geom_line())

##ggplot with line func
(ggplot(dataFrameUKBF) +
aes(x='year', y='lifeExp', colour='country') +
geom_line() )

# Now change geom_line to geom_point and examine how that changes the plot.

##ggplot with point graph
(ggplot(dataFrameUKBF) +
aes(x='year', y='lifeExp', colour='country') +
geom_point() )


# We can also layer geoms. Now add back in + geom_line() in addition to geom_point(). What does this plot look like?

## we have both the points of occurences and the lines formed from them
(ggplot(dataFrameUKBF) +
aes(x='year', y='lifeExp', colour='country') +
geom_point() +
geom_line())

# Suppose we want to add linear regression lines to data from each country. We can do 
#this by adding + geom_smooth(method="lm") to the end of our plot command.

##adding a straing geom_smooth regression line using the basic lm method
(ggplot(dataFrameUKBF) +
aes(x='year', y='lifeExp', colour='country') +
geom_point() +
geom_line()+
geom_smooth(method="lm"))

# We can remove the uncertainty intervals from the plots by changing + 
#geom_smooth(method="lm") to + geom_smooth(method="lm", se=False). Try this.

##removing the standard error to the regression lines
(ggplot(dataFrameUKBF) +
aes(x='year', y='lifeExp', colour='country') +
geom_point() +
geom_line()+
geom_smooth(method="lm", se=False))

# Suppose instead of plotting two regression lines, we want a single regression line 
#representing the trends across both countries. To do this, we can run the following code:

(ggplot(dataFrameUKBF, aes(x='year', y='lifeExp')) +
geom_point(aes(colour='country')) +
geom_smooth(method="lm", se=False))

# (ggplot(df_uk_bf, aes(x='year', y='lifeExp')) +
# geom_point(aes(colour='country')) +
# geom_smooth(method="lm", se=False))


# Why has the above plotted a single regression line?

##Because this way ggplot is not passing down the aestetics in a way that will be inherited

##It's because whilst we use a colour aesthetic, the colour aesthetic is used only 
##by geom_point and not inherited by geom_smooth. Whereas in the former case the colour 
##aesthetic is stated in the ggplot section which means it is inherited by downstream geoms,
## including geom_smooth meaning it creates two regression lines — one for each colour.


# Now use to ggplot to create a similar plot except plotting all countries in the Americas.

dataFrameAmericas= \
    dataFrameGapMinder.loc[dataFrameGapMinder['continent'] == "Americas"]
    
(ggplot(dataFrameAmericas) +
 aes(x='year', y='lifeExp', colour='country')+
 geom_point() +
 geom_line())

## this one has the regression line of all the Americas
(ggplot(dataFrameAmericas, aes(x='year', y='lifeExp')) +
geom_point(aes(colour='country')) +
geom_smooth(method="lm", se=False))


# We can also change our straight regression line into a curvy line using a locally 
#weighted regression (known as a loess line). To do this, change from:

##the loess, weighted regression is the defaut of geom_smooth() so we just need to have
## geom_smooth() empty like this
# geom_smooth(method="lm", se=False) to geom_smooth()

(ggplot(dataFrameAmericas) +
 aes(x='year', y='lifeExp', colour='country')+
 geom_point() +
 geom_smooth())   

(ggplot(dataFrameAmericas, aes(x='year', y='lifeExp')) +
geom_point(aes(colour='country')) +
geom_smooth()) 


# We can also use ggplot to plot life expectancy over time for each continent in a 
#given panel. To do so, run the following code:

(ggplot(dataFrameGapMinder, aes(x='year', y='lifeExp')) +
geom_point() +
facet_wrap('continent')) ##facet_wrap makes a different plot for each continent
    

# (ggplot(df, aes(x='year', y='lifeExp')) +
# geom_point() +
# facet_wrap('continent'))

# Add a loess regression line to each of the panels above. 
#Colour all of the regression lines orange.

(ggplot(dataFrameGapMinder, aes(x='year', y='lifeExp')) +
geom_point() +
geom_smooth(colour='orange')+
facet_wrap('continent'))

# Open ended question

# Using visualisations, assess the following statement:

# "Increases in gdp per capita are associated with increases in life expectancy."


(ggplot(dataFrameGapMinder, aes(x='gdpPercap', y='lifeExp')) +
geom_point() +
geom_smooth(colour='orange')+
facet_wrap('continent'))

(ggplot(dataFrameGapMinder, aes(x='gdpPercap', y='lifeExp')) +
geom_point() +
geom_smooth(colour='orange'))


#%%

#Implementing simple linear regression with numpy and with scikit-learn on simulated data

# Linear regression from scratch with numpy
# Simulate inputs

# Simulate inputs 𝑥1,…,𝑥𝑛
# from standard Normal distribution as a column vector, i.e. a matrix with 1 column
# and 𝑛 rows:

np.random.seed(123) # make it reproducible
n = 20 # sample size    
x = np.random.normal(size=(1,n))


# Simulate outputs as
# 𝑦𝑖=1+0.5𝑥𝑖+𝜖𝑖
# where 𝜖𝑖 has a Normal distribution with mean zero and standard deviation 0.2:

# loc = mean , scale = standard deviation, 
e = np.random.normal(loc=0,scale=0.2,size=x.shape)

y = 1 + 0.5 * x + e

## you need to put the 'o' to get the points
plt.plot(x,y,'o')
plt.xlabel('input x')
plt.ylabel('output y')
plt.show()













#%%

# Predicting bicycle traffic by linear regression

# This is my (i.e. Ben Lambert's) attempt to create a predictive model of bicycle traffic 
#in Seattle. Crucially, it is not an attempt to answer the problem questions; rather, it 
#is supposed to illustrate an overall approach to modelling data. It is also not supposed 
#to be definitive: many different models can often provide an adequate explanation of the 
#data.

# Whenever you model data, you should take a critical approach to modelling. Always 
#remember that a model is a simplified version of the world, so you need to ask whether 
#the various simplifications are justified. As such, you need to take a proactive approach
# to searching for flaws in your models. Usually, the best way to elucidate these flaws
# is to visualise the data and model predictions, and I hope to demonstrate this approach
# here.

# First, we load necessary packages and data.

import datetime
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

a = "C:\AppliedDataScienceAndStatistics\Applied-Data-Science-and-Statistics\Term1\ApplicationOfDataAndStats\week9\FremontBridge.csv"
b = "C:\AppliedDataScienceAndStatistics\Applied-Data-Science-and-Statistics\Term1\ApplicationOfDataAndStats\week9\SeattleWeather.csv"


dfFermonBridge = pd.read_csv(a)
dfSeattleWeather = pd.read_csv(b)

##convert all names of collumns to lower case

dfFermonBridge.columns = map(str.lower, dfFermonBridge.columns)
dfSeattleWeather.columns = map(str.lower, dfSeattleWeather.columns)

##renaming a collum
dfSeattleWeather.rename(columns={'tavg': 'tavgr'}, inplace=True)
dfSeattleWeather.rename(columns={'tavgr': 'tavg'}, inplace=True)

dfSeattleWeather.dtypes
dfFermonBridge.dtypes
## as we can see here both date collums don't have the correct date type

## %m is month
## %d is day
## %Y is year
## %H is hour
## %M is minutes
## %S is second
## %p is am or pm
## don't forget that we got to put it in the exact same other with the right characters
## that break the values between each other like / or : 
dfFermonBridge["date"] = \
    pd.to_datetime(dfFermonBridge['date'], format="%m/%d/%Y %H:%M:%S %p")
dfSeattleWeather['date'] = pd.to_datetime(dfSeattleWeather['date'], format= "%Y-%m-%d")

## The bike data is hourly; the weather data is daily. So we want to aggregate the former.

## there are 2 ways to strip the hour of the date 

dfFermonBridge['date'] = \
    pd.to_datetime(dfFermonBridge["date"].dt.strftime('%Y-%m-%d'), format="%Y-%m-%d")

##or 
i = 0
for i in range(len(dfFermonBridge)):
    
    auxString = dfFermonBridge['date'][i]
    auxDate = str(auxString).split(" ")[0]
    
    dfFermonBridge['date'][i] =  auxDate
        
    i = i +1

dfFermonBridge.dtypes

#Now let's aggregate the data to be daily.
## now we will group by day

dfFermonBridgePerDay = dfFermonBridge.groupby(['date'])['fremont bridge west sidewalk'].sum()





#%%



