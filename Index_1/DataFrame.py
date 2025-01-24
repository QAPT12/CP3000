import pandas as pd

# Creating a DataFrame using the DataFrame constructor
data = {
'Name': ['Alice', 'Bob', 'Charlie', 'David'],
'Age': [25, 30, 35, 40],
'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

# Saving the DataFrame to disk as a pickle file
pickle_filename = 'index_1/dataframe.pkl'

df.to_pickle(pickle_filename)

print(f"DataFrame saved to {pickle_filename}")