from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from sys import argv
import pdb
import pandas as pd 

# x,y,z = np.loadtxt('xyz.csv', unpack=True)
df = pd.read_csv('xyz.csv')
x = df['x']
y = df['y']
z = df['z']

fig = plt.figure()
ax = Axes3D(fig)
surf = ax.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0.1)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()