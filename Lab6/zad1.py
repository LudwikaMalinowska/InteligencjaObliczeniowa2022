import pandas as pd
import numpy as np

# df = pd.read_csv('iris_with_errors.csv')
# df.head()
missing_values = ["n/a", "na", "-"]
df = pd.read_csv('iris_with_errors.csv', na_values=missing_values)

#a
print(df.isnull().values.any())
print(df.isnull().sum())
print("suma brakujących rekordów:", df.isnull().sum().sum())

#b


median = df['sepal.length'].median()
df['sepal.length'].fillna(median, inplace=True)
df['sepal.length'] = np.where((df['sepal.length'] > 15) | (df['sepal.length'] < 0),
                              median, df['sepal.length'])


median = df['sepal.width'].median()
df['sepal.width'].fillna(median, inplace=True)
df['sepal.width'] = np.where((df['sepal.width'] > 15) | (df['sepal.width'] < 0),
                              median, df['sepal.width'])

median = df['petal.length'].median()
df['petal.length'].fillna(median, inplace=True)
# df['petal.length'] = np.where(not df['petal.length'].between(0,15),
#                               median, df['petal.length'])
df['petal.length'] = np.where((df['petal.length'] > 15) | (df['petal.length'] < 0),
                              median, df['petal.length'])


median = df['petal.width'].median()
df['petal.width'].fillna(median, inplace=True)
df['petal.width'] = np.where((df['petal.width'] > 15) | (df['petal.width'] < 0),
                              median, df['petal.width'])

print(df.isnull().values.any())
print(df.isnull().sum())
print("suma brakujących rekordów:", df.isnull().sum().sum())
print(df[-15:])


#c
df["variety"] = df["variety"].str.lower()
df["variety"] = np.where((df["variety"].str.startswith("set")),
                              "setosa", df["variety"])
df["variety"] = np.where((df["variety"].str.startswith("versi")),
                              "versicolor", df["variety"])
df["variety"] = np.where((df["variety"].str.startswith("virgi")),
                              "virginica", df["variety"])

# print(df[-15:])