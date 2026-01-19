import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

'''
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
'''

#Part 5: ***********************Hands on Tasks*******************************
#5.1 Plotting a Frequency Distribution
def plot_freq ():
    f = 10
    fs = 500
    A = 5
    t = np.arange(0, 1, 1/fs)
    y = A * np.sin(2 * np.pi * f * t)
    
    #Plotting the frequency
    plt.plot(t,y)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Sine Wave")
    plt.show()
    print("Frequency plot complete.")
    

#5.2 Generating Random Noise
def sample_noises ():
    f = 10
    fs = 500
    A = 5
    
    t = np.arange(0, 1, 1/fs)
    noise_sample = []
    noise_sample = np.random.normal(0, 1, 500) 
    signal = (A * np.sin(2 * np.pi * f * t))
    noisy_signal = []
    noisy_signal = 0.25 * noise_sample + signal
    
    t = np.arange(0, 1, 1/fs)
    y = noisy_signal

    plt.plot(t, y)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Real Life Noisy Signal")
    plt.show()

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
    plt.title("Temperature Readings Over Time")
    plt.ylabel("Temperature (C)")
    plt.xlabel("Time (s)")
    plt.show()

#Part 6: Exploring and Handling Sensor Data*************************************
def load_csv() :
    df = pd.read_csv('env_temp_humidity_clean.csv')
    x = np.array(df.loc[0:1441, "temperature_C"].tolist())
    y = np.array(df.loc[0:1441, "humidity_pct"].tolist())
    
    column_names = df.columns.tolist()
    print(column_names)
    plt.scatter(x,y)
    plt.show()
    
    # Convert timestamp to actual datetime objects
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Display key info
    print("--- First 5 Rows ---")
    print(df.head())

    print("\n--- Column Names ---")
    print(df.columns)

    print("\n--- Data Types ---")
    print(df.dtypes)



#Calling the functions
if __name__ == "__main__" :
    #sample_temps()
    #plot_temp()
    #plot_freq()
    #sample_noises()
    load_csv()



