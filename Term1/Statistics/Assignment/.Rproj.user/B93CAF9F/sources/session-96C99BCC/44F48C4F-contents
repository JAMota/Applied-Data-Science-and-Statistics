#number of mutations of covid

set.seed(1234)

myMytation = virus_mutation(N=5)

# here the poison distribution is the most stuitable

#Poisson, X ~ Poisson(lambda)

#X1,X2,X3,X4,X5

#estimate of lambda

N = 1000
myLambda = vector(length = N)
for (i in 1:N) {
  myMytation = virus_mutation(N=5)
  myLambda[i] = mean(myMytation)
}

library(tidyverse)

data.frame(Lambda = myLambda) %>% 
  ggplot(aes(x=Lambda)) +
  geom_density()












