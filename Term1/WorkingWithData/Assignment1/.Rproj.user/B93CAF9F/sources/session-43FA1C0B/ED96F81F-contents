## very useful to install before using install.packages('tidyverse')

library(tidyverse)

#tidy data is useful because it becomes tidy in a very specific way that is common to all other tidy data 

##Specifically, a tidy data set is one in which:
#• rows contain different observations;
#• columns contain different variables;
#• cells contain values

?iris

head(iris)

##filter - filters rows with tidyverse

filter(iris, Species == 'setosa')

##arrange - arrange function lets you sort alphabetically and numerically

arrange(iris,Species,Sepal.Length)

##select - selects just specific columns from the data sect ex just column 1, 3 and 7 and presents them in that order

select(iris, Species, Sepal.Length, Sepal.Width)

# using start_with we can specify what is the name of the columns we want to display
select(iris, Species, starts_with("Sepal"))

# we can also remove them individually

select(iris, -Petal.Length, -Petal.Width)

##we can add more columns and derivate them from existing columns

mutate(iris, Sepal.Length2 = Sepal.Length^2)


##attach - used to add as an new additional column to the data set a specific variable that we have created
##detach - removes the attached variables from the data set

##NOTE! - is it not a good pratice to attach and detach variables to the dataset due to it being very prone to errors

attach(iris)
Sepal.Length2 = Sepal.Length^2

detach(iris)
Sepal.Length2 = Sepal.Length^2

## in R we can pipes similar in the way we use them in linux to chain multiple commands with their respective
##command results 
##     %>% is the equivalent of ||

iris %>% filter(Species == "versicolor") %>% head()

##TODO ASK if when piping we use functions by leaving them empty inside the pipe

##the pipe operator must be at the end of the line if we wish to split the code over multiple lines

## %>% can be place by using ctrl + shift + m

iris %>%
  filter(Species == "versicolor") %>%
  select(Species, starts_with("Sepal")) %>%
  mutate(Sepal.Length2 = Sepal.Length^2) %>%
  arrange(Sepal.Length) %>%
  head()

##group_by - basically the same type of group by in mysql where every result of that type of variable is aggregated
##as one and it allows to make calculations
iris %>%
  group_by(Species) %>%
  summarise(mn = mean(Sepal.Length))

?summarise
##summarise - creates a new data frame where rows are a combination of grouping variables, you use it to 
## create new variables on the new data using calculations or mutations from the previous data set 

#task page 6


iris %>%
  group_by(Species) %>%
  summarise(MeanSepalLength = mean(Sepal.Length),##create a variable that is assigned the mean of the sepal length
            VarSepalLength = var(Sepal.Length), ##create a variable that is assigned the variance of the sepal length
            MeanSepalWidth = mean(Sepal.Width), ##create a variable that is assigned the mean of the sepal width
            VarSepalWigth = var(Sepal.Width)) ##create a variable that is assigned the variance of the sepal width

## ‘summarise()‘ ungrouping output (override with ‘.groups‘ argument) ?????? TODO ASK


################################### Reshaping Data sets #######################################################


##gather - takes multiple columns and groups them in key-value pair (like an hash map)
?gather
##spread - takes a key-value and spreads them into two different variables
?spread

##tidyign up a data set

##load the dataset don't forget that R only accepts paths that use the / for separating folders like it was
## a linux path so when copying from windows you have to change from \ to /

GDPIncome = read.csv("C:/WorkingWithData/indicator_gapminder gdp_per_capita_ppp.csv")

##this data is incredibly messy and untidy 
GDPIncome

##first to start tidying it up we will rename the first collum which was incorrectly called gdp per capita 

GDPIncome = GDPIncome %>% 
  rename(country = 'GDP.per.capita')

##### NOTE: only do this when you have a copy of the data set saved in another place such as the csv file where
#### we extracted the data set from. Don't destroy the original data
### please for the love of god test the command before assigning it to the same data set

head(GDPIncome)

## to continue to tidy up the data set we will collapse the year columns down so we can ideally have a collum with
## the year and the associated value of that year

##gather usage example - gather( key = valueToGroupBy,
##                               pair = secondValueAssociatedWIthFirstValue,
##                               c( -city)) ## all the columns we want to group by in the wide format of data
##                                          ## in this case we use -city because we want all the other columns expect
##                                          ## the one that includes the city to be paired up but we could just
##                                          ## name all the other columns instead of the city (less practical)
## extra note: if we see the csv for this example one row is just the name(country) and the entire values of the gdp
## that correspond to the year assigned on the first row

GDPIncome = GDPIncome %>% 
  gather(key = year, value = gdp, c(-country))

head(GDPIncome)

## if we look at out environment we can see that the year is considered as a string which doesn't make any sense
## because we the possible values of the year can only be numerical
## REMEMBER NA is the R version of NULL

GDPIncomeNumericYear = GDPIncome

GDPIncomeNumericYear$year = gsub('X', '', GDPIncomeNumericYear$year)
head(GDPIncomeNumericYear)

GDPIncomeNumericYear = GDPIncomeNumericYear %>% 
  mutate(year = as.numeric(year))

##using sapply we can check the variable and the class sapply(value, whatWeWantToCheck)

sapply(GDPIncomeNumericYear$year, class)

##count how many missing values

sum(is.na(GDPIncomeNumericYear$country)) 

GDPIncomeNumericYear$country

##TODO ASK what was supposed to happen when we make the sum
## it doesn't make sense since we don't have gdps from non existent countries


GDPIncomeNumericYear %>% filter(is.na(country)) %>% summary()

##removing all the countries that don't have a single value of GDP
GDPIncomeNumericYearAndNullCountriesRemoved = GDPIncomeNumericYear %>% filter(!is.na(gdp))

GDPIncomeNumericYearAndNullCountriesRemoved

## we will now focus on only the data starting in 1990

GDPIncomeNumericYearAndNullCountriesRemovedStartingFrom1990 = 
  GDPIncomeNumericYearAndNullCountriesRemoved %>% filter(year >= 1990)

summary(GDPIncomeNumericYearAndNullCountriesRemovedStartingFrom1990)

##to do this all at once and get it all properly tidy

##WARNING!!!!!!!using read.csv is buggy and gives extra characters like in this case

GDPIncomeNeedGrubbingToBecomeTiddy = read.csv("C:/WorkingWithData/indicator_gapminder gdp_per_capita_ppp.csv") 
GDPIncomeNeedGrubbingToBecomeTiddy = GDPIncomeNeedGrubbingToBecomeTiddy %>% 
  rename(country = 'GDP.per.capita') %>%
  gather(year, gdp, -country); GDPIncomeNeedGrubbingToBecomeTiddy$year = gsub(
    'X', '', GDPIncomeNeedGrubbingToBecomeTiddy$year); GDPIncomeTidy = GDPIncomeNeedGrubbingToBecomeTiddy %>% 
  mutate(year = as.numeric(year)) %>%
  filter(!is.na(country)) %>%
  filter(!is.na(gdp)) %>%
  filter(year > 1990)

## for a less error prone solution we can read the file using read_csv which no longer require us to use 
## bgsub to parse the extra character out of the data

GDPIncomeTidyInOneGo = read_csv("C:/WorkingWithData/indicator_gapminder gdp_per_capita_ppp.csv") 
GDPIncomeTidyInOneGo = GDPIncomeTidyInOneGo %>% 
  rename(country = 'GDP per capita') %>%
  gather(year, gdp, -country) %>% 
  mutate(year = as.numeric(year)) %>%
  filter(!is.na(country)) %>%
  filter(!is.na(gdp)) %>%
  filter(year > 1990)




##mean GDP from all the countries starting from 1990


GDPIncomeTidy %>%
  group_by(country) %>%
  summarise(meanGDP = mean(gdp))

## mean GDP for each year starting from 1990

GDPIncomeTidy %>%
  group_by(year) %>%
  summarise(meanGDP = mean(gdp))



















