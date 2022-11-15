library(tidyr)
library(tidyverse)
library(ggplot2)
library(GGally)

ozone = read_csv("ozone.csv")


## The exploratory analysis starts summarising the data and then
##by plotting the information and attempt to detect any obvious trends 

summary(ozone)


ggpairs(ozone,
        lower = list(continuous = "smooth"),
        diag=list(continuous = "barDiag"),
        axisLabels= "show")


























