import numpy as np


def mag2db(mag):
    db = 20 * np.log10(np.abs(mag)+np.finfo(float).eps)
    return db
