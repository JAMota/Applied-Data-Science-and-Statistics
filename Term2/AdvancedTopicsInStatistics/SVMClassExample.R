

# Import the gene dataset
gene <- read.csv("C:/AppliedDataScienceAndStatistics/Applied-Data-Science-and-Statistics/Term2/AdvancedTopicsInStatistics/StatsTopic4_files/gene_expression.csv",row.names=1)

# Extract labels as factors - B- or T-cell acute lymphocytic leukaemia
y <- as.factor(substr(colnames(gene),1,1))
x <- t(gene)
rownames(x) <- NULL

# Split data into Train and Test dataset
ii <- createDataPartition(y, p=.7, list=F) ## returns indices for train data 
xTrain <- x[ii,]; yTrain <- y[ii]
xTest <- x[-ii,]; yTest <- y[-ii]

## SVM with linear kernel ##

library(kernlab) 
mdl <- train(x=xTrain,y=yTrain, method='svmLinear') 
print(mdl)
# Test model on testing data
yTestPred <- predict(mdl, newdata=xTest)
# yTestPred <- mdl %>% predict(xTest) 
confusionMatrix(yTestPred, yTest) # predicted/true




# Import the wine dataset
wine <- read.csv("C:/AppliedDataScienceAndStatistics/Applied-Data-Science-and-Statistics/Term2/AdvancedTopicsInStatistics/StatsTopic4_files/wine.csv")

y <- wine[,1]
x <- wine[,-1]

ii <- createDataPartition(y, p=.7, list=F) ## returns indices for train data 
xTrain <- x[ii,]; yTrain <- y[ii]
xTest <- x[-ii,]; yTest <- y[-ii]


## SVM with linear kernel ##

library(kernlab) 
mdl <- train(x=xTrain,y=yTrain, method='svmLinear') 
print(mdl)
# Test model on testing data
yTestPred <- predict(mdl, newdata=xTest)
# yTestPred <- mdl %>% predict(xTest) 
confusionMatrix(yTestPred, yTest) # predicted/true

