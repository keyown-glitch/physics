import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = 11,11
from matplotlib.animation import FuncAnimation
from matplotlib import animation

L = float(input("Length: "))
angle = float(input("Angle: "))
# x1 = np.linspace(-L, L, 1000)
#L = np.sqrt(x**2+y**2)
#angles = np.linspace(-0.111111111*np.pi, 0.111111111*np.pi, 1000)
# 10000)
T = 2*np.pi*np.sqrt(L/9.8)
# T = f-2/30
f = round(30*T + 2)
#o = np.linspace(angle, 5*angle, f)
ymax = (L-L*np.cos(angle))
xmax = L*np.sin(angle)
#x1 = np.linspace(-xmax*np.sin(o*np.pi/(2*angle)), xmax*np.sin(o*np.pi/(2*angle)), 33)
def cycle(o):
    x = [xmax*np.sin(-o*np.pi/(2*angle))]
    y = [-ymax*(np.cos(o*np.pi/angle)-1)/2]
    return np.array([x, y])
    #return np.array([[-1, -0.5, 0], [0.5, 0.5, 0.5]])
fig, ax = plt.subplots()
ball, = ax.plot(L*np.sin(-angle), L-L*np.cos(-angle), marker = "o", markersize = "9")
rope, = ax.plot(L*np.sin(angle), np.cos(angle)*L+1)
# def line(o):
#     return np.array([[xmax*np.sin(-o*np.pi/(2*angle)), xmax*np.sin(o*np.pi/(2*angle))], (-ymax*(np.cos(o*np.pi/angle))-1)*np.array([xmax*np.sin(-o*np.pi/(2*angle)), xmax*np.sin(o*np.pi/(2*angle))])/(xmax*np.sin(-o*np.pi/(2*angle)))+L])
#    # return np.array([[xmax*np.sin(-o*np.pi/(2*angle))], [((ymax*np.cos(o*np.pi/angle) - 1)*xmax*np.sin(-o*np.pi/(2*angle))/(xmax * np.sin(-o * np.pi /(2 * angle)))) + L]])
#     #return np.array([[-1, -0.5, 0], [0.5, 0.5, 0.5]])


# def rope(o):
#     m = np.cos(-o) / np.sin(-o)
#     return np.array(x1, m*x1 -(L-L*np.cos(angle))*(np.cos(np.pi)-1)/2 - m*L*np.sin(angle)*np.sin(np.pi / 2))
#     #y2 = m*x2 + -(L - L * np.cos(angle))*(np.cos(np.pi) - 1)/2 - m * L * np.sin(angle) * np.sin(np.pi / 2)
def update(o):
    x, y = cycle(o)
    #x2, y2 = line(o)
    ball.set_data([x], [y])
    rope.set_data([0, x], [1, y])
    return ball, rope,



plt.xlim(-1, 1)
plt.ylim(0, 1)
plt.grid()
ani = FuncAnimation(fig, update, interval=10, blit=True, repeat=True,
                     frames=np.linspace(angle,5*angle,f, endpoint=False))
writergif = animation.PillowWriter(fps=30)
ani.save("pendul6.gif", writer = writergif)
plt.show()