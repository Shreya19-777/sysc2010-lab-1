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
#5.1 Plotting a Frequency Distribution
def plot_freq ():
    f = 10
    fs = 500
    A = 5
    duration =1
    t = np.arange(0, 1, 1/fs)
    y = A * np.sin(2 * np.pi * f * t)
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
    duration =1
    t = np.arange(0, 1, 1/fs)
    y = noisy_signal
    noise_sample = []
    noise_sample = np.random.normal(0, 1, 500) 
    signal = (A * np.sin(2 * np.pi * f * t))
    noisy_signal = []
    noisy_signal = 0.25 * noise_sample + signal

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
    plt.title("Tempraature Readings Over Time")
    plt.ylabel("Temprature (C)")
    plt.xlabel("Time (s)")
    plt.show()


if __name__ == "__main__" :
    #sample_temps()
    plot_temp()
    plot_freq()
    sample_noises ()



