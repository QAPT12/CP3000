import pandas as pd

# Creating a sample DataFrame

data = {

'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],

'Age': [25, 30, 35, 40, 29],

'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],

'Salary': [70000, 80000, 120000, 110000, 95000]

}

df = pd.DataFrame(data)

# Viewing the first few rows

print("First 5 rows:")

print(df.head())

# Viewing the last few rows

print("\nLast 5 rows:")

print(df.tail())

# Getting a summary of the DataFrame

print("\nDataFrame info:")

print(df.info())

# Getting statistical summaries of numerical columns

print("\nStatistical summary:")

print(df.describe())

# Getting the dimensions of the DataFrame

print("\nShape of the DataFrame:")

print(df.shape)

# Getting the column labels

print("\nColumn labels:")

print(df.columns)

# Getting the row labels

print("\nRow labels:")

print(df.index)

# Getting the data types of each column

print("\nData types of each column:")

print(df.dtypes)

# Detecting missing values

print("\nDetecting missing values:")

print(df.isnull())

# Counting unique values in the 'City' column

print("\nValue counts for 'City' column:")

print(df['City'].value_counts())

# Getting unique values of the 'City' column

print("\nUnique values in 'City' column:")

print(df['City'].unique())

# Getting the number of unique values per column

print("\nNumber of unique values per column:")

print(df.nunique())

# Getting the memory usage of the DataFrame

print("\nMemory usage of the DataFrame:")

print(df.memory_usage())

# Randomly sampling rows from the DataFrame

print("\nRandom sample of 2 rows:")

print(df.sample(2))