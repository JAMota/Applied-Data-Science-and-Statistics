install.packages('Amelia')
install.packages('broom')

library(tidyverse)
library(broom)
library(Amelia)



# This sets the seed that ’sample’ uses and ensures we will
#get the same random numbers if we repeated fill them with plausible values
## we generate a vector with a total of 10 positions, the first 7 positions are filled with values the other 3
## are nulled so we can fill them with plausible values
set.seed(1234)
x <- c(sample(1:10, 7, TRUE), rep(NA, 3))
x

## we can't just do a direct mean of the entire vector because R doesn't know what to do with the null values
mean(x)

## we can however just remove the null values during the calculation to get a mean of the existing values
mean(x, na.rm = TRUE)

## to estimate the standard error we use the standard deviation devided by the square root of the sample size
sd(x, na.rm = TRUE)/sqrt(sum(!is.na(x)))
## here we also use the not is.na to check how many values aren't null aka the actual sample size
!is.na(x)

# This takes the elements of x that are not missing and adds on
# 3 randomly chosen x values to replace the missing values. It
# does this 5 times and saves the result as ’imp’
CollectionOf5Elementes <- replicate(5, c(x[!is.na(x)], sample(x[!is.na(x)], 3, TRUE)), simplify = FALSE)
CollectionOf5Elementes

## the first 7 values are all the same as we had previously but now we generated randomly the other 3 missing values

#This calculates q bar, by using sapply to take
#a mean of each list element of ’imp’ and then taking the
#mean of those means
?sapply

## sapply - applies a function over each element of a vector
totalMean <- mean(sapply(CollectionOf5Elementes,mean))
##used to calculate the mean of the means from each vector

#This calculates the within variance
## Within-Group Variation - The total variation in the individual values in each group and their group mean
## within variance = Σ(Xij – Xj)2 
##  Σ: a symbol that means “sum”
##  Xij: the ith observation in group j
##  Xj: the mean of group j


withinVarianceIOfTheCollection <- (1/5)*sum((sapply(CollectionOf5Elementes,sd)/sqrt(10))^2)

#This calculates the between variance, denoted B above
## Between Group Variation - The total variation between each group mean and the overall mean
## between variation =  Σnj(Xj – X..)2 
##  nj: the sample size of group j
##  Σ: a symbol that means “sum”
##  Xj: the mean of group j
##  X..: the overall mean

betweenVarianceOfTheCollection <- (1/4)*sum((sapply(CollectionOf5Elementes,mean)-qbar)^2)

#This calculates T
## T =  withinVariance + (1 + 1/m )B
bigt <- withinVarianceIOfTheCollection + (1+(1/5))*betweenVarianceOfTheCollection
#This calculates the standard error of T

sebigt <- sqrt(bigt)

######################################################### Lappy and lists ###########################################

## finds the square of each element in the vector
lappyTest = lapply(1:3, function(x) x^2)
lappyTest
## attention, the output of the function is actually a list.
## a list is a generic vector containing other objects instead of just values

listOfNumbers = c(2, 3, 5)
listOfStrings = c("aa", "bb", "cc", "dd", "ee")
listOfBooleans = c(TRUE, FALSE, TRUE, FALSE, FALSE)
CollectionOfLists = list(n, s, b, 3) # x contains copies of n, s, b

## We can select just a single list from the collection by using the [] operator

CollectionOfLists[2]


################################################## MATRIX ##########################################################

#Creating a matrix of means

meanCoefficientMatrix = CollectionOf5Elementes %>% #begin with our imputed data list object
  sapply(mean) %>% #pipe it into sapply and take the mean of each element
  matrix() # pipe it into a matrix

meanCoefficientMatrix

#Creating a matrix of standard errors
standardErrorMatrix <- CollectionOf5Elementes %>% #begin with our imputed data list object
  sapply(sd)%>% #pipe it into sapply and take the standard deviation of each element
  '/'(sqrt(10)) %>% # divide by the square root of 10 to get standard errors
  matrix() # make it a matrix

standardErrorMatrix

?mi.meld
## mi.meld - combines sets of estimates and their standard errors from different datasets into one set of results
mi.meld(meanCoefficientMatrix, standardErrorMatrix)  



africa

summary(africa)


# This fits a linear model were GDP is predicted using civil liberties and trade
regressionModel = lm(gdp_pc ~ civlib + trade, data = africa)
summary(regressionModel)

?summary
 ##TODO ASK how am I supposed to see from the summary that some values are missing?

#install.packages('naniar')
#library('naniar')

##graphs/maps and gives a percentage of the missing variables values in the dataset

vis_miss(africa)


?amelia

#Impute missing values 
## aka it adds aditional values to "replace" the missing/nulled values in the dataset

ameliaPassedDataSet <- amelia(x = africa, #use the africa data
                     m = 5, # repeat 5 times
                     idvars="country", #This specifies country as an ID variable, not to be imputed.
                     logs = "gdp_pc", #variables that require log transform
                     p2s = 1) #Output type

## the idea of multiple imputations is to give multiple filled in data sets
## this is more appropriate because the computer doesn't know which are fake values and actual data
## with this the filled in fluctuate between average 
## we should do a looot of imputations 100, 1000, 10000
## then by combining all the imputed data sets we can preserve the randomness/uncertantity 


## graphs/maps and lets your see missing values of a dataset passed to amelia
?missmap

missmap(ameliaPassedDataSet)

head(ameliaPassedDataSet$imputations$imp1)












