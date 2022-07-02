if __name__ == "__main__":  
    import matplotlib.pyplot as plt
    import numpy as np
    from ftransfert import Ftransfert
    import sys

    DPI=100
    gain=1
    num=lambda p : 1
    den=lambda p : 1+p
    HBO=Ftransfert(num=num,den=den,gain=gain,name="H_{BO}")
    den=lambda p : p+2
    HBF=Ftransfert(num=num,den=den,gain=gain,name="H_{BF}")
    HBO.bode(y1lim=(-35,10),y2lim=(-90,0),n=1024,color="tab:green",savefig='bode_hbo.eps',dpi=DPI)
    HBF.bode(y1lim=(-35,10),y2lim=(-90,0),n=1024,color="tab:green",savefig='bode_hbf.eps',dpi=DPI)
    HBO.nyquist(complet=False,mcircles=True,ncircles=False,xlim=(-0.5,1.25),ylim=(-1,1),n=1024,color="tab:green",arrow_pcts=[0.45],savefig='nyquist_hbo_m-cercles.eps',dpi=DPI)
    HBO.nyquist(complet=False,mcircles=False,ncircles=True,xlim=(-0.5,1.25),ylim=(-1,0.25),n=1024,color="tab:green",arrow_pcts=[0.35],savefig='nyquist_hbo_n-cercles.eps',dpi=DPI)
    HBO.black(xlim=(-90,0),ylim=(-35,5),nichols=True,savefig='blackNichols_hbo.eps',color="tab:green",n=1024,dpi=DPI)
    w=np.array([0.0,1.0,2,3])*1j
    HBF.tabLaTeX(ws=w)
