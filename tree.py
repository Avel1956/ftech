from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

Matx = np.random.random((3, 3))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = Matx[0][0]
y = Matx[1][0]
z = Matx[2][0]

ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
print(np.matrix(Matx))
