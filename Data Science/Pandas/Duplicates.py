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

df_dup= df[df.duplicated(keep = "first")]
print(df_dup)

df = df.drop_duplicates()
print(df)

#LAMBDA FUNCTION
df["Salary"] = df["Salary"].apply(lambda x : x/10 if x>50000 else x)
print(df)