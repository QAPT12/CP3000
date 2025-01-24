import pandas as pd

# Creating a sample DataFrame

data = {

'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],

'Age': [25, 30, 35, 40, 29],

'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],

'Salary': [70000, 80000, 120000, 110000, 95000]

}

df = pd.DataFrame(data)

# 1. Using the query() method

# Query to get rows where Age is greater than 30

subset_query = df.query('Age > 25')

print("Subset using query():")

print(subset_query)

# 2. Using the loc[] accessor

# Access rows by label index and columns by label

subset_loc = df.loc[1:3, ['Name', 'City']]

print("\nSubset using loc[]:")

print(subset_loc)

# 3. Using the iloc[] accessor

# Access rows by integer location and columns by integer #location

subset_iloc = df.iloc[1:4, [0, 2]]

print("\nSubset using iloc[]:")

print(subset_iloc)