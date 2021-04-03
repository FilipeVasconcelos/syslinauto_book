if __name__ == "__main__":  
    import matplotlib.pyplot as plt
    from ftransfert import Ftransfert
    import sys

    #H_0
    do_H0=False
    do_H1=False
    do_H2=True
    if do_H0 :
        gain=1
        num=lambda p : 1
        den=lambda p : 1+p
        H0=Ftransfert(num=num,den=den,gain=gain,name="H_0")
        H0.nyquist(complet=False,xlim=(-1.5,1.5),ylim=(-1,1),n=2048,color="tab:green")
        H0.black(nichols=True,xlim=(-180,0),ylim=(-30,10),n=2048,color="tab:green")
        H0.bode(n=2048,color="tab:green")
        plt.show()     
    if do_H1 :
        #gain=1
        #num=lambda p : 1
        #den=lambda p : p*(2*p+1)*(p+1)
        #H1=Ftransfert(num=num,den=den,gain=gain,name="H_1")
        gain=0.5
        zeros=[]
        poles=[(0,0),(-0.5,0),(-1,0)]
        H1=Ftransfert(zeros=zeros,poles=poles,gain=gain,name="H_1")
        H1.nyquist(complet=True,xlim=(-4,4),ylim=(-4,4),n=2048,color="tab:green")
        H1.black(nichols=True,xlim=(-360,0),ylim=(-80,40),n=2048,color="tab:green")
        H1.bode(xlim=(1e-2,1e2),y2lim=(-360,0),y1lim=(-80,40),n=2048,color="tab:green",fmax=1e4)
        plt.show()     
    if do_H2 :
        gain=1  
        num=lambda p: p**2-5*p+2
        den=lambda p:p*(p**3+2*p**2+2*p+10)
        H2=Ftransfert(num=num,den=den,gain=gain,name="H_2")
        H2.black(nichols=True,xlim=(-360,0),ylim=(-60,40),arrow_pcts=[0.15,0.4],n=1024,color="tab:green")
        H2.bode(xlim=(1e-2,1e2),y1lim=(-80,40),y2lim=(-270,-90),n=1024,color="tab:green")
        plt.show()     
