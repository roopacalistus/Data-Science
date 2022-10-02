# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 16:04:27 2022

@author: eliz
"""
# SUV Car Analysis
"""
A Car company has released a new SUV in the market
Using the previous data about the sales of their SUVs they want to predict the 
category of people who might be interested in buying 

*** What factors made people more interested in buying an SUV ?

"""
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data=pd.read_csv('suv_data.csv')
data.head()
data.info()

# Checking for null values
print(data.isnull().sum())
sns.heatmap(data.isnull(),yticklabels=False,cbar=False)

sns.countplot(x="Purchased",data=data)

sns.countplot(x="Purchased",hue="Gender",data=data)

# Analysing agewise
data['Age'].plot.hist()

"""
sex=pd.get_dummies(data['Gender'])
sex.head(5)
sex=pd.get_dummies(data['Gender'],drop_first=True)
sex.head()

data=pd.concat([data,sex],axis=1)
data.drop(['Gender'],axis=1,inplace=True)

data.head()

cols=['Age',
      'EstimatedSalary']

      
x=data[cols]

y=data['Purchased']

"""
x=data.iloc[:,[2,3]].values

y=data.iloc[:,4].values


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=30,random_state=0)

logmodel=LogisticRegression()
logmodel.fit(x_train,y_train)
predictions=logmodel.predict(x_test)
accuracy_score(y_test,predictions)

"""
# How my model is performing using the classifications Report
from sklearn.metrics import classification_report
classification_report(y_test,predictions)
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,predictions)
"""