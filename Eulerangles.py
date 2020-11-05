import numpy as np
import math as m
import matplotlib.pyplot as plt

def Rx(theta):
  return np.matrix([[ 1, 0           , 0           ],
                   [ 0, m.cos(theta),-m.sin(theta)],
                   [ 0, m.sin(theta), m.cos(theta)]])
  
def Ry(theta):
  return np.matrix([[ m.cos(theta), 0, m.sin(theta)],
                   [ 0           , 1, 0           ],
                   [-m.sin(theta), 0, m.cos(theta)]])
  
def Rz(theta):
  return np.matrix([[ m.cos(theta), -m.sin(theta), 0 ],
                   [ m.sin(theta), m.cos(theta) , 0 ],
                   [ 0           , 0            , 1 ]])

phi = m.pi/2
theta = m.pi/4
psi = m.pi/2
print("phi =", phi)
print("theta  =", theta)
print("psi =", psi)
  
  
R = Rz(psi) * Ry(theta) * Rx(phi)
print(np.round(R, decimals=2))

v1 = np.array([[1],[0],[0]])
v2 = R * v1
print(np.round(v2, decimals=2))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Cartesian axes
ax.quiver(-1, 0, 0, 3, 0, 0, color='grey',linestyle='dashed')
ax.quiver(0, -1, 0, 0,3, 0, color='grey',linestyle='dashed')
ax.quiver(0, 0, -1, 0, 0, 3, color='grey',linestyle='dashed')

# Vector before rotation
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='blue')

# Vector after rotation change based on output value from v2
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='red')
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])
plt.show()