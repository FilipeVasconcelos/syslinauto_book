if __name__ == "__main__":  
    import sys
    import matplotlib.pyplot as plt
    import numpy as np
    sys.path.append('/home/filipe/enseignement/sma_auto/notebook/ftransfert_module')
    from ftransfert import Ftransfert

    DPI=200
    gain=1
    num=lambda p : p+3
    den=lambda p : (p+2)*(p*p+2*p+25)
    H1=Ftransfert(num=num,den=den,gain=gain,name="H_1",title='$H_1(p)$')
    H1.nyquist(complet=True,mcircles=False,ncircles=False,
               xlim=(-0.06,0.07),ylim=(-0.13,0.13),
               n=2048,color="tab:blue",arrow_pcts=[0.61,0.619,0.64],
               savefig='chap_stab_h1.eps',dpi=DPI)
