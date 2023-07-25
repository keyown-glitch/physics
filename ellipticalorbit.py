import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation
from matplotlib import animation
import random
G = 6.67 * 10**-11
M = 5.97 * 10**24
m = 7.35 * 10**22
e = 0.055
a = 384400000
b = 383800000
tolerance = 1e-5

T = 2 * np.pi * np.sqrt(a**3 / (G * M))
t_vec = np.linspace(0, T, 131)
E = np.zeros(131)


def f(x, t):
    return x - e * np.sin(x) - 2 * np.pi * t / T


def fd(x):
    return 1 - e * np.cos(x)


# Newton's method
for i in range(len(t_vec)):
    f_value = f(E[i], t_vec[i])
    while np.abs(f_value) >= tolerance:
        E[i] = E[i] - f(E[i], t_vec[i]) / fd(E[i])
        f_value = f(E[i], t_vec[i])

x = a * (np.cos(E) - e)
y = b * np.sin(E)


def orbit(o):
    return np.array([a * (np.cos(o) - e), b * np.sin(o)])


dt = t_vec[1]
vx = []
vy = []
for i in range(len(t_vec) - 1):
    vx.append((x[i+1] - x[i]) / dt)
    vy.append((y[i+1] - y[i]) / dt)

speed = np.sqrt(np.array(vx)**2 + np.array(vy)**2)
print(f'Starting speed: {speed[0]} m/s')
print("Maximum speed:", speed.max())
print("Minimum speed", speed.min())

time = float(input("Speed at time...(Hours)"))*3600

while True:
  i = random.randint(0, 130)
  if np.abs(time - t_vec[i]) < t_vec[1]:
    t = t_vec[i]
    index = i
    break
  else:
    pass


s = np.sqrt(np.array(vx[index])**2 + np.array(vy[index])**2)
radius = np.sqrt(np.array(x[i-1])**2 + np.array(y[i-1])**2)

E = 0.5*m*speed**2 - G*M*m/radius

print(f'Speed after {time/3600} Hours: {s} m/s')

fig, ax = plt.subplots()
moon, = ax.plot([], [], marker='o', color = 'grey', markersize = 7)
earth = ax.plot(np.sqrt(a**2 - b**2), 0, marker='o', color = 'blue', markersize = 14, markeredgecolor = 'green')


def init():
    moon.set_data([], [])
    return moon,


def update(o):
    x, y = orbit(o)
    moon.set_data([x], [y])
    return moon,


ani = FuncAnimation(fig, update, init_func=init, frames=np.linspace(-np.pi, np.pi, 150, endpoint=False),
                    interval=50, blit=True, repeat=True)

plt.plot(x, y, linestyle = 'dashed', linewidth = 0.1, color = 'black')
writergif = animation.PillowWriter(fps=30)
ani.save("moon.gif", writer=writergif)

plt.show()