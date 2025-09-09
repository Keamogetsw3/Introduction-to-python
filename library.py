# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Create a NumPy array of numbers from 1 to 10 and calculate the mean
array = np.arange(1, 11)
mean_value = np.mean(array)
print("NumPy Array:", array)
print("Mean of array:", mean_value)

# Load a small dataset into a pandas DataFrame and display summary statistics
data = {
    'Name': ['Maria', 'David', 'Lewis', 'Payne'],
    'Age': [30, 30, 35, 45],
    'Salary': [55000, 50000, 53000, 54000]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:\n", df)
print("\nSummary Statistics:\n", df.describe())
