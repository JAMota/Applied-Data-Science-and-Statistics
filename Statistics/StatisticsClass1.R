#for loop
 
for(i in 1:5){
  print(2*i)
}

#non numerical vector

for(i in c('head','tails')){
  print(i)
}

#if statement
#when it is true it executed what is inside the if statement
#when the statement is false it skips ahead

if(1!=2){
  print('Hello world!')
}

#logical operators

# < > ==  !=

#logical AND &&  (logical gates)

if(4<5 && 5>3){
  print('Hello there!')
}

# logical OR || 

if(1==1 || 1==2){
  print('wow much true')
}


# Relative frequency
# if the event we are interested happens the counter is incremented
#repeat for a large number of times > 10000

#randomly select a,b,c from the set (1,2,3,4,5,6,7)
#what are the chances of a + b > c


# in a sample from 1 to 7 it picks 3 numbers and it doesn't replace


counter = 0
largeNumberOfTries = 10000

for(i in 1:largeNumberOfTries){
  
  x = sample(1:7,size=3,replace=F)
  
  
  if( x[1]+x[2]> x[3]){
    #print('its true')
    counter = counter + 1
  }
}

prob = counter/largeNumberOfTries
print(prob)

# what are the chances of there is a number that is in the correct place in comparison to natural number position


y = 1:10

counter = 0
largeNumberOfTries = 10000


for(i in 1:largeNumberOfTries){
  
  x = sample(1:10)
  
  #when we compare vectors using == what R does is compare if vector1[n] == vector2[n] for the entire vectors
  
  x==y
  
  #since R automatically converts booleans to integers TRUE is converted to 1 and FALSE is converted to 0
  if (sum(x==y) > 1){
    counter = counter +1
  }
  
}

prob = counter/largeNumberOfTries
print(prob)


#consider a coin
#in six tosses what are the odds of having a different side each toss

true1 = c('T','H','T','H','T','H')
true2 = c('H','T','H','T','H','T')

event1 = sample(c('H','T'),size=6,replace=T)

counter = 0

for (i in 1:10000) {
  

if(sum(event1==true1) == 6 || sum(event1==true2) == 6){
  counter = counter + 1
}

}



for(i in 1:10000){
  for (j in 1:6) {
    x = sample(c(0:1),size=6,replace=1)
  }
}

