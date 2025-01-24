import pandas as pd

# Reading the DataFrame from the pickle file

pickle_filename = 'index_1/dataframe.pkl'

restored_df = pd.read_pickle(pickle_filename)

# Displaying the restored DataFrame

print(restored_df)