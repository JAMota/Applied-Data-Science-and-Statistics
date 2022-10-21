## lme4 - A tool that implements hierarchical modelling.
## lmerTest - A library that implements significance testing for lmer
## tidyverse - A library that implements tidyverse functions
## readxl - A library allows importing of excel data
## magrittr - A library for piping
## sjPlot - A library for plotting hierarchical model output
## sjmisc - A library of miscellaneous functions for hierarchical models
## sjstats - A library with an icc function
## arm - A library with a function to extract standard errors from lmer

install.packages('lme4')
install.packages('lmerTest')
install.packages('readxl')
install.packages('magrittr')
install.packages('sjPlot')
install.packages('sjmisc')
install.packages('sjstats')
install.packages('arm')
install.packages('glmmTMB')

library(lme4)
library(lmerTest)
library(readxl)
library(magrittr)
library(sjPlot)
library(sjmisc)
library(sjstats)
library(arm)
library(tidyverse)
library(glmmTMB)

jsp = read_xls('C:/AppliedDataScienceAndStatistics/Applied-Data-Science-and-Statistics/Term1/WorkingWithData/week4/jsp-728.xls')

jsp

junirSchoolData = rename(jsp,mathsYear3= 'math yr 3',
                         mathsYear1 = 'math yr 1',
                         isBoy = 'Gender: boy=1',
                         socialClassManual= 'Social class: manual=1',
                         schoolID = 'School ID',
                         normScoreYear3 = 'Normal score yr 3',
                         normScoreYear1 = 'Normal score yr 1'
                         )

junirSchoolData

##As we can see all the columns are treated as numerical as seen by the <dbl> above the numers but schoolId,
## isBoy and socialClassManual don't make as numerical 

str(junirSchoolData)

juniorSchoolLm = lm(mathsYear3~mathsYear1,data=junirSchoolData)

summary(juniorSchoolLm)
##Residuals:
##Min       1Q   Median       3Q      Max 
##-17.4869  -2.2951   0.3673   2.9147  15.0093 
## we have underestimated someone by -17 (min) and +15 (max)
## on average we deviate from the correlation expectation by 3 (1Q and 3Q)

##Coefficients:
##Estimate Std. Error t value Pr(>|t|)    
##(Intercept) 13.84487    0.69171   20.02   <2e-16 ***
##  mathsYear1   0.64962    0.02572   25.26   <2e-16 ***
## the P value of the null hipotises is very small
##(the null hipothesis is it having no correlation between year 1 and 3)

ggplot(data=junirSchoolData,aes(x=mathsYear1,y=mathsYear3)) +
  geom_point() +
  stat_smooth(method = "lm", col = "red") +
  xlab("Maths score in Year 1") +
  ylab("Maths Score in Year 3") +
  ggtitle("Relationship between maths scores in years 1 and 3")


##Ignoring hierarchy we can see that mathsYear1 is a strong predictor of mathsYear3
junirSchoolData <- mutate(junirSchoolData,isBoy = as.factor(isBoy),
                 socialClassManual= as.factor(socialClassManual),
                 schoolID = as.factor(schoolID)
)

jspFElm <- lm(mathsYear3~mathsYear1 + schoolID + mathsYear1*schoolID,data=junirSchoolData)
summary(jspFElm)

## fixed effect model where we allow each school to have it’s own intercept and slope
## this allows each school to have vertical school and using different intercept and different slopes
## the standard error increases because we are less certain with more slopes bu the coefficient stays the same


ggplot(data=junirSchoolData,aes(x=mathsYear1,y=mathsYear3,col=schoolID)) +
  geom_point() +
  stat_smooth(method = "lm", aes(col = schoolID),alpha=0.15) +
  xlab("Maths score in Year 1") +
  ylab("Maths Score in Year 3") +
  ggtitle("Relationship between maths scores in years 1 and 3")

junirSchoolData$schoolID

str(junirSchoolData)


########################################Hierarchical modelling ##################################################


## allow schoolId to create interceptions and raise or lower the y axis more on his own
## it can be observed in the fixed effects how much the year 1 and schoolid influenced the maths in year 3 values
juniorschoollmer1 <- lmer(mathsYear3~mathsYear1 + (1|schoolID) ,data=junirSchoolData)
summary(juniorschoollmer1)

#Fixed effects for the lm model
juniorSchoolLm %>% coef() %>% round(5)

#Fixed effect standard errors for the lm model
juniorSchoolLm %>% se.coef() %>% round(5)

#Fixed effects for the lmer model
juniorschoollmer1 %>% fixef() %>% round(5)


#Fixed effect standard errors : extract2 extracts elements of a list
#and unlists them for the lmer model
juniorschoollmer1 %>% se.coef() %>% extract2(1) %>% round(5)


## VarCorr - extracts variance and correlation components
?VarCorr
juniorschoolLmer1vc = VarCorr(juniorschoollmer1)
print(juniorschoolLmer1vc,comp="Variance")

#the variance attributed to the intercept is much smaller than the residual error
#ICC - Intraclass Correlation Coefficient
3.2887/(3.2887+19.8053)

performance::icc(juniorschoollmer1) #same as above

## this means that roughly 14% of the difference in maths from year 1 to year 3 is associated to the school


juniorschoolLmerdiag = data.frame(Residuals=resid(juniorschoollmer1),
                          schoolID=junirSchoolData$schoolID,
                          Fitted= fitted(juniorschoollmer1))


ggplot(data=juniorschoolLmerdiag, aes(x=Fitted,y=Residuals,col=schoolID)) +
  geom_point() +
  facet_wrap(~schoolID) +
  ggtitle("Lowest level residuals facetting by school")

plot_model(juniorschoollmer1, type = "re") #Plotting random effects

##Here we are looking at the performance of the model. We would like to see that the school random effects
## are randomly scattered about 0 (they are here), and that there are no major outliers.

install.packages('effects')
library(effects)

#Marginal effects
plot_model(juniorschoollmer1, type = "eff", terms = "mathsYear1") +
  geom_point(aes(x=mathsYear1,y=mathsYear3),data=junirSchoolData)

##The marginal plot lets us see the overall association between year 1 maths scores and year 3 maths scores
## when we have dealt with the clustering through random intercepts.

################################################### RANDO SLOPES ##################################################

##We can further allow the slopes of the relationship between maths scores for each school to be drawn from
## a distribution of possible slopes


juniorSchoolLmer2 <- lmer(mathsYear3~mathsYear1 + (1+ mathsYear1|schoolID) ,data=junirSchoolData)
summary(juniorSchoolLmer2)

## This gives a convergence warning which we can suppress by specifying the optimizer to be used

juniorSchoolLmer2 <- lmer(mathsYear3~mathsYear1 + (1+ mathsYear1|schoolID) ,data=junirSchoolData,
                 control = lmerControl(optimizer ="Nelder_Mead"))
summary(juniorSchoolLmer2)

##The code below plots predictions from the model without using the sjPlot library (in case there is difficulty
## loading it). Note at the end we use ‘ggthemes’ to change how the plot looks. There are many theme options
## available. Have a look at some of the others

library(ggthemes)



junirSchoolData$juniorSchoolLmer.predictions <- predict(juniorSchoolLmer2)

ggplot(aes(x = mathsYear1, y = juniorSchoolLmer.predictions,
           color = schoolID), data = junirSchoolData) +
  geom_line(size=.3) +
  geom_point(aes(y = mathsYear3)) +
  xlab("Year 1 Maths Score") +
  ylab("Year 3 Maths score") +
  ggthemes::theme_tufte()


## We can explore the lowest level residuals, the random effects and the marginal effects as before.

juniorSchoolLmer2diag <- data.frame(Residuals=resid(juniorSchoolLmer2),
                           schoolID=junirSchoolData$schoolID,
                           Fitted= fitted(juniorSchoolLmer2))


ggplot(data=juniorSchoolLmer2diag, aes(x=Fitted,y=Residuals,col=schoolID)) +
  geom_point() +
  facet_wrap(~schoolID) +
  ggtitle("Lowest level residuals by school")










