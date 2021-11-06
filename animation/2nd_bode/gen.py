import sys
sys.path.insert(0, '/home/filipe/enseignement/sma_auto/notebook/ftransfert_module/')
from ftransfert import Ftransfert
import numpy as np



import matplotlib.pyplot as plt
k=1

for xi in np.arange(0.1,1.0,0.01):
    gain=1    
    num=lambda p : 1
    den=lambda p : 1+2*xi*p+p**2
    H_bo=Ftransfert(num=num,den=den,gain=gain,name="$\\xi="+f'{xi:.2f}$',DPI=250,verbeux=0)
    fig=H_bo.bode(n=1024,y1lim=(-80,20),y2lim=(-180,0),color="tab:green",arrow_pcts=[0.3])
    #plt.title("$\\xi="+f'{xi:.2f}$',loc='left')
    fname='2nd_bode_files/2nd_bode_'+str(k)+'.png'
    print(xi,fname)
    plt.savefig(fname,transparent=True)
    plt.close(fig)
    k+=1
for xi in np.arange(1.0,0.1,-0.01):
    gain=1    
    num=lambda p : 1
    den=lambda p : 1+2*xi*p+p**2
    H_bo=Ftransfert(num=num,den=den,gain=gain,name="$\\xi="+f'{xi:.2f}$',DPI=250,verbeux=0)
    fig=H_bo.bode(n=1024,y1lim=(-80,20),y2lim=(-180,0),color="tab:green",arrow_pcts=[0.3])
    fname='2nd_bode_files/2nd_bode_'+str(k)+'.png'
    print(xi,fname)
    plt.savefig(fname,transparent=True)
    plt.close(fig)
    k+=1

    #plt.show(block=False)
