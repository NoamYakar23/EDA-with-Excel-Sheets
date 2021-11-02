import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.preprocessing as preprop
import numpy as np


file = 'finalizeRegressionData3.xlsx'
xls = pd.read_excel(file)

#check for null values in each row4
print(xls.isnull().sum())

#shape of our data (rows, columns)
print(xls.shape)
print(xls.head())
print(xls.info())

#creating distribution plots for every column within the dataset
for column in xls.columns:
    sns.displot(xls[column], bins = 10, kde = True).set(xlabel = column)
    plt.title(column + " Distribution Plot")
    sns.set_style(style='darkgrid')
    plt.show()



#heatmap showing the correlations of columns with eachother
correlations = xls.corr()
sns.heatmap(correlations, linewidths =.5, cmap="YlGnBu", annot=True)
plt.show()

#we know we are trying to approximate demand for this rideshare service
#y-target variable is the number of weekly riders
#Lets visualizise further the correlations represented in the heatmap

columns = xls.columns

#getting features: every variable besides number of weekly riders --> kind of stupid wiht a list comprehension but ... whateva
features = xls.drop('Number of weekly riders', axis=1)
target_variable = xls['Number of weekly riders']

#graph every feature against the target variable
for feature in features:
    sns.scatterplot(data = xls, x=feature, y=target_variable)
    plt.show()


