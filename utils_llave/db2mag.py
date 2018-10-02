import numpy as np


def db2mag(db):
    mag = np.power(10., db / 20.)
    return mag
