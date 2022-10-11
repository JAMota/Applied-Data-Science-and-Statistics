# dataframes utilize vectors

a = c(1,2,3,4,5)
b = c(-2,-4,5,6,7)

myDataFrame = data.frame(a,b)

print(myDataFrame)

#see all datasets in R
data()

c = c(2,3,1,6,-1)

ExerciseDataFrame = data.frame(a,b,c)

print(ExerciseDataFrame)

#count the number of rows
nrow(ExerciseDataFrame)

#count the number of colums
ncol(ExerciseDataFrame)

#name the variables
names(ExerciseDataFrame)

#shows the structure of the dataframe on with each vector as a string in a single line
str(ExerciseDataFrame)

#shows all the entire vector of the variable a
ExerciseDataFrame[,'a'] 

#shows the first row of all the collums of variables
ExerciseDataFrame[1,]

# row number 3 from the variable b
ExerciseDataFrame[3,'b']

#extract a variable from the dataframe
ExerciseDataFrame$b

#create a new variable by adding a and b
ExerciseDataFrame$aplusb = ExerciseDataFrame$a + ExerciseDataFrame$b

ExerciseDataFrame$aplusb

#create a a times b variable
ExerciseDataFrame$aTimesB = ExerciseDataFrame$a *ExerciseDataFrame$b

if(1==1 && 2==2){
  print('qiuckmaths')
}

if(1==1 || 1==2){
  print('swift calculus')
}

#extract parts of the dataframe where a certain condition is true

subset(ExerciseDataFrame, a < 4)

subset(ExerciseDataFrame, b = 4)


#reading data from other sources such as CSV comma separated values
dataframeFromCsv = read.csv(file='mtcars.csv')


carExamplesDataSet = data.frame(mtcars)

drugCostList= c(2.0,4.0,6.2,8.0,8.0,8.0,12.0,15.0,15.0,18.0,18.2,20.0,20.0,20.0,21.0,22.0,
              24.2,27.0,27.0,27.0,28.0,29.7,29.7,29.7,29.7,29.7,30.0,30.0,31.0,41.4,42.3,
              45.4,45.4,45.4,45.4,45.4,45.4,45.4,45.4,45.4,49.4,50.8,51.4,53.4,56.0,57.0,
              57.4,59.0,59.4,60.0,61.5,65.4,65.4,65.4,65.4,67.0,90.8,92.0,94.0,94.0,94.0,
              94.0,94.0,94.0,94.7,105.0,125.0,126.0,130.0,130.0,130.0,151.2,160.0,177.0,
              187.0,187.0,194.4,194.4,194.4,212.4,213.0,233.0,267.0,320.4)


#see how many values are stored in the vector

length(drugCostList)

#calculate the average/mean

mean(drugCostList)

#calculate the mean

sum(drugCostList)/length(drugCostList)

median(drugCostList)

#calculates the variance 
var(drugCostList)
?var

#standard deviation
sd(drugCostList)

min(drugCostList)
max(drugCostList)

#drug cost range

max(drugCostList)-min(drugCostList)

# Lower quartile of the drug costs.
quantile(drugCostList, probs = 0.25)

# Upper quartile of the drug costs.
quantile(drugCostList, probs = 0.75)

# Interquartile range of the drug costs.
IQR(drugCostList)

summary(drugCostList)

# Drug Class in a vector
drugClass <- c("A","C","C","C","A","A","A","B","A","B","B","B","B","A","A","A","B",
               "A","A","A","C","A","B","B","C","A","C","A","C","A","B","C","C","B",
               "B","A","C","B","A","B","B","A","A","C","B","B","A","B","C","C","B",
               "A","C","B","C","A","B","C","C","C","A","A","A","C","B","A","A","B",
               "C","A","B","A","A","B","C","C","A","A","C","C","A","B","C","C")


# Calculating the number of each drug type
table(drugClass)

# Probability of each drug type
prop.table(table(drugClass))


# Categorising the drugcost: (i) Low (1-50), (ii) Medium (50-100),
# (iii) High (100-200) and (iii) Very high (+201).
# Data to be categorised
drugCostCat <- cut(drugCostList, 
                   breaks = c(0,50,100,200,max(drugCostList)), # Breaks for the categories
                   labels = c('Low','Medium','High','Very High')) # Category names


table(drugCostCat)

#call the dataset into R
data(mtcars)

# Viewing the structure of the dataset
str(mtcars)

head(mtcars)

# Extracting the number of cylinders
mtcars$cyl
