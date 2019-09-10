### Data Science Fundamentals

import pandas as pd

df = pd.read_csv('..\\Git Clones\\python_pandas\\sample_data\\02 Introduction to Pandas\\intel.csv')
print(type(df))
# print(df.columns)
open = df['Open']
close = df['Close']

print(df[['Open', 'Close']].head())
