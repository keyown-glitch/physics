import numpy as np
import matplotlib.pyplot as plt


# v^2 = vy^2 + vx^2
# 2vy/a = t
v = float(input("Velocity: "))
angle = int(input("Angle(Degrees): "))*np.pi/180
vx = v*np.cos(angle)
vy = v*np.sin(angle)
b = 2*v*np.sin(angle)/9.8
t = np.linspace(0, b, 1000)


def x(t):
    return vx*t
def y(t):
    return vy*t - 0.5*9.8*t**2
total = []
for time in t:
    total.append(y(time))

max_height = y(b/2)
print("Maximum Height =", max_height)

plt.plot(t, total, label = "Position")
plt.xlabel('Time (seconds)')
plt.ylabel('Height')
plt.show()
