import math
import numpy as np
import matplotlib.pyplot as plt

v0 = 14
a = 7777


def runge_kutta(x, y, h, vb):
    k1 = f(x, y, vb)
    k2 = f(x + (.5*h), y + (.5 * h * k1), vb)
    k3 = f(x + (.5*h), y + (.5 * h * k2), vb)
    k4 = f(x + h, y + (h*k3), vb)

    return y + (1/6)*h*(k1 + 2*k2 + 2*k3 + k4)


def f(x, y, vb):
    # Numerator of big fraction on rhs
    w = 4*v0*((x/a)-(x**2/a**2))
    # Denominator of big fraction on rhs
    den = vb * (x/math.sqrt(x**2 + y**2))

    left = y/x
    right = w/den
    return left - right


def main():
    h = -.1
    x = np.arange(a, 0, h)
    y = [0]
    vb = [7, 14, 21]

    for spd in vb:
        for ind, el in enumerate(x[:-1]):
            y.append(runge_kutta(el, y[ind], h, spd))

        with open('speed' + str(spd) + '.txt', 'w') as fi:
            for item in list(zip(x, y)):
                fi.write("%s\n" % str(item))

        plt.plot(x, y)
        y = [0]

    plt.show()


main()
