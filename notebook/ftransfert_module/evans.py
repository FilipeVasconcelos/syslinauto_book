import sys
import numpy as np
from numpy.polynomial import polynomial as nppol
import matplotlib.pyplot as plt
points=[[],[],[]]
ncoeff=4
npoints=512
coeffs=np.zeros((npoints,ncoeff))+[0,8,6,1]
coeffs[:,0]=np.linspace(0,100,npoints)
for p in coeffs:
    for k,r in enumerate(sorted(nppol.polyroots(p))):
        #r.sort()
        print(r)
        points[k].append((r.real,r.imag))
#for k in np.linspace(0,50,npoints):
#    coeffs[
#    print(np.roots([1,6,8,k]))
#    sys.exit()
#    for r in np.roots([1,6,8,k]):
#        if r.real < 0 :
#            print(r)
#            #points.append()
colors=['red','blue','green']
for k in range(ncoeff-1):
    x,y=zip(*points[k])
    plt.scatter(x,y,s=1,color=colors[k])
plt.show()
