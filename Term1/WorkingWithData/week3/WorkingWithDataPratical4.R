install.packages('ggplot2')
install.packages('raster')

require(ggplot2)
require(raster)


mtcars

?mtcars

############################################### BAR CHARTS ##########################################################

##ggplot() - select the data to display basically what the x and y axis will be displaying
## then we use geom_bar - tell R we want to display the data as a bar chart and fill it with all the relevant 
## labs - text information about the graph we made (Modify axis, legend, and plot labels)

?ggplot
?labs
# Bar chart of cars by number of cylinders using ggplot
ggplot(mtcars, aes(x = factor(cyl))) + # ggplot with the desired data
  geom_bar(fill='lightgreen',colour='black') + # Specifying a bar chart
  labs(x="Number of cylinders", y="Frequency") # Axes labels



################################################ PIE CHARTS #########################################################

##to create a pie chart we use the same basis as the bar chart but we add an extra option to make it a pie chart

##coord_polar - transforms a bar chart into a pie chart by giving it a polar coordinate whey they all stack/merge

?coord_polar

# Pie chart of cars by number of cylinders using ggplot
ggplot(mtcars, aes(x = factor(1), fill=factor(cyl))) + # ggplot with the desired data
  geom_bar(width = 1) + # A bar chart
  coord_polar(theta = "y") + # Specifying a pie chart
  labs(x="",y="",fill='Number of cylinders') # Blank Axes labels



################################################ Histogram #########################################################

##histograms are used to display frequencies of quantitative variables


##geom_histogram - displays the data in as a scatter plot

# Histogram of fuel consumption using ggplot
ggplot(mtcars, aes(x=mpg)) + # ggplot with the desired data
  geom_histogram(binwidth=5, fill='lightgreen',colour='black') + # Specifying bar chart
  labs(x="Fuel consumption (in mpg)", y="Frequency") # Axes labels


################################################ BOX PLOTS #########################################################

##box plot can be used to display both median and variability in data. the median is the line drawn inside the box 
## and the box extends to the first and third quartile with any data outside this range(box) being displayed in dots

##geom_boxplot - displays the data inserted via ggplot into a boxplot
?geom_boxplot

# Boxplot of fuel consumption using ggplot
ggplot(mtcars, aes(x=factor(cyl),y=mpg)) + # ggplot with the desired data
  geom_boxplot(fill='lightgreen',colour='black') + # Specifying boxplot
  labs(x="Number of cylinders",y="Fuel consumption (in mpg)") # Axes labels


################################################ VIOLIN PLOTS ######################################################

##for when we want to incorporate more information about the distribution of the subsets of data

?geom_violin
##geom_violin - a violin plot is a display of a continuous distribution 
## (it is a mix of geom_boxplot and geom_density)

# Violin plot of fuel consumption using ggplot
ggplot(mtcars, aes(x=factor(cyl),y=mpg)) + # ggplot with the desired data
  geom_violin(fill='lightgreen',colour='black') + # Specifying boxplot
  labs(x="Number of cylinders",y="Fuel consumption (in mpg)") # Axes labels


################################################ SCATTER PLOTS ######################################################

##scatter plots are used to display a pair of values of 2 quantitative variables
## what we are interested to see is the correlation between the 2 variables often to test correlation or
## association of the variables

?geom_point
## creates a scatterplot (all dots) that is mostly used to display relationships between 2 continuous variables

# Scatter plot of cars weight by fuel consumption using ggplot
ggplot(data = mtcars, aes(x=wt,y=mpg)) + # ggplot with the desired data
  geom_point(colour='red') + # Specifying a scatter plot
  labs(x="Weight", y="Fuel consumption (in mpg)") # Axes labels



################################################ PLOT COSTUMIZATION #################################################


##Adding colour allows you to a a new value comparison of a property that wasn't defined on the xy axis


# Scatter plot of cars weight by fuel consumption using ggplot
ggplot(data = mtcars, aes(x=wt,y=mpg,colour=factor(cyl))) +
  # ggplot with the desired data
  geom_point() + # Specifying that we want it to be a scatter plot
  labs(x="Weight", y="Fuel consumption (in mpg)",colour='Number of cylinders') # Axes labels



##As an alternative to colours we can also use different symbols instead of the dots to represent another property
## not defined on the xy axis

#Scatter plot of cars weight by fuel consumption using ggplot
ggplot(data = mtcars, aes(x=wt,y=mpg,shape=factor(cyl))) +
  # ggplot with the desired data
  geom_point(aes(x=wt,y=mpg)) + # Specifying that we want it to be a scatter plot
  labs(x="Weight", y="Fuel consumption (in mpg)",shape='Number of cylinders') # Axes labels


##point size and transparency - We can also alter them which is especially useful for when we have overlapping
## points due to their lower opacity 
##transparency = 0 => fully transparent, transparency = 1 => fully opaque

# Scatter plot of cars weight by fuel consumption using ggplot
ggplot(data = mtcars, aes(x=wt,y=mpg,shape=factor(cyl))) +
  # ggplot with the desired data
  geom_point(aes(x=wt,y=mpg),cex=10,alpha=0.3) + # Specifying that we want it to be a scatter plot
                                                # increasing the point size so that can we can see the overlap 
  labs(x="Weight", y="Fuel consumption (in mpg)",shape='Number of cylinders') # Axes labels



## Trend lines - we can already see there is a relationship between fuel consumption and weight 
## using the function geom_smooth we can create an indicator of the linear relationship between x and y 

# Scatter plot of cars weight by fuel consumption using ggplot
ggplot(data = mtcars, aes(x=wt,y=mpg,colour=factor(cyl))) +
  # ggplot with the desired data
  geom_point(aes(x=wt,y=mpg)) + # Specifying that we want it to be a scatter plot
  geom_smooth(method="lm") + # Indicating we want to add a linear trend to the plot
  labs(x="Weight", y="Fuel consumption (in mpg)",shape='Number of cylinders') # Axes labels

##Facetting - when we cannot identify partners or relationships on the entire data set
## it is useful for trying to find these paterns by separating groups in different panels

##NOTE! - this cannot be done using the basic R graphics but we can achieve this using the ggplot2 lib


# Scatter plot of cars weight by fuel consumption using ggplot
ggplot(data = mtcars, aes(x=wt,y=mpg)) + # ggplot with the desired data
  geom_point(aes(x=wt,y=mpg)) + # Specifying that we want it to be a scatter plot
  labs(x="Weight", y="Fuel consumption (in mpg)") + # Axes labels
  facet_grid(. ~ cyl) # Facet split by columns


################################################ LINE PLOTS ######################################################

economics

?economics

##Lines plots - are used to show values of 1 or more variables over the measured time connected by a line.


#seeing unemployed people
# Line plot of unemployment using ggplot2
ggplot(data=economics, aes(x=date,y=uempmed)) + # ggplot with the desired data
  geom_line(colour='red') + # Specifying a bar chart
  labs(x='Date',y='Number unemployed (in 1000s)') # Axes labels

## exe 1

iris


ggplot(data=iris, aes(x=Sepal.Length,y=Sepal.Width)) +
  geom_point(colour='black') + # Specifying a scatter plot
  geom_smooth(method="lm") + # creates de "correlation" ## worst correlation ever
  labs(x="Sepal Length", y="Sepal Width") # Axes labels

##ex2

ggplot(data=iris, aes(x=Sepal.Length,y=Sepal.Width)) +
  geom_point(colour='black') + # Specifying a scatter plot
  geom_smooth(method="lm") + # creates de "correlation" ## worst correlation ever
   # Axes labels
  xlab('S width')+
  ylab('S Length')+
  ggtitle('good title')

?labs

##ex 3

install.packages('wesanderson')

library(wesanderson)

iris

##check the data structure of all the parameters of the data structure
str(iris)
##we have to check if the parameter we want to use to differentiate species in aesthetics is a vector with
## multiple levels


ggplot(data=iris, aes(x=Sepal.Length,y=Sepal.Width)) +
  geom_point(aes(color = Species)) + # Specifying a scatter plot
  scale_color_manual(values=c("#999999", "#E69F00", "#56B4E9")) + 
  geom_smooth(method="lm") + # creates de "correlation" ## worst correlation ever
  labs(xlab, ylab,ggtitle ) + # Axes labels
  facet_grid(. ~ Species) # Facet split by columns
  
?geom_point
?facet_grid

#ex 4 

install.packages("GGally")

library(GGally)



ggplot(data=iris, aes(x=Sepal.Length,y=Sepal.Width)) +
  geom_point(aes(color = Species)) + # Specifying a scatter plot
  scale_color_manual(values=c("#999999", "#E69F00", "#56B4E9")) + 
  geom_smooth(method="lm") + # creates de "correlation" ## worst correlation ever
  labs(xlab, ylab,ggtitle ) + # Axes labels
  facet_grid(. ~ Species) # Facet split by columns


?ggpairs

ggpairs(
  
  data = iris,
  mapping = aes(colour = Species),
  columns = c(1:4)

  
)

## iris[,1:4] - would only load the first to forth collums





