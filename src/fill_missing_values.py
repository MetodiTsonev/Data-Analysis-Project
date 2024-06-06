# src/fill_missing_values.py

import pandas as pd

def fill_missing_values(df):
    df_filled = df.copy()
    for column in df_filled.columns:
        if df_filled[column].dtype in ['int64', 'float64']:
            # Assign the filled values directly
            df_filled[column] = df_filled[column].fillna(df_filled[column].mean())
        else:
            # Assign the filled values directly
            df_filled[column] = df_filled[column].fillna(df_filled[column].mode()[0])
    return df_filled

if __name__ == "__main__":
    df = pd.read_csv('data/input1.csv')
    df_filled = fill_missing_values(df)
    df_filled.to_csv('data/filled_input1.csv', index=False)
