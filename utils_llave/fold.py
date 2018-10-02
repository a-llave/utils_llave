import numpy as np


def fold(r, axis=0):
    # Fold left wing of vector in "FFT buffer format" onto right wing
    # J.O.Smith, 1982 - 2002

    nb_row, nb_col = r.shape

    flipped = 0
    if axis == 0:
        tmp = nb_col
        nb_col = nb_row
        nb_row = tmp
        r = r.T
        flipped = 1

    # RETURN IF TO SMALL
    if nb_col < 3:
        rw = r
        return rw
    # COMPUTE
    elif np.mod(nb_col, 2) == 1:
        nt = int((nb_col + 1) / 2)
        rw = np.concatenate(
            (r[:, 0][:, np.newaxis], r[:, 1:nt] + np.fliplr(np.conjugate(r[:, nt:nb_col])), np.zeros((nb_row, nb_col-nt))), axis=1)
    else:
        nt = int(nb_col / 2)
        rf = np.concatenate((r[:, 1:nt], np.zeros((nb_row, 1))), axis=1)
        rf = rf + np.fliplr(np.conjugate(r[:, nt:nb_col]))
        rw = np.concatenate((r[:, 0][:, np.newaxis], rf, np.zeros((nb_row, nb_col-nt-1))), axis=1)

    if flipped:
        rw = rw.T
    return rw
