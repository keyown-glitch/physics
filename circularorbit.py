import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = 12,11
from matplotlib.animation import FuncAnimation
from matplotlib import animation

G = 6.67e-11
R = float(input("Distance Separated (Kilometers): "))
M = float(input("Mass of Celestial Body (Kilograms): "))
v = np.sqrt(G*M/(R*1000))


fig, ax = plt.subplots()
moon, = ax.plot(0, R, marker = "o", markersize = 11, markeredgecolor = "silver", markerfacecolor = "lightslategray")
earth = ax.plot(0, 0, marker = "o", markersize = 19, markeredgecolor="green", markerfacecolor="cornflowerblue")
ax.axis([-1.5, 1.5, -1.5, 1.5])

def circle(o):
    return np.array([R * np.cos(o), R * np.sin(o)])
def orbit(o):
    x1, y2 = circle(o)
    moon.set_data([x1],[y2])
    return moon,

plt.xlim(-R-100000, R+100000)
plt.ylim(-R-100000, R+100000)
plt.grid()


f = round(120*np.pi*R*1000*30/(v*2355466.58) - 1)
T = 2355466.58*(f + 1)/1800
ani = FuncAnimation(fig, orbit, interval=10, blit=True, repeat=True,
                     frames=np.linspace(0,2*np.pi,f, endpoint=False))

print("Velocity =", v, "m/s")
print("Orbital Period:", T/(86400), "Days")
writergif = animation.PillowWriter(fps=30)
ani.save("Circular Orbit (Moon/Earth.gif", writer = writergif)
plt.show()
