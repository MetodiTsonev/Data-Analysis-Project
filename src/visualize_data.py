# visualize_data.py

import pandas as pd
import matplotlib.pyplot as plt

def plot_stacked_bar_chart(df):
    # Prepare data for the stacked bar chart
    stacked_data = df.pivot_table(index='X_7', columns='X_6', values='Z1', aggfunc='count')

    # Plot
    ax = stacked_data.plot(kind='bar', stacked=True, color=['#1f77b4', '#ff7f0e'], figsize=(10, 7))

    # Add labels
    for container in ax.containers:
        ax.bar_label(container, label_type='center')

    # Customize chart
    ax.set_xlabel('X_7')
    ax.set_ylabel('X_6')
    ax.set_title('Stacked Bar Chart of X_6 and X_7')
    ax.legend(title='X_6', labels=['Females', 'Males'], loc='upper left')

    # Save the figure
    plt.savefig('output/stacked_bar_chart.png')
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv('data/processed_input1.csv')
    plot_stacked_bar_chart(df)
