import matplotlib.pyplot as plt
import numpy as np

def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo*np.sin(2*frekuensi * t + np.deg2rad(theta))
    return t,y

t1,y1 = sinusGenerator(1,1,5,0)
t2,y2 = sinusGenerator(1,1,5,90)
t3,y3 = sinusGenerator(1,1,5,180)
t4,y4 = sinusGenerator(1,1,5,270)

#tipe 1
#plt.plot(t1,y1, label="sin(0)")
#plt.plot(t2,y2, label="sin(90)")
#plt.legend()

#tipe 2
#plt.plot(t1,y1, label="sin(0)")
#plt.plot(t2,y2, label="sin(90)")
#plt.legend(loc="upper center")

#tipe 3
#plt.plot(t1,y1, label="sin(0)")
#plt.plot(t2,y2, label="sin(90)")
#plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05))

#tipe 4
plt.figure(1)
ax = plt.subplot(111)

plt.plot(t1,y1, label="sin(0)")
plt.plot(t2,y2, label="sin(90)")
plt.plot(t3,y3, label="sin(180)")
plt.plot(t4,y4, label="sin(270)")

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.7, box.height])

plt.legend(loc="upper center", bbox_to_anchor=(1.2,1))

plt.show()








