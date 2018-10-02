from .fold import *


def min_phase_spectrum(s, axis=0):
    """
    Make cepstrum causal to make spectrum minimum phase
    :param s: <Nx1 vector>
    :return: sm: minimum phase specturm
    """

    cepstrum = np.real(np.fft.ifft(np.log(np.clip(s, 10**-6, np.max(s))), axis=axis))
    cepstrum_causal = fold(cepstrum, axis=axis)
    sm = np.exp(np.fft.fft(cepstrum_causal, axis=axis))
    return sm
