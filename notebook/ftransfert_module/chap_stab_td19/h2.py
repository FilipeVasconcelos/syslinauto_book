if __name__ == "__main__":  
    import sys
    import matplotlib.pyplot as plt
    import numpy as np
    sys.path.append('/home/filipe/enseignement/sma_auto/notebook/ftransfert_module')
    from ftransfert import Ftransfert

    DPI=200
    gain=1
    num=lambda p : 500*(p-2)
    den=lambda p : (p+2)*(p+7)*(p+50)
    H1=Ftransfert(num=num,den=den,gain=gain,name="H_2",title='$H_2(p)$')
    H1.nyquist(complet=True,mcircles=False,ncircles=False,
               xlim=(-1.5,1.5),ylim=(-1.5,1.5),
               n=2048,color="tab:blue",arrow_pcts=[0.52,0.55,0.59,0.67],
               savefig='chap_stab_h2.eps',dpi=DPI)
