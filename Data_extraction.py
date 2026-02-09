import pandas as pd
import numpy as np

df =pd.read_csv(r'99laptop.csv')
#print(dataframe.head())
#print(df.columns.tolist())
#print(df['name_c'].head(1))
#print(df['name_c'].iloc[77])

df_raw = df[['name_c', 'price']]
#print(df_raw.head())

#print(df_raw.columns.tolist())
#print(df_raw['name_c'].head())

# Extracting the brand name from the 'name_c' column
df_raw['brand'] = df_raw['name_c'].apply(lambda x: x.split())
print(df_raw['brand'].head())