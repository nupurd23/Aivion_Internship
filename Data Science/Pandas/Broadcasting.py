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
df["Salary"] = df["Salary"] + 5000

print(df["Salary"])

#Renaming Columns

df.rename(columns = {"Department " : "Dept"} , inplace =True)

print(df["Department"].unique())