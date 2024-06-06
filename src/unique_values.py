# unique_values.py

import pandas as pd

def unique_values_table(df):
    return df.groupby(['X_6', 'X_7'])['X_1'].nunique().unstack()

if __name__ == "__main__":
    df = pd.read_csv('data/filled_input1.csv')
    unique_values = unique_values_table(df)
    print("Unique Values Table:\n", unique_values)
