








######################################################## EX 13 #####################################################


a = 1664525
c = 1013904223 
m = 2^32

d = as.numeric(Sys.time()) # seed


rn = vector(length = 10)

for (i in 1:10) {
  d = (a*d+c)%%m
  rn[i] = d/m
}

randomGeneration = function(N=10){
  a = 1664525
  c = 1013904223 
  m = 2^32
  
  d = as.numeric(Sys.time()) # seed
  
  
  rn = vector(length = N)
  
  for (i in 1:N) {
    d = (a*d+c)%%m
    rn[i] = d/m
  }
  return(rn)
}


randomGeneration(1)
randomGeneration(5)
randomGeneration(20)
randomGeneration(100)

x = randomGeneration(1000)
y = -log(x)

hist(y)
