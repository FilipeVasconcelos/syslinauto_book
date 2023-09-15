#coding : utf-8
import sys
import numpy as np
import math as m
import matplotlib.pyplot as plt
import random
# ====================================================================== 
# petit outils pour convertir des fonctions de transferts 
# du second ordre de la forme Aabc -> Kwz
# cad :
#         A                   Kw^2
#    -----------   ->    ------------- 
#     ap^2+bp+c           p^2+2zwp+w^2 
# ====================================================================== 
def abc_to_Kwz(A,a,b,c):
    K=A/c
    w=np.sqrt(c/a)
    z=b/(2*np.sqrt(a*c))
    return K,w,z
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
# ====================================================================== 
# Fonction de transfert du premier ordre  
# (dans le domaine de Laplace)
# ====================================================================== 
def PO(p,**kwargs):
    K=kwargs.get('K', 1.0)
    tau=kwargs.get('tau', 1.0)
    """
    système du 1er ordre
    K : gain
    tau : constante de temps

               K
          ------------
           tau p + 1
    """
    return K/(tau*p+1)
# ====================================================================== 
# Fonction de transfert du premier ordre  
# (dans le domaine temporelle)
# forme analytique pour la comparaison des résultats 
# des méthodes numériques
# ====================================================================== 
def PO_ana(t,name="step",**kwargs):
    K=kwargs.get('K', 1.0)
    tau=kwargs.get('tau', 1.0)
    a=np.exp(-t/tau)
    if name=="impu" :
        return K*a/tau
    if name=="step" :
        return K*(1-a)
    if name=="ramp" :
        return K*(t-tau*(1-a))
# ====================================================================== 
# Fonction de transfert du second ordre  
# (dans le domaine de Laplace)
# ====================================================================== 
def SO(p,**kwargs):
    K=kwargs.get('K', 1.0)
    w=kwargs.get('w', 1.0)
    z=kwargs.get('z', 1.0)
    """
    Système du 2nd ordre
    K : gain
    w : pulsation propre
    z : coefficient d'amortissement

                K w^2
         ----------------------
          p^2 + 2 z w p + w^2 
    """
    return (K*w**2)/(p**2+2*z*w*p+w**2)
# ====================================================================== 
# Fonction de transfert du second ordre  
# (dans le domaine temporelle)
# forme analytique pour la comparaison des résultats 
# des méthodes numériques
# ====================================================================== 
def SO_ana(t,name="step",**kwargs):
    K=kwargs.get('K', 1.0)
    w=kwargs.get('w', 1.0)
    z=kwargs.get('z', 1.0)

    if z <= 0.0 :
        return
    else:
        alpha = z*w
    if z > 1.0 :
        b=np.sqrt(z*z-1)
        wd=w*b
        p1=-alpha+wd
        p2=-alpha-wd
        a1=np.exp(t*p1)
        a2=np.exp(t*p2)
        p1p2=p1-p2
    if z == 1.0:
        p1=-w
        a1=np.exp(t*p1)
    if z < 1.0:
        b=np.sqrt(1-z*z)
        wd=w*b
        phi=np.arctan(b/z)
        a1=np.exp(-alpha*t)
    
    if name=="impu" :
        if z > 1.0 :
            return K*w*w*(a1-a2)/p1p2
        if z == 1.0 :
            return K*w*w*t*np.exp(p1*t)
        if z < 1.0 :
            a=a1/(b*b)
            c=np.sin(wd*t)
            return K*wd*a*c
    if name=="step" :
        if z > 1.0 :
            return K*(1+(1.0/p1p2)*(p2*a1-p1*a2))
        if z == 1.0 :
            return K*(1-a1+p1*t*a1)
        if z < 1.0 :
            c=np.sin(wd*t+phi)
            return K*(1-a1*c/b)
    if name=="ramp" :
        if z > 1.0 :
            return K*(t+((p1+p2)/(w*w))+(1.0/(p1p2*w*w))*(p2*p2*a1-p1*p1*a2))
        if z == 1.0 :
            return K*((2.0/p1)+t-(2.0/p1)*a1+t*a1)
        if z < 1.0 :
            c=np.sin(wd*t+2*phi)
            return K*(t-((2*z)/w)+((2*z)/wd)*a1*c)
# ====================================================================== 
# Fonction de transfert par composition de 
# plusieurs systèmes du premier et du second ordre
# ====================================================================== 
def CO(p,**kwargs):
    COp=1.0
    P1er=kwargs.get('P1er', [])
    P2nd=kwargs.get('P2nd', [])
    # somme sur les premiers ordres
    for k in range(len(P1er)):
        K=kwargs['P1er'][k][0]
        tau=kwargs['P1er'][k][1]
        COp*=PO(p,K=K,tau=tau)
    # somme sur les seconds ordres
    for k in range(len(P2nd)):
        K=kwargs['P2nd'][k][0]
        w=kwargs['P2nd'][k][1]
        z=kwargs['P2nd'][k][2]
        COp*=SO(p,K=K,w=w,z=z)
    return COp
# ====================================================================== 
# Fonction de transfert de l'entrée
# dans le domaine de Laplace 
# ====================================================================== 
def E(p,name,E0):
    if name == "step":
        return E0/p
    elif name == "impu":
        return E0
    elif name == "ramp":
        return E0/(p*p)
# ====================================================================== 
# laplace inverse by Gaver-Stehfest or Fixed Talbot
# ====================================================================== 
def ilaplace(t,N,vs,name='step',method="stehfest",E0=1,H=SO,**kwargs):
    if method == "stehfest" :
        """ 
        (equation 31) JcO.pdf
        """
        c=np.log(2)/t
        sumk=0.0
        for k,v in enumerate(vs):
            sumk+=v*H((k+1)*c,**kwargs)*E((k+1)*c,name,E0) 
        return c*sumk
    if method == "talbot":
        """ 
        (equation 18) abate2004.pdf
        """
        r=2.0*N/(5.0*t)
        sumk=0.5*H(r,**kwargs)*E(r,name,E0)*np.exp(r*t)
        step=np.pi/N
        for k in range(1,N):
            tk=k*step
            cotk=1.0/np.tan(tk)
            stk=r*tk*(cotk+1j)
            sigtk=tk+(tk*cotk-1)*cotk
            fp=H(stk,**kwargs)*E(stk,name,E0)
            sumk_tmp=fp*(1+1j*sigtk)*np.exp(t*stk)
            sumk+=sumk_tmp.real # real part
        return sumk*r/N
# ====================================================================== 
if __name__=="__main__":
    sep=60*"="
    print(sep)
    N=16 # coefficients de Stehfest
    vs=v_stehfest(N)
    sumvs=0.0
    print("nombre de coefficients (précision) de la méthode (Stehfest) : ", N)
    for k,v in enumerate(vs):
        sumvs+=v
        print(k,v)
    print("Somme des coeffs:",sumvs)
    t=[]
    y_ana={}
    y_num={}
    y_err={}
    #methods=["stehfest","talbot"]
    #entree=["impu","step","ramp"]
    #systems=["PO","SO"]
    methods=["stehfest","talbot"]
    entree=["impu"]
    systems=["SO"]
    N_methods={"stehfest":N,"talbot":N}
    fana={"PO":PO_ana,"SO":SO_ana}
    fnum={"PO":PO,"SO":SO}
    for s in systems :
        for e in entree :
            key_se=s+"+"+e
            y_ana[key_se]=[]
            for m in methods :
                key=s+"+"+e+"+"+m
                y_num[key]=[]
                y_err[key]=[]
    # ----------------------------------------------------
    # temps finale
    # ----------------------------------------------------
    T=50   
    # ----------------------------------------------------
    # pas de temps
    # ----------------------------------------------------
    dt=0.0005
    # ----------------------------------------------------
    # nombre de points de la fonction temporelle
    # ----------------------------------------------------
    npoints=int(T/dt) 
    # ----------------------------------------------------
    # paramètres des systèmes 
    # ----------------------------------------------------
    #K,w,z=abc_to_Kwz(1,2,3,4)
    # second ordre
    K,w,z=1.0,1.0,0.1
    # premier ordre
    tau=1.0
    # ----------------------------------------------------
    # boucle temps 
    # ----------------------------------------------------
    for i in range(1,npoints):
        t.append(i*dt)
        for s in systems :
            for e in entree :
                key_se=s+"+"+e
                # ------------------------
                # PO_ana ou SO_ana
                # ------------------------
                yana=fana[s](i*dt,e,K=K,w=w,z=z)
                # ------------------------
                # store
                # ------------------------
                y_ana[key_se].append(yana)
                for m in methods :
                    key=s+"+"+e+"+"+m
                    ynum=ilaplace(i*dt,N_methods[m],vs,e,m,H=fnum[s],K=K,w=w,z=z)
                    yerr=yana-ynum
                    y_num[key].append(ynum)
                    y_err[key].append(yerr)
    # ------------------------
    # plots
    # ------------------------
    plt.rc('text', usetex=True)
    for s in systems :
        for e in entree :
            key_se=s+"+"+e
            for m in methods :
                key=s+"+"+e+"+"+m
                print(key)
                plt.title(key)
                plt.xlabel(r'$t$')
                plt.ylabel(r'$y(t)$')
                plt.plot(t,y_ana[key_se])
                plt.plot(t,y_num[key])
                plt.show()
                plt.title(key+" Erreur")
                plt.xlabel(r'$t$')
                plt.ylabel(r'$\epsilon=y_{ana}(t)-y_{num}(t)$')
                plt.plot(t,y_err[key])
                plt.show()
    sys.exit()
    # ----------------------------------------------------
    # Composition de systèmes du premier et second ordre 
    # ----------------------------------------------------
    dt=0.02
    npoints=2**14
    x=[]
    y_num=[]
    for i in range(1,npoints):
        t=i*dt
        #y_numeric = ilaplace(t,N,'step',H=CO,P1er=[(1.0,0.1),(2.0,0.01),(1.5,0.05)],P2nd=[(1.0,1.0,0.5),(0.5,0.5,1.5)])
        y_numeric = ilaplace(t,N,'step',H=CO,P2nd=[(10.0,0.1,0.2),(1.0,1.0,1.0)])
        y_num.append(y_numeric)
        x.append(t)
    plt.plot(x,y_num)
    plt.show()


