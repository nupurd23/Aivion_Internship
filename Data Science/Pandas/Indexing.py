import pandas as pd

s= pd.Series([1,2,3,4,5])

print(s[0])
print(s[0:2])#start(included) : stop(excluded) : step value (values to jump)

#iloc -> location based indexing

print(s.iloc[3])

print(s.iloc[[1,2,4]])

s.name = "calories"

index = ["apple", "banana" , "grapes" ,"orange","kiwi"]

s.index = index
print(s)

#loc -> label based indexing
print(s.loc['grapes'])
# In label based indexing your start as well as stop value both are included in the output.

print(s['banana':'kiwi'])