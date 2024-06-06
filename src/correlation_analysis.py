# correlation_analysis.py

import pandas as pd
from scipy.stats import pearsonr

def calculate_correlation(df):
    correlation_coefficient, p_value = pearsonr(df['X_0'], df['X_2'])
    return correlation_coefficient, p_value

if __name__ == "__main__":
    df = pd.read_csv('data/filled_input1.csv')
    correlation_coefficient, p_value = calculate_correlation(df)
    print("Correlation Coefficient:", correlation_coefficient)
    print("P-Value:", p_value)
