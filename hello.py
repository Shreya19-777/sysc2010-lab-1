import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("Libraries imported successfully!")
# Create a small series
data = pd.Series([1, 3, 5, np.nan, 6, 8])
print(data)

#Loading the CSV file
file = 'env_temp_humidity_clean.csv'
df = pd.read_csv(file)