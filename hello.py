import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

print("Libraries imported successfully!")
# Create a small series
data = pd.Series([1, 3, 5, np.nan, 6, 8])
print(data)

#Loading the CSV file 
#CSV File
file = 'env_temp_humidity_clean.csv'
df = pd.read_csv(file, header=None)
df.columns = ["Column1", "Column2", "Column3"]
print(df.loc[0, "Column1"])


#Part 5: Hands on Tasks
#5.3 Simulate Sensor Readings
def sample_temps () :
    temp_samples = []
    for i in range(120) :
        sec = i*60
        temp_samples.append({"Time (s)": sec, "Temperature(C)" : round(random.uniform(35.5, 36.5), 2)})

    print(temp_samples)
    
    df = pd.DataFrame(temp_samples)
    with open('sensor_readings.csv', 'w', newline='') as file :
        df.to_csv(file, index=False)

def plot_temp () :
    temps_to_plot = []
    times_to_plot = []
    df = pd.read_csv('sensor_readings.csv')
    
    temps_to_plot = df.loc[40:81, "Temperature(C)"].tolist()
    times_to_plot = df.loc[40:81, "Time (s)"].tolist()
    print(temps_to_plot)
    print(times_to_plot)
    
    y = np.array(temps_to_plot)
    x = np.array(times_to_plot)
    
    plt.plot(x,y)
    plt.show()
    plt.xlabel("Time (s)")

if __name__ == "__main__" :
    #sample_temps()
    plot_temp()