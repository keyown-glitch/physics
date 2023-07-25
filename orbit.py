import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = 12,11
from matplotlib.animation import FuncAnimation
from matplotlib import animation
#5.97200e24 Kg
# 382500 km
G = 6.67e-11
# 1 s orbit period = 2355466.58 REAL s orbit period
R = float(input("Distance Separated (Kilometers): "))
M = float(input("Mass of Celestial Body (Kilograms): "))
v = np.sqrt(G*M/(R*1000))

# for t in time:
#     angle.append(v*t/R)
#     for theta in angle:
#         x = R*np.cos(angle)
#         y = R*np.sin(angle)
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
# v = 2piR/T, T = 2355466.58*(frames + 1)/fps
# 2piR/sqrtGM/R = 2355466.58*(frames + 1)/fps
# 2piR*fps/(sqrtGM/R*2355466.58) = f + 1
# 2piR*fps/(sqrtGM/R*2355466.58) - 1 = f
f = round(120*np.pi*R*1000*30/(v*2355466.58) - 1)
T = 2355466.58*(f + 1)/1800
ani = FuncAnimation(fig, orbit, interval=10, blit=True, repeat=True,
                     frames=np.linspace(0,2*np.pi,f, endpoint=False))

print("Velocity =", v, "m/s")
print("Orbital Period:", T/(86400), "Days")
writergif = animation.PillowWriter(fps=30)
ani.save("Earth+Moon4.gif", writer = writergif)
plt.show()