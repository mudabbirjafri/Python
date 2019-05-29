import matplotlib.pyplot as plt
%matplotlib inline
import random
import numpy as np
import pandas as pd
from sklearn import datasets, svm, tree, preprocessing, metrics
import sklearn.ensemble as ske
import os
import datetime

os.chdir('C:/Users/adhillon/OneDrive - NVIDIA Corporation/AnacondaProjects/OPS 808/Dataset/')
nyc_data = pd.read_csv('nyc-rolling-sales.csv')

# examine the dataset
nyc_data.dtypes
nyc_data.shape
nyc_data.isna().sum()
nyc_data.groupby(['TAX CLASS AT PRESENT']).count().iloc[:,:1]/len(nyc_data)
nyc_data.groupby(['BOROUGH']).count().iloc[:,:1]/len(nyc_data)

nyc_data.head()

# preprocessing
nyc_data['SALE DATE'] = pd.to_datetime(nyc_data["SALE DATE"])
nyc_data = nyc_data.replace(to_replace=' -  ', value ='0')
nyc_data['SALE PRICE'] = nyc_data['SALE PRICE'].astype('int64')
nyc_data['BUILDING CLASS AT TIME OF SALE']=pd.Categorical(nyc_data['BUILDING CLASS AT TIME OF SALE']).codes
nyc_data['BUILDING CLASS AT TIME OF SALE']=nyc_data['BUILDING CLASS AT TIME OF SALE'].astype('category').cat.codes


nyc_data.drop(['EASE-MENT', 'APARTMENT NUMBER'], axis=1, inplace=True) #Remove Empty columns
nyc_data =nyc_data.loc[:, ~nyc_data.columns.str.contains('^Unnamed')]


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
