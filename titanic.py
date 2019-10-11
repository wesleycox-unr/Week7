#titanic.py
import pandas as pd

df = pd.read_csv("train.csv")

#print(df.head(10))

#print(df.tail(10))

#print("Shape: {}".format(df.shape))

#print(df.info())

#print(df.describe())

#print(df.loc[0,["Name","Sex"]])

#print(df.iloc[0,3])

#print(df[df["Age"] > 30].describe())

#print(df.sort_values(["Age","Name"], ascending=[True, False]).loc[:,["Name","Age"]])

df = df[~df["Name"].str.contains("Owen")]
