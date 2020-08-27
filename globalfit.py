from functools import wraps
import numpy as np
from scipy.optimize import curve_fit


def globalfit(func, x, ys, *args, **kwargs):
    ys = np.concatenate(ys)

    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        res = np.concatenate(res)
        return res

    return curve_fit(wrapper, x, ys, *args, **kwargs)



