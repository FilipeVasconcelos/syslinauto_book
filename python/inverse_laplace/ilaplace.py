#coding : utf-8
import sys
import numpy as np
import math as m
import matplotlib.pyplot as plt
# ====================================================================== 
# coefficient binomiaux
#
#    k         n!
#   C   = -------------
#    n      k! (n-k)!
#
# ====================================================================== 
def coeff_bin(n,k):
    a=m.factorial(n)
    b=m.factorial(k)
    c=m.factorial(n-k)
    return a/(b*c)
# ====================================================================== 
# méthode de "Stehfest"
# https://fr.wikipedia.org/wiki/Transformation_inverse_de_Laplace
# ====================================================================== 
def v_stehfest(N):
    """
    equation (32) de http://www.columbia.edu/~ww2040/JoC.pdf
    """
    if N%2 !=0 : 
        return
    else : 
        M=N//2
    vs=[]
    for k in range(1,2*M+1):
        coeff=(-1)**(M+k)/m.factorial(M)
        vs.append(coeff)
        jmi=(k+1)//2
        jma=min(k,M)
        sumk=0.0
        for j in range(jmi,jma+1):
            a=j**(M+1)
            c=coeff_bin(M,j)
            d=coeff_bin(2*j,j)
            e=coeff_bin(j,k-j)
            sumk+=a*c*d*e
        vs[-1]*=sumk
    return vs

def gaver_stehfest(t,f,N=16):
    """ 
    (equation 31) JcO.pdf
    """
    c=np.log(2)/t
    sumk=0.0
    for k,v in enumerate(v_stehfest(N)):
        sumk+=v*f((k+1)*c) 
    return c*sumk

def talbot(t,f,N=16):
    """ 
    (equation 18) abate2004.pdf
    """
    r=2.0*N/(5.0*t)
    sumk=0.5*f(r)*np.exp(r*t)
    step=np.pi/N
    for k in range(1,N):
        tk=k*step
        cotk=1.0/np.tan(tk)
        stk=r*tk*(cotk+1j)
        sigtk=tk+(tk*cotk-1)*cotk
        sumk_tmp=f(stk)*(1+1j*sigtk)*np.exp(t*stk)
        sumk+=sumk_tmp.real # real part
    return sumk*r/N

def ilaplace(t,f,method='talbot',N=16):
    if method=='talbot':
        return talbot(t,f,N)
    else:
        return gaver_stehfest(t,f,N)
# ====================================================================== 
if __name__=="__main__":
    fp = lambda p: 1/(p+1)**2
    ft = lambda t: t*exp(-t)
    for t in [0.001,0.01,0.1,1,10]:
        print(ilaplace(t,fp,method="talbot"))
