#https://en.wikipedia.org/wiki/Lagrange_polynomial

import matplotlib.pyplot as plt
from random import sample


def plot_points(num_of_points, ceiling):
    x_points = sample(range(0,ceiling), num_of_points)
    y_points = sample(range(0,ceiling), num_of_points)
    points = [(x_points[i], y_points[i]) for i in range(0, num_of_points)]
    print(points)

    plt.plot(x_points, y_points, "o")
    plt.xlim(-1, ceiling + 1)
    plt.ylim(-ceiling, ceiling + 1)
    plt.show()
    return points 



plot_points(3, 10)

