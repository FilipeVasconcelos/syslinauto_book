if __name__ == "__main__":  
    import numpy as np
    import matplotlib.pyplot as plt
    from contour import add_arrow
    from ftransfert import Ftransfert
    import sys

    gain=100
    num=lambda p : 1
    den=lambda p : (1+10*p)*(1+0.01*p) 
    H0=Ftransfert(num=num,den=den,gain=gain,title="$H_3(p)$ $K=2.2$",name='H_3')
    #H0.nyquist(complet=False,xlim=(-1.7,0),ylim=(-0.6,0.6),n=2048,color="tab:blue",arrow_pcts=[0.535])
    H0.bode(xlim=(1e-3,1e4),y1lim=(-120,60),y2lim=(-180,0),fmax=1e4)
    plt.show()
