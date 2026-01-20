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
    
    #Generating the noise and adding to the clean signal
    t = np.arange(0, 1, 1/fs)
    noise_sample = []
    noise_sample = np.random.normal(0, 1, 500) 
    signal = (A * np.sin(2 * np.pi * f * t))
    noisy_signal = []
    noisy_signal = 0.25 * noise_sample + signal
    
    t1 = np.arange(0, 1, 1/fs)
    y1 = noisy_signal
    
    #Clean signal
    f = 10
    fs = 500
    A = 5
    t = np.arange(0, 1, 1/fs)
    y = A * np.sin(2 * np.pi * f * t)

    plt.plot(t1, y1, color='red')
    plt.plot(t,y, color = 'blue')
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
    #writing to the sensor_readings csv file
    with open('sensor_readings.csv', 'w', newline='') as file :
        df.to_csv(file, index=False)

def plot_temp () :
    temps_to_plot = []
    times_to_plot = []
    df = pd.read_csv('sensor_readings.csv')
    
    #plotting 
    temps_to_plot = df.loc[41:80, "Temperature(C)"].tolist()
    times_to_plot = df.loc[41:80, "Time (s)"].tolist()
    print(temps_to_plot)
    print(times_to_plot)
    
    y = np.array(temps_to_plot)
    x = np.array(times_to_plot)
    
    plt.plot(x,y)
    plt.title("Temperature Readings Over Time")
    plt.ylabel("Temperature (C)")
    plt.xlabel("Time (s)")
    plt.show()

#Part 6: ************************Exploring and Handling Sensor Data**********************************
def load_csv() :
    df = pd.read_csv('env_temp_humidity_clean.csv')
    
    temp = np.array(df.loc[0:1441, "temperature_C"].tolist())
    humidity = np.array(df.loc[0:1441, "humidity_pct"].tolist())
    
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    reference_time = df['timestamp'].iloc[0].normalize() 
    time_difference = df['timestamp'] - reference_time
    df['total_minutes'] = time_difference.dt.total_seconds() / 60
    total_min = df['total_minutes'].astype(int)
    
    time = total_min
    print(time)
    
    plt.title("Temperature vs Time")
    plt.scatter(time,temp)
    plt.xlabel("Time (min)")
    plt.ylabel("Temperature (C)")
    plt.show()
    
    plt.title("Humidity vs Time")
    plt.scatter(time, humidity)
    plt.xlabel("Time (min)")
    plt.ylabel("Humidity")
    plt.show()

    # Display key info
    print("First 5 Rows:")
    print(df.head())

    print("\nColumn Names:")
    print(df.columns)

    print("\nData Types")
    print(df.dtypes)
    
    # Check for missing values
    print("\nMissing Values: ")
    print(df.isna().sum())

    # Check for outliers
    print("\nChecking for outliers: ")
    print(df.describe())



#Calling the functions
if __name__ == "__main__" :
    #5.1
    plot_freq()
    #5.2
    sample_noises()
    #5.3
    sample_temps()
    plot_temp()
    #6
    load_csv()



