import matplotlib.pyplot as plt
import numpy as np

def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo*np.sin(2*frekuensi * t + np.deg2rad(theta))
    return t,y

t,y = sinusGenerator(1,1,4,0)

plt.plot(t,y)

plt.axis([0,4,-1.5,1.5])

plt.show()


























