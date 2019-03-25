from __future__ import print_function
import tigre
import copy
import tigre.algorithms as algs
import numpy as np
import tigre.algorithms as algs
from tigre.demos.Test_data import data_loader
from matplotlib import pyplot as plt

geo = tigre.geometry(mode='cone', nVoxel=np.array([264, 264, 264]), default_geo=True)
niter = 10
nangles = 100
angles = np.linspace(0, 2 * np.pi, nangles, dtype=np.float32)
#angles_2 = np.zeros((nangles, ), dtype=np.float32)
#angles_3 = np.ones((nangles, ), dtype=np.float32)
#angles = np.vstack((angles_1, angles_2, angles_3)).T
head = data_loader.load_head_phantom(geo.nVoxel)
proj = tigre.Ax(head,geo,angles)
output_tv = algs.ossart_tv(proj,geo,angles,niter=10,blocksize=20,tviter=50,tvlambda=50)
output = algs.ossart(proj,geo,angles,niter=10,blocksize=20)
plt.imshow(np.hstack((output_tv[geo.nVoxel[0]/2],output[geo.nVoxel[0]/2])))
plt.colorbar()
plt.show()