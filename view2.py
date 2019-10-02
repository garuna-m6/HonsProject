# import show3d
import numpy as np
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a=np.loadtxt(sys.argv[1])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# print(a[:,0])
xs = a[:,0]
ys = a[:,1]
zs = a[:,2]
print(xs.shape)
print(ys.shape)
print(zs.shape)

ax.scatter(xs,ys,zs)
plt.show()

# show3d.showpoints(a)

