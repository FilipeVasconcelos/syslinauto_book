import numpy as np
import matplotlib.pyplot as plt
from laplace_inverse_num import ilaplace,SO_ana,abc_to_Kwz


def function_p(p,**kwargs):
    #return (p+100)/((p+10)*(p+1)**4*(p**2+2*p+4))
    return 1.0/(p**2+0.75*p+1)

if __name__=="__main__":

    t=[]
    y=[]
    T=40
    dt=0.002
    npoints=int(T/dt)
    K,w,z=abc_to_Kwz(1.0,1.0,0.75,1.0)
    print(K,w,z)

    for i in range(1,npoints):
        t.append(i*dt)
        y_2=SO_ana(i*dt,'step',K=K,w=w,z=z)
        y_=ilaplace(i*dt,32,[],'step','talbot',H=function_p,K=K,w=w,z=z)
        y.append((y_,y_2,y_-y_2))

    plt.plot(t,y)
    plt.show()
