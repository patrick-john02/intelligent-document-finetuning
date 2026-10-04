import pandas as pd


data = pd.read_excel("data/raw/classification/Book1.xlsx", sheet_name='COMMUNICATION')

# print(data.describe(include='all'))
print(data.duplicated().sum())