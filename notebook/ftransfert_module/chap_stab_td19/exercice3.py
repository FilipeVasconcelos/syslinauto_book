if __name__ == "__main__":  
    import sys
    import matplotlib.pyplot as plt
    import numpy as np
    sys.path.append('/home/filipe/enseignement/sma_auto/notebook/ftransfert_module')
    from ftransfert import Ftransfert

    DPI=200
    gain=1
    gain=0.14
    #[-0.4942 0.7679 -0.6074 -0.7573 0.0874]
    num=lambda p : -0.4942*p**4 + 0.7679*p**3 - 0.6074*p**2 - 0.7573*p**1 + 0.0874   
    #[ 0.3146 0.3820  0.7915  0.8392 0.6802    0.4169]
    den=lambda p :  0.3146*p**5 + 0.3820*p**4 + 0.7915*p**3 + 0.8392*p**2 + 0.6802*p**1 + 0.4169 
    H1=Ftransfert(num=num,den=den,gain=gain,name="H_{BO}",title=None)
    H1.nyquist(complet=True,mcircles=False,ncircles=False,
    #           xlim=(-10,0.5),ylim=(-2,2), #K=1
               xlim=(-1.5,0.08),ylim=(-0.3,0.3),  #K=0.14
               n=4096,color="tab:blue",arrow_pcts=[0.52,0.531,0.536,0.54,0.546,0.555],
               savefig='exercice3.eps',dpi=DPI)
