import pandas as pd
import quandl 
import math
import numpy as np
from sklearn import preprocessing, cross_validation,svm
from sklearn.

df = quandl.get('WIKI/GOOGL')
df= df[['Adj. High','Adj. Low','Adj. Open','Adj. Close','Adj. Volume']]
df['HL. PCT']= ((df['Adj. High']-df['Adj. Low'])/df['Adj. Low'])*100
df['OC. PCT']= ((df['Adj. Open']-df['Adj. Close'])/df['Adj. Close'])*100
df= df[['Adj. Close','HL. PCT','OC. PCT','Adj. Volume']]

forcast_col ='Adj. Close'
df.fillna(-99999,inplace=True) #to fill na blocks


forcast_out = int(math.ceil(0.01*len(df))) #used to shift lable col by 1%into future
df['label'] = df[forcast_col].shift(-forcast_out) #creates new col with forcasr_col shifted by 1% into  future
df.dropna(inplace=True) #drops all rows with na in it 

print(df.head()) #prints only head of data
