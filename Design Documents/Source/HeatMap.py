import TickerScrape
import numpy as np
import matplotlib.pyplot as plt


def show_heat_map():
    data = np.random.random((12, 12))
    plt.imshow(data, cmap='autumn', interpolation='nearest')

    plt.title("2-D Heat Map")
    plt.show()


class HeatMap():
    pass


