import pandas as pd
import numpy as np

df =pd.read_csv(r'99laptop.csv')
#print(dataframe.head())
#print(df.columns.tolist())
#print(df['name_c'].head(1))
#print(df['name_c'].iloc[77])

df_raw = df[['name_c', 'price']]
print(df_raw.head())

print(df_raw.columns.tolist())
