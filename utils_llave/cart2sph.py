import numpy as np


def cart2sph(x, y, z):
    mat_m = np.concatenate((x, y, z), axis=1)
    rad_v = np.linalg.norm(mat_m, axis=1)
    rad_v = rad_v[np.newaxis, :].T

    subrad_v = np.linalg.norm(np.concatenate((x, y), axis=1), axis=1)
    subrad_v = subrad_v[np.newaxis, :].T

    azim_v = np.rad2deg(np.arctan2(y, x))
    elev_v = np.rad2deg(np.arctan2(z, subrad_v))

    return rad_v, azim_v, elev_v
