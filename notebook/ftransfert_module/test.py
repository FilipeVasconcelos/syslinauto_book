if __name__ == "__main__":  
    import numpy as np
    import matplotlib.pyplot as plt
    from contour import add_arrow
    from ftransfert import Ftransfert
    import sys

    gain=2.2
    num=lambda p : p-1
    den=lambda p : p**3+p**2-p+2 
    H0=Ftransfert(num=num,den=den,gain=gain,title="$H_3(p)$ $K=2.2$",name='H_3',DPI=200)
    H0.nyquist(complet=False,xlim=(-1.7,0),ylim=(-0.6,0.6),n=2048,color="tab:blue",arrow_pcts=[0.535])
    plt.show()
