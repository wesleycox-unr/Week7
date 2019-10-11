#adding.py
import pandas as pd

lst = ["USA","France","Germany","Aus"]

df = pd.DataFrame(lst, columns=["Country"])

#print(df[df["Country"] != "France"])

df2 = pd.DataFrame([[1,2],[3,4]], columns=["A","B"])


df3 = pd.DataFrame([[5,6]],columns=list("AB"))
df2 = df2.append(df3, ignore_index=True)

df4 = pd.DataFrame([[7,8],[9,10]],columns=["A","B"])
df2 = df2.append(df4, ignore_index=True)

print(df2)
