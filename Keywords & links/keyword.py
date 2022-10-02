# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 10:33:20 2022

@author: eliz
"""

"""
1. Read the excel file and create Pandas DataFrame.
2. List all the queries which has the word HTML in it.
3. Find out the total number of clicks for the queries having the word HTML  
4. Find out the query which has generated maximum number of Clicks having the word html
5. Find out the shortest query having the word html
6. Find out the longest query having the word html
"""

import pandas as pd
df=pd.read_excel('kw1_short.xlsx')     #1. Read the excel file and create Pandas DataFrame.     
df.columns

# 2. List all the queries which has the word HTML in it.
result=df[df.Query.str.contains('HTML',case=False)]
print(result)

# 3. Find out the total number of clicks for the queries having the word HTML  
print(result.Clicks.sum())

# 4. Find out the query which has generated maximum number of Clicks having the word html
print(result.Clicks.max())


result=result[result.Query.str.len().min()]

# 5. Find out the shortest query having the word html
print(result[result['Query'].str.len()==result['Query'].str.len().min()])

# 6. Find out the longest query having the word html
print(result['Query'].str.len().max())
print(result[result['Query'].str.len()==result['Query'].str.len().max()])




import pandas as pd
my_data=pd.read_excel('links_external.xlsx')
print(my_data.shape)
print(my_data.columns)

# What is the current year?
current_year=pd.to_datetime('now').year
print(current_year)

# number of records in current year
my_data['Lastcrawled']=pd.to_datetime(my_data['Lastcrawled'])
df=my_data[my_data['Lastcrawled'].dt.year==current_year]
print("Number of records in the current year : ",len(df))

# number of records in previous year

df=my_data[my_data['Lastcrawled'].dt.year==current_year-1]
print("Number of records in the current year : ",len(df))

# number of records in the year 2020
df=my_data[my_data['Lastcrawled'].dt.year==current_year-2]
print("Number of records in the current year : ",len(df))

# Display the year and the number of records in that year
# groupby() 
my_data=pd.read_excel('links_external.xlsx')
my_data['Lastcrawled']=pd.to_datetime(my_data['Lastcrawled'])
print(my_data.groupby(my_data['Lastcrawled'].dt.year).count())


# Display the month and the number of records in that month
# groupby() 
my_data=pd.read_excel('links_external.xlsx')
my_data['Lastcrawled']=pd.to_datetime(my_data['Lastcrawled'])
print(my_data.groupby(my_data['Lastcrawled'].dt.month).count())

# Display the year and the month and the number of records in that year grouped by each month
# groupby() 
print(my_data.groupby([my_data['Lastcrawled'].dt.year,my_data['Lastcrawled'].dt.month]).count())



my_data=my_data[my_data['Linkingpage'].str.contains('example3.com')]
print(len(my_data))
print(my_data.groupby(my_data['Lastcrawled'].dt.year).count())

