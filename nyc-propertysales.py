import matplotlib.pyplot as plt
%matplotlib inline
import random
import numpy as np
import pandas as pd
from sklearn import datasets, svm, tree, preprocessing, metrics
import sklearn.ensemble as ske
import os

os.chdir('C:/Users/Mudabbir/Desktop/Spring Quarter/Machine Learning 808/nyc-property-sales')
nyc_data = pd.read_csv('nyc-rolling-sales.csv') #Lead the data
#Remove Empty colums
nyc_data.drop(['EASE-MENT', 'APARTMENT NUMBER'], axis=1, inplace=True)
nyc_data =nyc_data.loc[:, ~nyc_data.columns.str.contains('^Unnamed')]
#Drop Nans
nyc_data.dropna().head(2)
#Replace - in Sale price with NAN
nyc_data['SALE PRICE']=nyc_data['SALE PRICE'].replace(' -  ', np.NaN)
nyc_data.head(5)


#Use LabelEncoder to convert labels into binary codes
from sklearn.preprocessing import LabelEncoder

LE = LabelEncoder()
nyc_data['NEIGHBORHOOD'] = LE.fit_transform(nyc_data['NEIGHBORHOOD'])
nyc_data['BUILDING CLASS CATEGORY'] = LE.fit_transform(nyc_data['BUILDING CLASS CATEGORY'])
nyc_data['BUILDING CLASS AT PRESENT'] = LE.fit_transform(nyc_data['BUILDING CLASS AT PRESENT'])
nyc_data['TAX CLASS AT PRESENT'] = LE.fit_transform(nyc_data['TAX CLASS AT PRESENT'])
nyc_data['BUILDING CLASS AT TIME OF SALE'] = LE.fit_transform(nyc_data['BUILDING CLASS AT TIME OF SALE'])
nyc_data['ADDRESS'] = LE.fit_transform(nyc_data['ADDRESS'])
nyc_data['SALE PRICE'] = nyc_data['SALE PRICE'].astype(str)

nyc_data.fillna(nyc_data.mean(), inplace=True)


Avg_price = nyc_data.groupby(['TAX CLASS AT PRESENT', 'YEAR BUILT'])['SALE PRICE']['SALES PRICE'].mean()
Avg_price.head()
