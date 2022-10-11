library(ggplot2)
require(raster)
library(tidyverse)


men = read.csv("C:/WorkingWithData/week3/data9b_men.csv")


women = read.csv("C:/WorkingWithData/week3/data9b_women.csv")

men$gender = "man"
women$gender = "woman"

women$ID 
men$ID

human = bind_rows(men,women)

ggplot(data = human, aes(x=steps,y=bmi)) +
  geom_point(aes(color = gender))

mylm = lm(steps~gender+bmi, data=human)

summary(mylm)

#bmiCentered =
















