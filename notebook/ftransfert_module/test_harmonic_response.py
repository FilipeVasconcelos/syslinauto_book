if __name__ == "__main__":  
    import matplotlib.pyplot as plt
    import numpy as np
    from ftransfert import Ftransfert
    import sys

    #H_0
    do_H0=True
    do_H1=False
    do_H2=False
    do_H3=False
    if do_H0 :
        gain=1
        num=lambda p : 1
        den=lambda p : 1+p
        HBO=Ftransfert(num=num,den=den,gain=gain,name="H_{BO}",DPI=200)
        den=lambda p : p+2
        HBF=Ftransfert(num=num,den=den,gain=gain,name="H_{BF}",DPI=200)
        HBO.nyquist(complet=False,mcircles=True,ncircles=False,xlim=(-0.5,1.25),ylim=(-1,1),n=1024,color="tab:green",arrow_pcts=[0.45],savefig='nyquist_hbo_m-cercles.eps')
        HBO.nyquist(complet=False,mcircles=False,ncircles=True,xlim=(-0.5,1.25),ylim=(-1,0.25),n=1024,color="tab:green",arrow_pcts=[0.35])
        HBO.bode(y1lim=(-35,10),y2lim=(-90,0),n=1024,color="tab:green")
        HBF.bode(y1lim=(-35,10),y2lim=(-90,0),n=1024,color="tab:green")
        w=np.array([0.0,1.0,2,3])*1j
        HBF.tabLaTeX(ws=w)
        plt.show()  
    if do_H1 :
        #gain=1
        #num=lambda p : 1
        #den=lambda p : p*(2*p+1)*(p+1)
        #H1=Ftransfert(num=num,den=den,gain=gain,name="H_1")
        gain=1.0
        zeros=[]
        poles=[(-1,0),(-2,1),(-2,-1)]
        H1=Ftransfert(zeros=zeros,poles=poles,gain=gain,name="H_1",DPI=100)
        H1.nyquist(complet=True,xlim=(-0.5,0.5),ylim=(-0.5,0.5),n=2048,color="tab:green")
        H1.black(nichols=True,xlim=(-270,0),ylim=(-60,0),n=2048,color="tab:green")
        H1.bode(xlim=(1e-2,1e2),y2lim=(-270,0),y1lim=(-60,0),n=2048,color="tab:green",fmax=1e4)
        plt.show()     
    if do_H2 :
        gain=1  
        num=lambda p: p**2-5*p+2
        den=lambda p:p*(p**3+2*p**2+2*p+10)
        H2=Ftransfert(num=num,den=den,gain=gain,name="H_2")
        H2.black(nichols=True,xlim=(-360,0),ylim=(-60,40),arrow_pcts=[0.15,0.4],n=1024,color="tab:green")
        H2.bode(xlim=(1e-2,1e2),y1lim=(-80,40),y2lim=(-270,-90),n=1024,color="tab:green")
        plt.show()    
    # effet du retard Padé
    if do_H3 :
        tR=3
        gain=1  
        #num=lambda p: (1-tR*p*0.5+0.1*tR*tR*p*p-tR*tR*tR*p*p*p*0.008333333333333333)/(1+tR*p*0.5+0.1*tR*tR*p*p+tR*tR*tR*p*p*p*0.008333333333333333)
        num=lambda p: (p**4 - 6.667*p**3 + 20*p**2 - 31.11*p + 20.74)/(p**4 + 6.667*p**3 + 20*p**2 + 31.11*p + 20.74)
        den=lambda p: p+1
        H3=Ftransfert(num=num,den=den,gain=gain,name="H_3")
        H3.nyquist(complet=True,xlim=(-3.5,1),ylim=(-10,10),n=2**16,fmax=1e4,color="tab:green")
        plt.show()     

