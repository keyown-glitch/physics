# This is a sample Python script.
import numpy as np
import matplotlib.pyplot as plt
# x = Acos(2pi*f*t)
# T = 2pisqrt(m/k)
A = float(input("Distance Stretched:"))
k = float(input("Spring Constant:"))
m = float(input("Mass:"))
b = float(input("Duration:"))
assert b and m and k and A >= 0
T = 2*np.pi*np.sqrt(m/k)
f = 1/T


time_axis = np.linspace(0, b, 1000)
x_value = []

for element in time_axis:
    x_value.append(A*np.cos(2*np.pi*f*element))
plt.plot(time_axis, x_value, label = "Position")
plt.xlabel('Time (seconds)')
plt.ylabel('Position and Force')

F = []
for element in time_axis:
    F.append(k*A*np.cos(2*np.pi*f*element))
plt.plot(time_axis, F, label = "Force")

t = int(input("t = "))

def F(t):
    if t <= b:
            print("F = ", k*A*np.cos(2*np.pi*f*t))
    else:
        t = int(input("try again t = "))


F(t)

plt.legend()


# F = []
# for position in x_value:
#     F.append(k*position)
# plt.plot(x_value, F, label = "Force")

# print("x_value=", x_value)
# print("time_value=", time_axis)


plt.show()