import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("train.csv")
print(df.head())#first 5 rows
print(df.info())#name of columns+how much values+ datatypes
print(df.shape) #(rows,columns)

print(df.isnull().sum())#How many missing values ​​are there in each column?(know Missing Values)

print(df.describe())#Summary Statistics(mean,min,max,med)

#Dealing with missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df.drop("Cabin", axis=1, inplace=True)#Since a very large number of its values ​​are missing, it won't be useful enough for our analysis.


print(df.groupby("Sex")["Survived"].mean())#Survival by Gender
print(df.groupby("Pclass")["Survived"].mean())#Survival by Class
print(df.groupby(["Sex", "Pclass"])["Survived"].mean())#Survival by Class+sex

#Graphs
# Survival by Gender
sns.barplot(data=df, x="Sex", y="Survived")
plt.title("Survival Rate by Gender")
plt.show()

# Survival by Class
sns.barplot(data=df, x="Pclass", y="Survived")
plt.title("Survival Rate by Passenger Class")
plt.show()

# Gender + Class Heatmap
survival_table = df.pivot_table(
     values="Survived",
     index="Sex",
     columns="Pclass",
     aggfunc="mean"
 )
sns.heatmap(survival_table, annot=True, fmt=".2f")
plt.title("Survival Rate by Gender and Class")
plt.show()

#Correlation
correlation = df.corr(numeric_only=True)
sns.heatmap(correlation, annot=True, fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()



# =========================
# Key Insights
# =========================

# 1. Gender had a strong relationship with survival.
# Female passengers had a survival rate of about 74.2%,
# while male passengers had a survival rate of about 18.9%.

# 2. Passenger class also showed a clear survival pattern.
# First-class passengers had the highest survival rate (63.0%),
# followed by second class (47.3%), then third class (24.2%).

# 3. Gender and passenger class together showed an even clearer pattern.
# Female passengers in first class had the highest survival rate (96.8%),
# while male passengers in third class had the lowest (13.5%).

# 4. The dataset contained missing values.
# Age had 177 missing values, Cabin had 687,
# and Embarked had 2 missing values.
# Age was filled using the median,
# Embarked was filled using the mode,
# and Cabin was removed because it had too many missing values.

# 5. Overall, gender and passenger class were two important factors
# associated with survival in the Titanic dataset.