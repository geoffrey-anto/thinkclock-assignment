# ThinkClock Take Home Assignment

## Introduction
In this assignment, we will analyze the NASA Battery Dataset available on Kaggle: [NASA Battery Dataset](https://www.kaggle.com/datasets/patrickfleith/nasa-battery-dataset/data).

### Objective
Created plots using Plotly to visualize how the following battery parameters change as the battery cell ages through charge/discharge cycles:
- **Battery_impedance**
- **Rct**: Estimated charge transfer resistance (Ohms)
- **Re**: Estimated electrolyte resistance (Ohms)

### Steps
1. **Data Exploration**: Load and explored the dataset to understand its structure and contents.
2. **Data Preprocessing**: Clean and preprocessed the data to extract relevant information for plotting.
3. **Plotting with Plotly**: Created interactive plots to visualize the changes in Battery_impedance and Rct over the aging process.

### Resources
- [Plotly Documentation](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)

### Deliverables
- A Jupyter notebook or Python script containing:
    - Data loading and preprocessing steps
    - Plotly visualizations for Battery_impedance, Rct and Re
    - Insights and observations from the plots

### Code Structure
    The project directory contains the following files:

    - `analysis.ipynb`: Jupyter notebook containing data loading and preprocessing.
    - `layouts.py`: Python script for defining the layout of the plots.
    - `main.py`: Main Python script to run the analysis and generate plots.
    - `README.md`: This file, providing an overview and instructions for the assignment.
    - `utils.py`: Utility functions for data processing and analysis.

### Instructions
1. Clone the repository to your local machine.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Clone the NASA Battery Dataset from Kaggle and place the CSV file in the `dataset` folder.
4. Copy the `metadata-norm.csv` file from the data folder to the projects dataset directory after cloning the dataset.
5. Run the `main.py` script to generate the plots.

### Note
- The dataset contains multiple CSV files, but we will focus on the `metadata-norm.csv` file for this assignment.

### Usage
- There are 3 input select fields to choose the Battery ID, Parameter, and frequency(In the case of Battery_impedance).
- The plots will be updated based on the selected values.

### Images

![image](https://github.com/user-attachments/assets/e93a0b3c-2c3b-4ade-8330-4527e5cebd20)
![image](https://github.com/user-attachments/assets/9adcff69-5688-4dbc-96e6-338782d1de7c)
![image](https://github.com/user-attachments/assets/bf7ff53b-af7e-44a5-bc06-d1b4c8c4623b)
![image](https://github.com/user-attachments/assets/5afc5ae6-1707-413a-8d42-6f597f0759f3)


