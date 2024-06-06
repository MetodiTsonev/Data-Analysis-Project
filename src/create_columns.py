# create_columns.py

import pandas as pd

def create_columns(df):
    df['Z1'] = df['X_8'].apply(lambda x: 1 if 'Ribo' in str(x) else 0)
    df['Z2'] = df['X_8'].apply(lambda x: str(x).count('Ribo'))
    return df

if __name__ == "__main__":
    df = pd.read_csv('data/filled_input1.csv')
    df = create_columns(df)
    df.to_csv('data/processed_input1.csv', index=False)
