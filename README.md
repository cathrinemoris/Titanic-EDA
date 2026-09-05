# 🚢 Titanic Dataset — Exploratory Data Analysis

## 📌 Project Overview

This project performs an **Exploratory Data Analysis (EDA)** on the Titanic dataset using Python.

The goal is to explore the dataset, clean missing data, analyze survival patterns, and visualize the relationships between passenger characteristics and survival.

---

## 📊 Dataset

The dataset used in this project is the **Titanic: Machine Learning from Disaster** dataset.

It contains information about passengers such as:

* Passenger class
* Gender
* Age
* Number of siblings/spouses
* Number of parents/children
* Ticket
* Fare
* Cabin
* Port of embarkation
* Survival status

The dataset contains **891 passengers and 12 columns**.

---

## 🛠️ Tools & Libraries

* Python
* Pandas
* Matplotlib
* Seaborn

---

## 🧹 Data Cleaning

The dataset was inspected for missing values and inconsistent data.

### Missing Values

| Column   | Missing Values |
| -------- | -------------: |
| Age      |            177 |
| Cabin    |            687 |
| Embarked |              2 |

### Handling Missing Data

* **Age:** Missing values were replaced with the median age.
* **Embarked:** Missing values were replaced with the most frequent value (mode).
* **Cabin:** The column was removed because it contained a large number of missing values.

---

## 🔍 Exploratory Data Analysis

Several analyses were performed to understand survival patterns.

### Survival Rate by Gender

* Female survival rate: **74.2%**
* Male survival rate: **18.9%**

This shows a clear difference in survival rates between female and male passengers.

### Survival Rate by Passenger Class

* 1st Class: **63.0%**
* 2nd Class: **47.3%**
* 3rd Class: **24.2%**

Passengers in 1st class had the highest survival rate, while passengers in 3rd class had the lowest.

### Survival Rate by Gender and Class

The combination of gender and passenger class revealed an even clearer pattern:

| Gender | Class | Survival Rate |
| ------ | ----: | ------------: |
| Female |   1st |         96.8% |
| Female |   2nd |         92.1% |
| Female |   3rd |         50.0% |
| Male   |   1st |         36.9% |
| Male   |   2nd |         15.7% |
| Male   |   3rd |         13.5% |

For example, among **1st-class passengers**, females had a survival rate of **96.8%**, compared with **36.9%** for males.

---

## 📈 Visualizations

The analysis includes:

* Survival Rate by Gender
* Survival Rate by Passenger Class
* Survival Rate by Gender and Class
* Correlation Heatmap

These visualizations were used to identify important patterns and relationships within the dataset.

---

## 💡 Key Insights

1. **Gender was strongly associated with survival.**
   Female passengers had a much higher survival rate than male passengers.

2. **Passenger class showed a clear survival pattern.**
   Survival rates decreased from 1st class to 3rd class.

3. **Gender and class together revealed stronger differences.**
   Female passengers generally had higher survival rates than male passengers within the same class.

4. **Missing data required different handling methods.**
   Numerical data such as Age was handled using the median, categorical data such as Embarked was handled using the mode, and Cabin was removed due to the large number of missing values.

---

## 🎯 Conclusion

The Titanic EDA revealed clear survival patterns related to **gender and passenger class**.

Female passengers and passengers traveling in higher classes had noticeably higher survival rates in this dataset. The analysis also demonstrated the importance of properly handling missing data and using visualizations to understand patterns that may not be obvious from raw data alone.

---

## 📁 Project Structure

```text
Titanic-EDA/
│
├── train.csv
├── titanic_eda.py
└── README.md
```

---

## ▶️ How to Run

Clone the repository and make sure `train.csv` is in the same folder as the Python script.

Install the required libraries:

```bash
pip install pandas matplotlib seaborn
```

Then run:

```bash
python titanic_eda.py
```

---

## 👩‍💻 Project

This project was completed as part of a **Data Analysis Internship** to practice Python, Pandas, data cleaning, exploratory data analysis, and data visualization.
