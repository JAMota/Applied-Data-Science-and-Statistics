install.packages('haven')

library(haven)
library(tidyverse)

#dataFromSpss = read_spss('C:/Users/AndreMota/Downloads/OneDrive_1_21-10-2022/SPSS/UKDA-8971-spss/spss/spss25/dcms_csbs_combined_2016-2022_banded_cost_data_only_v3_public.sav')
#
#dataFromSpss
#
#dataFromStata = read_stata('C:/Users/AndreMota/Downloads/OneDrive_1_21-10-2022/STATA/UKDA-8971-stata/stata/stata13/dcms_csbs_combined_2016-2022_banded_cost_data_only_v3_public.dta')
#
#dataFromStata
#
#dataFromEzData = read_csv('C:/Users/AndreMota/Downloads/archive/Cyber Security Breaches.csv')
#
#dataFromEzData

technicalAnnex2018 = 'https://doc.ukdataservice.ac.uk/doc/8406/mrdoc/pdf/8406_cyber_security_breaches_survey_2018_technical_annex.pdf'
## will be used in comments to refer to pages to look for info

dataCyberSecuritySurvey2018 = read_spss('C:/AppliedDataScienceAndStatistics/Applied-Data-Science-and-Statistics/Term1/WorkingWithData/Assignment1/Cyber Security Breaches Survey, 2018/UKDA-8406-spss-CyberSurvey2018/spss/spss24/17-054294-01_csbs_2018_final_data_deidentified_v1_12042018_public.sav')

dataCyberSecuritySurvey2018$year = '2018'

str(dataCyberSecuritySurvey2018)

head(dataCyberSecuritySurvey2018)

colnames(dataCyberSecuritySurvey2018)

##renaming all the bloody variables to a more java like name

dataCyberSecuritySurvey2018TidyName <- rename(dataCyberSecuritySurvey2018,isBusiness= 'samptype')

## terrible boolean pratice but if isBusiness is 1 it is a business if it is 2 it is a charity

dataCyberSecuritySurvey2018$samptype

## for typex it will be to describe from micro/small to medium and large companies
browseURL(technicalAnnex2018) ## page 26 Q5X.TYPEX

## for the typex variable: SCRIPT TO BASE BUSINESS/CHARITY TEXT SUBSTITUTIONS ON TYPEX (BUSINESS IF
## TYPEX CODES 1–2, ELSE CHARITY // so basically makes it redundant with the samtype/isBusiness? 
##//TODO possibly remove the isBusiness variable
## I assume the -97 is just missing data but in a terrible representation 

## lets go to the variables by question as in the technicalAnnex2018 to reduce messiness and even more headaches

## Question 4 sizea - number of employees/workers











