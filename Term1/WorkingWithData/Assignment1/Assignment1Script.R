install.packages('haven')

library(haven)
library(tidyverse)

dataFromSpss = read_spss('C:/Users/AndreMota/Downloads/OneDrive_1_21-10-2022/SPSS/UKDA-8971-spss/spss/spss25/dcms_csbs_combined_2016-2022_banded_cost_data_only_v3_public.sav')

dataFromSpss

dataFromStata = read_stata('C:/Users/AndreMota/Downloads/OneDrive_1_21-10-2022/STATA/UKDA-8971-stata/stata/stata13/dcms_csbs_combined_2016-2022_banded_cost_data_only_v3_public.dta')

dataFromStata

dataFromEzData = read_csv('C:/Users/AndreMota/Downloads/archive/Cyber Security Breaches.csv')

dataFromEzData
