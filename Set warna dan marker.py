import matplotlib.pyplot as plt
import numpy as np

def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo*np.sin(2*frekuensi * t + np.deg2rad(theta))
    return t,y

t1,y1 = sinusGenerator(1,1,5,0)
plt.plot(t1,y1)

t2,y2 = sinusGenerator(1,1,5,30)
plt.plot(t2,y2,'r')

t3,y3 = sinusGenerator(1,1,5,60)
plt.plot(t3,y3, 'g--')

t4,y4 = sinusGenerator(1,1,5,90)
plt.plot(t4,y4, 'y-o')

plt.show()