import pandas as pd
import numpy as np


def predict(a,b,c,d,e,f,g,h):

   data=pd.read_csv("CardioGoodFitness.csv")
  
   # import labelencoder
   from sklearn.preprocessing import LabelEncoder
   # instantiate labelencoder object
   le = LabelEncoder()
   categorical_feature_mask = data.dtypes==object
   # filter categorical columns using mask and turn it into a list
   categorical_cols = data.columns[categorical_feature_mask].tolist()
   data[categorical_cols] = data[categorical_cols].apply(lambda col: le.fit_transform(col))


   X = data.drop('Product',axis=1)
   y = data['Product']

   
   
   from sklearn.linear_model import LinearRegression
   regressor=LinearRegression()
   
   
  
   regressor.fit(X,y)
   
  
   
   y_pred=regressor.predict([[a,b,c,d,e,f,g,h]])
   print(int(y_pred))
   return y_pred






