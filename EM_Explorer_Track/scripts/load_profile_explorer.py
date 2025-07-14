import matplotlib.pyplot as plt

def plot_load_profiles(load_data):
    for label, series in load_data.items():
        plt.plot(series, label=label)
    plt.legend()
    plt.xlabel("Hour")
    plt.ylabel("kWh")
    plt.title("Hourly Load Profiles")
    plt.grid(True)
    plt.show()
