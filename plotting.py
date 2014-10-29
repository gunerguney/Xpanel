__author__ = 'cal02'

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline


def plot_chart(x,y,file_name):
    plt.title(file_name)
    plt.grid(True)
    plt.plot(x,y)
    plt.savefig( str(file_name) + ".png",dpi=100)
    plt.close()



