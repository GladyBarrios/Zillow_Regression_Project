# Zillow_Regression_Project

## Project goals 
Goals for this project are to proved insights on th housing market in three area codes in southern california and to find the key drivers of property value for single family properties. 


## Project description 

The main goal for this project is to use Machine learning models to help predict the home values using a home report of 2017 and using single family Residendials.With this project we will wrangle raw zillow data, explore the data, run statistical test, and end it off with predicting home values with our machine learning models. This prediction is important for not only zillow as a company but our future customers and familys who are looking for afordable housing in California. At the end of the presentation We will discover the best model for prediction of housing cost out of all the models tested. 

## Initial Questions 

- Question 1- Is there a relationship with the number of bathrroms a property has and the property value ?

- Question 2 - does a prperty with a certain number of bathrooms cause an increase in property value?

- Question 3- does the number of square feet have a relationship with the county the property is in?

- question 4- does the year the home was built have a relationship with area it is in ?

- Question 5- Is there a relationship with the number of bathrroms a property has and the county the property is in ?



## Data Dictionary 
bathroomcnt- this displays a bathroom count of 1-6

bedroomcnt- this displays a bedroom count of 1-6	

calculatedfinishedsquarefeet- The Number of sqarefeet per property

taxvaluedollarcnt- The cost of the property  

yearbuilt- Year the property was built 

fips- this is the area code the property resides 

County- The name of the county the property is in, three properties include Los Angeles County, Ventura County, Orange County


## Project plan 
Aquiring the data - used the Codeup SQL server to aquire the data 

Planning and preparing the data (data Wrangling)- when hadeling nulls, I did drop them which left me with more than enough data (99%) to continue my project
removed outliers such as Properties with 6+ bathrooms and bedrooms as well as 0 bathrooms and bedrooms
Created a new column that shows the counties the property is in all the counties are in souther California

Exploring the data- Went to my intital questions to see what could be the potential drivers of home prices focused more on bedroom and bathrhrrom considering the time crunch. Used visualizations to determine what could be the potential drivers of home prices. Then ending off with some statistical analysis pin point the relationship. 

Modeling- First I started out by creatig a baseline which is important- when comparing models-
I tried three diffrent models 
- OLS- (Ordiary Least Squares)

- LassoLars 

- GLM- (Generalized Linear Model)

- Polyniomial Model- This model had the lowest RMSE

after running these models on my x_train I was able to compare RMSE to see which model had the lowest. 



## Steps to reproduce 

You will need an env.py file that contains your own hostname, username and password of the mySQL database that contains the zillow_db Store that env file locally in the repository. clone my repo (including the acquire.py and prepare.py) (confirm .gitignore is hiding your env.py file) libraries used are pandas, matplotlib, seaborn, numpy, sklearn. you should be able to run final repo.
