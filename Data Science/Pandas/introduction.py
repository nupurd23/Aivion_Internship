import pandas as pd
s = pd.Series([10,20,30,40])
print(s)
s.dtype
s.values
s.index
print(s.name)
s.name = "numbers"
print(s)
