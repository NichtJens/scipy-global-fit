#!/usr/bin/env python3

from scipy.stats import norm
import numpy as np
from matplotlib import pyplot as plt

from globalfit import globalfit


# create some example data
gauss = norm.pdf
x = np.linspace(-100, 100, 100)
g1 = gauss(x, -1,  9)
g2 = gauss(x,  1, 11)


def fitfunc(x, x0, std):
    f1 = f2 = gauss(x, x0, std)
    return f1, f2


popt, _pcov = globalfit(fitfunc, x, (g1, g2))
fit1, fit2 = fitfunc(x, *popt)


plt.subplot(211)
plt.ylim(0, 0.05)
plt.plot(g1, "x-")
plt.plot(fit1)

plt.subplot(212)
plt.ylim(0, 0.05)
plt.plot(g2, "x-")
plt.plot(fit2)

plt.show()



