if __name__ == "__main__":  
    import numpy as np
    import matplotlib.pyplot as plt
    from contour import add_arrow
    from ftransfert import Ftransfert
    import sys

    gain=2.0
    num=lambda p : 1 
    den=lambda p : p**2+p+1
    H0=Ftransfert(num=num,den=den,gain=gain,title="$H(p)$ $K=2$",name='H_1',DPI=150)
    H0.nyquist(complet=True,mcircles=True,ncircles=False,xlim=(-2,2),ylim=(-2,2),n=512,color="tab:red",arrow_pcts=[0.535])
    plt.show()
