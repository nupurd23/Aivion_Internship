import pandas as pd
import numpy as np

data = {
    "Name" : ["Alice" , "Bob", " Charlie" ,"David" , " Eve","Alice"],
    "Age": [25,30, 35,np.nan,29,25],
    "Department": ["HR","IT","Finance","IT" ,"HR","HR"],
    "Salary": [50000,60000,70000,62000 ,np.nan,50000]
    
}
#print(data)
df =pd.DataFrame(data)
#print(df.isnull().sum())

#print(df.dropna(how = "any"))

#print(df.fillna(0))
#print(df["Age"].fillna(df["Age"].mean()))
#print(df["Salary"].fillna(df["Salary"].median()))
#print(df["Age"].fillna(method = "ffill"))
df["Name"] = df["Name"].replace(" Charlie", "Rose" )
print(df)