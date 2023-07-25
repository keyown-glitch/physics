import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import animation
plt.rcParams["figure.figsize"] = 11,11

L = float(input("Length: "))
angle = float(input("Angle: "))

T = 2*np.pi*np.sqrt(L/9.8)
f = round(30*T + 2)
ymax = (L-L*np.cos(angle))
xmax = L*np.sin(angle)

def cycle(o):
    x = [xmax*np.sin(-o*np.pi/(2*angle))]
    y = [-ymax*(np.cos(o*np.pi/angle)-1)/2]
    return np.array([x, y])
    
fig, ax = plt.subplots()
ball, = ax.plot(L*np.sin(-angle), L-L*np.cos(-angle), marker = "o", markersize = "9")
rope, = ax.plot(L*np.sin(angle), np.cos(angle)*L+1)

def update(o):
    x, y = cycle(o)
    ball.set_data([x], [y])
    rope.set_data([0, x], [1, y])
    return ball, rope,


plt.xlim(-1, 1)
plt.ylim(0, 1)
plt.grid()
ani = FuncAnimation(fig, update, interval=10, blit=True, repeat=True,
                     frames=np.linspace(angle,5*angle,f, endpoint=False))
writergif = animation.PillowWriter(fps=30)
ani.save("Pendulum.gif", writer = writergif)
plt.show()
