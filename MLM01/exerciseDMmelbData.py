import pandas as pd
melbourne_file_path = 'melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)
#melbourne_data.columns
print(melbourne_data.describe())
#melbourne_data = melbourne_data.dropna(axis=0)