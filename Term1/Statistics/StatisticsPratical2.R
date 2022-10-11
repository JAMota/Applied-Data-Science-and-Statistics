######################################################## EX 13 #####################################################

#X ~ Binom(100,0.05)
# p(X=5)

#sample function



counter = 0
repeats = 1000000

for (i in 1:repeats) {
  
  x = sample(c(0,1),100,replace=T,prob = c(0.95,0.05))
  
  sum(x)
  
  if(sum(x)==5){
    counter = counter + 1
  }
  
}

prob=counter/repeats
print('prob =')


##RBINOM

#repeating the experiment once

rbinom(1,100,0.05)

#repeat a large number of times
repeats = 1000000

#repeat experiment a large number of times
rbinom(repeats,100,0.05)

#counting the success cases
total = sum(rbinom(repeats,100,0.05)==5)

#probability
prob = total / repeats
print(prob)

#exact probabolity 
dbinom(5,100,0.05)

##warning in R the professor wants us to estimate the probability using a large amount of repeats instead of just
## calculating the exact probability



######################################################## EX 14 #####################################################
