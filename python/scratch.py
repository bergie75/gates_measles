import numpy as np
rng=np.random.default_rng()

x=np.array([1,2,3])
y=np.array([3,4,5])
z=np.stack((x,y,y),axis=1)
w=z.sum(axis=1)
print(z)
print(w)
a=z/w[...,None]
print(a)
print(a[1,:])