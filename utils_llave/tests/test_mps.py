import numpy as np
import utils_llave as u
import matplotlib.pyplot as plt

N = 128
N2 = int(N/2+1)
mag = np.zeros(N2)
mag[0:N2-30] = 1
mag = mag[:, np.newaxis]
mag = np.concatenate((mag, np.flipud(mag[1:N2-1, :])), axis=0)
ir = np.fft.ifft(mag, axis=0)
ir = np.concatenate((ir[N2:N, :], ir[1:N2]), axis=0)

spc_mp = u.min_phase_spectrum(mag)
ir_mp = np.fft.ifft(spc_mp, axis=0)

plt.plot(ir, 'b')
plt.plot(ir_mp, 'r')
plt.show()

plt.plot(np.abs(mag))
plt.plot(np.abs(spc_mp))
plt.show()
