import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def ReLU(x):
    return np.maximum(0, x)

def plot_sigmoid():
    x = np.arange(-5.0, 5.0, 0.1)
    y = sigmoid(x)

    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()

def plot_ReLU():
    x = np.arange(-5.0, 5.0, 0.1)
    y = ReLU(x)

    plt.plot(x, y)
    plt.show()

plot_sigmoid()
plot_ReLU()
