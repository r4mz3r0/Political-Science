
# coding: utf-8

# In[1]:


cd C:\Users\Ramiro Gonzalez\Desktop\POLI127DATA\json files


# # POLI 127 Data Analyst Role 
# ## Ramiro Gonzalez and Melissa Becerra

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
import json
from IPython.display import Image
import math
from pandas import DataFrame as df
from scipy.stats import trim_mean, kurtosis
from scipy.stats.mstats import mode, gmean, hmean
from scipy import interpolate


# # METADATA 
# 
# # Link 
# https://github.com/impracticaldev/Political-Science/tree/master/POLI127/Projects/Data-Analyst-Role 
# ## Curated data
# <span style="color:red">Independent Variable 1</span>: Income_same_sex_couple to be determined. <br>
# <span style="color:red">Independent Variable 2</span> (NOTE: This may be used as variable): Same_sex_couple_who_are_same_sex_spouses_for_years_2005_2016 was original in percentage, it was converted to quantity by using $FLOOR((x,y)\cdot(x_2,y_2))$ <br>
# <span style="color:red">Independent Variable 3</span>Total_same_sex_couple_year_2005_201 <br>
# <span style="color:red">Independent Variable 4</span>:Total_adoption_by_each_state. Interpolation may be neccessary since Independent variable 1,2, and 3, are of the following years: 2005 - 2016. Variable 4 consist of the following years: 1990,2000,2001,2005,2007,2008,2009,2010,2011,2012 <br> 
# Linear Interpolation $y  = y_1 + \frac{y_2 - y_1}{x_2 - x_1}(x -x_1) $ <br>
# <span style="color:red">Dependent Variable </span> The rate of adoption. May be theoretically computed for missing years using interpolation for independent variable 4. <br> 
# ## Miscellaneous
# Total number of same sex households
# # Documentation
# 

# ## Three Casual Models
# 

# In[3]:


Image(filename="img/CasualModel1.png",width=400,height=500)


# Having a spouse increases the chance of adoption.Income may be the hidden factor that causes this relationship since both partners may be bringing home income. (Income is the mediating variable)

# In[4]:


Image(filename="img/CasualModel2.jpg",width=400,height=500)


# Same sex spouses adopt at a higher rate, but the only way to be spouse it must be established by law, which means marriage must be legal in the state one resides to be considered a "spouse".

# In[5]:


Image(filename="img/CasualModel3.jpg",width=400,height=500)


# The adoption rate, variable y (independent variable) requires that x be same sex couple as they fit the definition of LGBTQ. Total same sex couple has a direct relationship on adoption rate, in that more same sex couple, there are higher or lower rate.

# ## Read In Data
# Saving the the data above in seperate variable. Possible variable names are as follow
# independentOne, independentTwo, independent3, independent4
#  

# In[6]:


#Using json files, option one, csv converted to json
pathvar1 = "Income_same_sex_couple.json"
samesexhouseholds = "samesexhouseholds.json"
pathvar2 = "Same_sex_couple_who_are_same_sex_spouses_for_years_2005_2016.json"
pathvar3 = "Total_same_sex_couple_year_2005_2016.json"
pathvar4 = "Total_adoption_by_each_state.json"


# In[7]:


cd C:\Users\Ramiro Gonzalez\Desktop\POLI127DATA\csv


# In[8]:


#income was originally in percentage
#importing to csv, analysis may be easier this way. 
pathvar1csv = "Income_same_sex_couple.csv"
sameSexHouseholdsTcsv = "samesexhouseholdsT.csv"
sameSexHouseholdscsv = "samesexhouseholds.csv"
pathVar2csv = "Same_sex_couple_who_are_same_sex_spouses_for_years_2005_2016.csv"
pathVar3csv = "Total_same_sex_couple_year_2005_2016.csv"
pathVar4csv = "Total_adoption_by_each_state.csv"


# In[9]:


income_couples = pd.read_csv(pathvar1csv) #DONE
same_sex_householdT = pd.read_csv(sameSexHouseholdsTcsv) #DONE
same_sex_household = pd.read_csv(sameSexHouseholdscsv) #DONE
same_sex_spouses = pd.read_csv(pathVar2csv) #DONE
total_same_sex_couple = pd.read_csv(pathVar3csv)
total_pop_each_state = pd.read_csv(pathVar4csv)


# In[10]:


income_couples.head()


# In[11]:


same_sex_spouses.head()


# In[12]:


total_same_sex_couple.head()


# In[13]:


total_pop_each_state.head()
#this will be a poblem in our anaysis, 1990 - 2012, use interpolation and reorder


# ## Obtain Summary/Descriptive Statistics

# ## Independent Variable 1
# Income of same sex couples. 
# 

# The following will be calculated for mean, sd, var, min, max, median, range, and quantile.
# In my analysis of variable 1 (Income_same_sex_couples) I want to find the mean, this will show the relative income bracket smae sex couple fall into. 
# The above "Income" bracket is of importance here. 

# In[14]:


#find the mean, for each year 
#mean, sd, var, min, max, median, range, and quantile.
stdDevEachYear,minEachYear,meanEachYear,maxEachYear,rangeEachYear = ({} for i in range(5))
for i in range(5,17):
    meanEachYear[("mean{}".format(i + 2000))] = income_couples['{}'.format(i + 2000)].mean()
    stdDevEachYear[("stdDev{}".format(i + 2000))] = income_couples['{}'.format(i + 2000)].std()
    minEachYear[("min{}".format(i + 2000))] = income_couples['{}'.format(i + 2000)].min()
    maxEachYear[("max{}".format(i + 2000))] = income_couples['{}'.format(i + 2000)].max()
print("#The mean, so called average.")
print(meanEachYear)  
print("#The standard deviation.")
print(stdDevEachYear) #The standard deviation
print("#The min and max.")
print(minEachYear)
print(maxEachYear)
print("#Range is max - min.")
for i in range(5,17):
    rangeEachYear[("range{}".format(i + 2000))] = maxEachYear[("max{}".format(i + 2000))] - minEachYear[("min{}".format(i + 2000))]
print(rangeEachYear)
income_couples.describe()


# The above data is stored meanEachYear. We may also get the percentage of couples that fall in the mean. 

# In[15]:


meanEachYearPlotted = [] 
for i in range(0,10):
    meanEachYearPlotted.append(meanEachYear["mean{}".format(i + 2005)])
plt.plot(meanEachYearPlotted)
plt.ylabel('Mean 2005 - 2016')
#The graph below goes from 2005 - 2016 , Increment 2005 + xlabel , that is 0 is 2005, 1 is 2006 ... etc
plt.show()


# As one can see from the above graph meanEachYearPlotted around 2009 the average decreased dramatically, and spiked during 2016, around 2007, a recession hit. The mean decreased dramattically. 

# ## Independent variable 2

# We consider the following. The Total Same Sex Couple Households. This are our potential adopters. 

# In[16]:


same_sex_householdT.head()


# In[17]:


#The following describes from 2005-2016
same_sex_householdT.describe()
#The year portion provides very little information. 


# In[18]:


#Plotting the same_sex_household 
plt.plot(same_sex_householdT)
plt.ylabel('Mean 2005 - 2016')
#The graph below goes from 2005 - 2016 , Increment 2005 + xlabel , that is 0 is 2005, 1 is 2006 ... etc
plt.show()


# Within the subset of $\textbf{total households}$ there exists same_sex_spouses. Note that $\textbf{Total households}$ includes same sex couples who are in a partnership or relationship, but also spouses under the law. We are interested in housholds with same sex spouses because they are more likely to adopt, or so our data will show. 

# In[19]:


same_sex_spouses.head()


# For this to work we must remove the states, and knowing that states are in alphabetical order Alabam = 0 .. Wyoming = 50 
# We will transpose the data below, so that we are able to describe it, removing the header manually was not possible. 

# #originally 2010 had a missing value, recall this is same sex couples, to be retrieve from orginial data. There was missing value in orginial data, therefore  interpolation may be neccesary. 
# $f(x) = \sum f_{j} \phi(x -x_j)$
# The mean would be sufficient. 

# In[20]:


#Begin by storing data 
y = [615,441,372,635,179,222,296,475,796,738,952]
mean = []
sumY = 0;
for i in range(0,11):
    sumY = sumY + y[i]
mean = sumY/12;
print(mean)


# In[21]:



total_same_sex_spouse_each_year = {};
for i in range(16,5,-1):
    total_same_sex_spouse_each_year[('total_spouses{}'.format(2000 + i))] = same_sex_spouses['{}'.format(2000 + i)].sum()
print(total_same_sex_spouse_each_year)


# In[22]:


same_sex_spouses.describe()
#The descriptions are specific to entire united states, that is 51 states, for years 2016 - 2005


# If need it be for every state we whould do the following. 

# In[23]:


# we transpose it and calculate the statistics for every state, as follows. 
(same_sex_spouses.T).describe()


# ## Independent Variable 3

# In[24]:


total_same_sex_couple.head()


# In[25]:


total_same_sex_couple.describe()


# ## Independent variable 4

# Total adoption by each state. 

# In[26]:


total_pop_each_state.head()


# In[27]:


(total_pop_each_state['2007']).describe()


# # Analysis of 2007

# In[28]:


path2007 = 'IIIP.csv'


# In[29]:


IIP = pd.read_csv(path2007)


# In[30]:


IIP.head()


# In[31]:


independent1, independent2,independent3 = ([] for i in range(3))
independent1 = IIP['Total Adopted']
independent2 = IIP['Same Sex Spouse']
independent3 = IIP['Same Sex Couple']
dependent = IIP['Adopted Children']


# ## Cross Tabulation

# In[32]:


pd.crosstab(dependent, [independent1, independent2, independent3], rownames=['dependent'], colnames=['independent1', 'independent2','independent3'])


# In[33]:


import matplotlib.pyplot as plt
plt.scatter(independent1, dependent)


# In[34]:


plt.scatter(independent2, dependent)


# In[35]:


plt.scatter(independent3, dependent)


# In[36]:


import numpy as np
#np.correlate(independent1,dependent, "full")


# In[37]:


#np.correlate(independent2,dependent)


# In[49]:


#np.correlate(independent3,dependent)


# In[50]:


import statsmodels.api as sm


# In[51]:


model = sm.OLS(dependent, independent2).fit()
predictions = model.predict(dependent) 
model.summary()

