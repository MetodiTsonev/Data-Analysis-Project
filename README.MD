Setup Instructions
1. Install Dependencies
Create a virtual environment and install the required packages using the following commands:


python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

2. Data Preparation
Place the provided dataset (input1.csv) in the data directory.

3. Running the Analysis
You can run the analysis through the individual scripts or by using the Jupyter notebook.

Option 1: Running Individual Scripts
Navigate to the project root directory and execute the scripts sequentially:

cd pythonProject
python3 src/fill_missing_values.py
python3 src/correlation_analysis.py
python3 src/unique_values.py
python3 src/create_columns.py
python3 src/visualize_data.py


Option 2: Using Jupyter Notebook
Launch the Jupyter notebook and follow the instructions in the notebook to perform the analysis interactively:


jupyter notebook notebooks/analysis.ipynb

4. Output
The results and visualizations will be saved in the output directory. The main output includes:

Filled Dataset: data/filled_input1.csv
Visualization: output/stacked_bar_chart.png