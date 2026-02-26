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
#print(df)
#print(df.head(2))
#print(df.tail(3))

# loc and iloc
#print(df.iloc[1:3])

#print(df.loc[1:3 , ["Age" , "Department"]])

#DROP ANY COLUMN FROM DATAFRAME
#print(df.drop("Age" , axis =1))
#print(df) 

#print(df.shape)
#print(df.info())

print(df.describe())