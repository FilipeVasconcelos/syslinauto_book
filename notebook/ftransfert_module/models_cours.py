if __name__ == "__main__":  
    import numpy as np
    import matplotlib.pyplot as plt
    from contour import add_arrow
    from ftransfert import Ftransfert
    import sys

    do_Int=True
    do_Der=True
    do_1er=True
    do_2nd=True
    if do_Int :
        gain=1
        num=lambda p : 1
        den=lambda p : p 
        H0=Ftransfert(num=num,den=den,gain=gain,name="H_0",DPI=100)
        H0.black(xlim=(-360,0),ylim=(-20,20),n=2048,color="tab:green")
        plt.show()  
    if do_Der :
        gain=1.0
        num=lambda p : p 
        den=lambda p : 1 
        H1=Ftransfert(num=num,den=den,gain=gain,name="H_1",DPI=100)
        H1.black(xlim=(0,180),ylim=(-20,20),n=2048,color="tab:green")
        plt.show()     
    if do_1er :
        gain=1  
        num=lambda p: 1
        den=lambda p: p+1
        H2=Ftransfert(num=num,den=den,gain=gain,name="H_2")
        H2.black(xlim=(-180,0),ylim=(-80,20),fmax=1e4,arrow_pcts=[0.4],n=1024,color="tab:green")
        plt.show()     
    if do_2nd :
        colors=["tab:blue","tab:orange","tab:green","tab:cyan","tab:red"]
        start=0.1
        inc=0.05
        xi=start
        gain=1  
        num=lambda p: 1
        den=lambda p: p**2+2*xi*p+1 
        H3=Ftransfert(num=num,den=den,gain=gain,name="H_3")
        H3.black(xlim=(-270,0),ylim=(-80,20),n=1024,color=colors[0])
        k=1
        for xi in np.arange(start+inc,1.0,inc):
            gain=1  
            num=lambda p: 1
            den=lambda p: p**2+2*xi*p+1 
            H3=Ftransfert(num=num,den=den,gain=gain,name="H_3")
            XB,YB=H3.black(plot=False,xlim=(-270,0),ylim=(-80,20),n=1024,color="tab:green")
            line,=plt.plot(XB[0],YB[0],color=colors[k%len(colors)])
            add_arrow(line,pcts=[0.4],middle=True)
            k+=1
        plt.show()
