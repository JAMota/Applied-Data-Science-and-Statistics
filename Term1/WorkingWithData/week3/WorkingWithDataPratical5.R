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

betweenVarianceOfTheCollection <- (1/4)*sum((sapply(CollectionOf5Elementes,mean)-totalMean)^2)

#This calculates T
## T =  withinVariance + (1 + 1/m )B
bigt <- withinVarianceIOfTheCollection + (1+(1/5))*betweenVarianceOfTheCollection
#This calculates the standard error of T

sebigt <- sqrt(bigt)

######################################################### Lappy and lists #########################################

## finds the square of each element in the vector
lappyTest = lapply(1:3, function(x) x^2)
lappyTest
## attention, the output of the function is actually a list.
## a list is a generic vector containing other objects instead of just values

listOfNumbers = c(2, 3, 5)
listOfStrings = c("aa", "bb", "cc", "dd", "ee")
listOfBooleans = c(TRUE, FALSE, TRUE, FALSE, FALSE)
CollectionOfLists = list(listOfBooleans, listOfStrings, listOfBooleans, 3) # x contains copies of n, s, b

## We can select just a single list from the collection by using the [] operator

CollectionOfLists[2]


################################################## MATRIX #########################################################

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
library('naniar')

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
## then by combining all the imputed data sets we can preserve the randomness/uncertainty 


## graphs/maps and lets your see missing values of a dataset passed to amelia
?missmap

missmap(ameliaPassedDataSet)

## see the first imputed data set (filled in with random plausibly numbers)

head(ameliaPassedDataSet$imputations$imp1)


## we can run a regression model on each imputed data set
regr_model <- lm(gdp_pc ~ civlib + trade, data = ameliaPassedDataSet$imputations$imp1)
summary(regr_model)

## but we can also simply do this for each data set at the same time using lappy

averageAmeliaOutputOfImputedValues = lapply(ameliaPassedDataSet$imputations, function(i) lm(gdp_pc ~ civlib + trade,
                                                               data = i))
averageAmeliaOutputOfImputedValues


##Averaging across the results is a little bit trickier than our earlier example because we have to extract
## the coefficients and standard errors from each model, format them in a particular way, and then feed that
## structure into the mi.meld function. The ‘mi.meld’ function applies Rubin’s rules to the summary statistics
## we have extracted


##The ‘lapply’ function takes the list of fitted models contained in ‘averageAmeliaOutputOfImputedValuest’ and  
## applies a function to each element of that list. 
##The function takes a ‘summary’ of each model output, and extracts the coefficients from that summary (using ‘coef’) 
## It extracts the first or second column depending on whether we want coefficients or standard errors extracted

coefecientAmelia <- averageAmeliaOutputOfImputedValues %>% # We begin with our list of models
  sapply(coef) %>% # we use sapply to extract coefficients from each model
  t()

# This creates a function to extract a standard error from a model
#This helps us as we can just call this function in our lapply
## this is standard erros
my_SE_extractor <- function(model) {summary(model)$coef[,"Std. Error"]}


standardErrorAmelia <- averageAmeliaOutputOfImputedValues %>% # we begin with our list of linear models again
  sapply(my_SE_extractor) %>% #we apply our standard error extracting function
  t() #we take a transpose of the matrix (just making rows into columns and vice versa)

#Now we are ready to use mi.meld
?mi.meld
## mi.meld() - it combines multiple results from multiple imputed(randomly filled up) data sets
mi.meld(coefecientAmelia, standardErrorAmelia)

## set a random seed to ensure "random" number can be easily optained again
?set.seed

set.seed(20221012)

################################################### ex 1  ##########################################################
##  regression model of the 5 imputed data sets

regressionModel1 <- lm(gdp_pc ~ civlib + trade, data = ameliaPassedDataSet$imputations$imp1)
regressionModel2 <- lm(gdp_pc ~ civlib + trade, data = ameliaPassedDataSet$imputations$imp2)
regressionModel3 <- lm(gdp_pc ~ civlib + trade, data = ameliaPassedDataSet$imputations$imp3)
regressionModel4 <- lm(gdp_pc ~ civlib + trade, data = ameliaPassedDataSet$imputations$imp4)
regressionModel5 <- lm(gdp_pc ~ civlib + trade, data = ameliaPassedDataSet$imputations$imp5)

regressionModel1$coefficients

##I will now process by extracting each civilian liberty coefficient value from the data using the 
## sheer power of cheating and data subtring extraction

coefficientRegressionModel1 = substr(regressionModel1$coefficients, 1,20)
civilianLibertiesCoefficient1 = coefficientRegressionModel1[2]
civilianLibertiesCoefficient1 = as.numeric(civilianLibertiesCoefficient1)

coefficientRegressionModel2 = substr(regressionModel2$coefficients, 1,20)
civilianLibertiesCoefficient2 = coefficientRegressionModel2[2]
civilianLibertiesCoefficient2 = as.numeric(civilianLibertiesCoefficient2)

coefficientRegressionModel3 = substr(regressionModel3$coefficients, 1,20)
civilianLibertiesCoefficient3 = coefficientRegressionModel3[2]
civilianLibertiesCoefficient3 = as.numeric(civilianLibertiesCoefficient3)

coefficientRegressionModel4 = substr(regressionModel4$coefficients, 1,20)
civilianLibertiesCoefficient4 = coefficientRegressionModel4[2]
civilianLibertiesCoefficient4 = as.numeric(civilianLibertiesCoefficient4)

coefficientRegressionModel5 = substr(regressionModel5$coefficients, 1,20)
civilianLibertiesCoefficient5 = coefficientRegressionModel5[2]
civilianLibertiesCoefficient5 = as.numeric(civilianLibertiesCoefficient5)


avereageCoefficientOfCivilianLiberties = mean(c(civilianLibertiesCoefficient1,civilianLibertiesCoefficient2,
    civilianLibertiesCoefficient3,civilianLibertiesCoefficient4,civilianLibertiesCoefficient5))

################################################### ex 2  ##########################################################
##compare the average coefficient of civilian liberties with the mi.meld result


mi.meld(coefecientAmelia, standardErrorAmelia)

avereageCoefficientOfCivilianLiberties

?mean


################################################### ex 3  ##########################################################

##By using multiple big scale imputations we can always get more than 1 data set that we use for calculations
## compared to the only 1 data set we get from eliminating all the rows with null values.
## by having many values of imputed data set such as 1000 or 10000 we mitigate the fake values since
## the computer doesn't know which are fake values and actual collected data 
## then by combining all the imputed data sets we can preserve the randomness/uncertainty 


################################################### ex 4  ##########################################################

##nrow - counts the number of rows in a data set
m = nrow(ameliaPassedDataSet$imputations$imp1) 

##step 0 calculate Q

#Q = 1/m * sum(Qi)

Q = 1/m * sum(ameliaPassedDataSet$imputations$imp1$civlib)

## remember that because no civ lib value was missing all the imputed data sets have the same values for civlib so
## we don't have to take into account multiple data sets
missmap(ameliaPassedDataSet)

##step 1 calculate between variance for every data set

#B = 1/(m-1) * sum(Qi - Q)^2

B = 1/(m-1) * (sum(ameliaPassedDataSet$imputations$imp1$civlib) - Q)^2


##step 2 calculate the within variance for every data set


# σ = sqrt((sum( - mean()))/(m-1))
#
# sum(xi - x)
#
#xpto = mean(ameliaPassedDataSet$imputations$imp1$civlib)
#
#totalXi = 0
#i=0
#xpto
#
#
#for (i in 1:m) {
#  
#  aux = xpto - ameliaPassedDataSet$imputations$imp1$civlib[i]
#  
#  totalXi = totalXi + aux
#  
#  print(totalXi)
#  
#}
#topHalfOfσ = totalXi^2
#
#σ = (topHalfOfσ/(m-1))
#


##instead of doing standard deviation by computing it like an absolute idiot you can use the sd function
## please for the love of god check for these functions first you absolute dummy

?sd


standardDeviation = sd(ameliaPassedDataSet$imputations$imp1$civlib)

#SE =  σ (sample standard deviation) / sqrt(m)

SE = (standardDeviation / sqrt(m))
 
#V = 1/m + sum(SE)^2 

V = 1/m + (sum(SE)^2)




## step 3 calculate T

#T = V + (1 +1/m) * B

T = V + ((1 + (1/m))*B)

##step 4 calculate Standard error by doing square root of T and compare to mi.meld

# standard error of T is sqrt(T)

SET = sqrt(T)

SET

mi.meld(coefecientAmelia, standardErrorAmelia)

################################################### SOLUTION TO EX4 ###############################################

#The colMeans function takes the mean of the columns and returns a vector the same length
#as the number of columns
## colMeans - it gives the mean of all the columns
?colMeans

coefmeans <- colMeans(coefecientAmelia)
##########
#Building the components for Rubin’s rules
##########
#V - the within variance. We square the extracted standard errors and take colMeans
V <- colMeans(standardErrorAmelia^2)
# We calculate the between variance
# the sweep function takes 4 arguments - 1. the object to be operated on (a matrix )
# 2. an indicator: 1 = rowwise, 2 = columnwise
# 3. a vector with the same number of columns or rows (depending
# on the previous parameter)
# 4. a function. In this case subtraction
B <- ((1/(5-1)) *colSums((sweep(coefecientAmelia,2,coefmeans,"-"))^2))
#Calculating the total variance
T <- V+ (1 + 1/5) *B
#Square rooting gives the pooled variance
SEt <- sqrt(T)
#Show the output
SEt

mi.meld(coefecientAmelia, standardErrorAmelia)


################################################# TIDYVERSE VERSION ################################################

## Note, unclass() is necessary because bind_rows() will complain when dealing with lists with the amelia class,
## which is what amelia() returns










