# import necessary libraries
import numpy as np
import pandas as pd

# loading the dataset
# df = pd.read_csv('Employee.csv')
df = pd.read_csv('Indian Employee dataset/Employee.csv')
print(df.head())

print('Missing Values in each column')
print(df.isnull().sum())