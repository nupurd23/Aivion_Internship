import pandas as pd
import matplotlib.pyplot as plt
data = {200000, 300000, 400000, 500000, 620000 , 450000, 550000, 220000, 1000000}
df = pd.DataFrame(data, columns=["Salary"])

# LINE GRAPH
'''
plt.plot(df["Salary"], color="red", marker="o", linestyle="--" , linewidth=2, markersize=8)
plt.title("Salary Distribution")
plt.xlabel("Index")
plt.ylabel("Salary")
plt.grid()
plt.show() '''

#HISTOGRAM
'''
plt.hist(df["Salary"], bins=5, color="blue", edgecolor="black")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.grid()
plt.show()

'''
#BOX PLOT
'''
plt.boxplot(df["Salary"])
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.grid()
plt.show()
'''

#univariate : Categorical 
df["Department"] = ["HR","IT","Finance","IT" ,"HR","HR","Finance","IT","HR"]
print(df.head())
#print(df.info())
department_counts = df["Department"].value_counts()
'''
#PIE CHART

plt.pie(department_counts, labels=department_counts.index , autopct="%1.1f%%", startangle=140 , explode=[0.1,0,0])
plt.title("Department Distribution")
plt.show()

#COUNT PLOT
plt.bar(department_counts.index, department_counts.values, color=["red","blue","green"])
plt.title("Department Distribution")    
plt.xlabel("Department")
plt.ylabel("Count")
plt.grid()
plt.show()
'''

#Bivariate : Numerical-Numerical

df["Age"] = [25,30, 35,28,29,25,32,31,27]

#print(df.head())

#SCATTER PLOT
'''
plt.scatter(df["Age"], df["Salary"], color="purple")
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.grid()
plt.show()
'''
'''
#LINE PLOT
plt.plot(df["Age"], df["Salary"], color="orange", marker="o", linestyle="-", linewidth=2, markersize=8)
plt.title("Age vs Salary")  
plt.xlabel("Age")
plt.ylabel("Salary")
plt.grid()
plt.show()
'''

#BAR CHART
'''
plt.bar(df["Age"], df["Salary"], color="cyan")
plt.title("Age vs Salary")
plt.xlabel("Age")   
plt.ylabel("Salary")
plt.grid()
plt.show()
'''

#Bivariate : Numerical-Categorical

hr_salary = df[df["Department"] == "HR"]["Salary"]
it_salary = df[df["Department"] == "IT"]["Salary"]
finance_salary = df[df["Department"] == "Finance"]["Salary"]
#BOX PLOT
plt.boxplot([hr_salary, it_salary, finance_salary], labels=["HR","IT","Finance"])
plt.title("Salary Distribution by Department")  
plt.xlabel("Department")
plt.ylabel("Salary")            
plt.grid()
plt.show()