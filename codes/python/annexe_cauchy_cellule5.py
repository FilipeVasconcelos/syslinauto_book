C1=rectangle((1,-1),(2,1),npts=64)
plot_contour(C1,xlim=(-2,3.5),ylim=(-1.5,1.5))
C1_inv=rectangle((1,-1),(2,1),npts=64,inverse=True)
plot_contour(C1_inv,xlim=(-2,3.5),ylim=(-1.5,1.5))
