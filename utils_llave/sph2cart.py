import numpy as np


def sph2cart(rad_v, azim_v, elev_v):
    x_v = rad_v * np.cos(np.deg2rad(elev_v)) * np.cos(np.deg2rad(azim_v))
    y_v = rad_v * np.cos(np.deg2rad(elev_v)) * np.sin(np.deg2rad(azim_v))
    z_v = rad_v * np.sin(np.deg2rad(elev_v))
    return x_v, y_v, z_v
