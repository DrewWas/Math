#https://en.wikipedia.org/wiki/Lagrange_polynomial

import matplotlib.pyplot as plt
from random import randint


def plot_points(num_of_points, ceiling):
    x_points = [i for i in range(0, num_of_points)]
    y_points = [randint(0, ceiling) for i in range(0, num_of_points)]
    points = [(x_points[i], y_points[i]) for i in range(0, num_of_points)]
    print(points)

    plt.plot(x_points, y_points, "o")
    plt.xlim(-1, num_of_points + 1)
    plt.ylim(-ceiling, ceiling + 1)
    plt.show()
    return points 



x = plot_points(10, 10)
x
    
