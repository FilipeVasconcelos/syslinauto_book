import numpy as np
import sys

def second(t,w0,xi):
    a=xi**2-1
    if xi > 1:
        sa=np.sqrt(a)
        r1=w0*(-xi+sa)
        r2=w0*(-xi-sa)
        return (1/(r1-r2))*(r1*(1-np.exp(r2*t))-r2*(1-np.exp(r1*t)))
    elif xi == 1 :
        return 1-(1+w0*t)*np.exp(-w0*t)
    else :
        sa=np.sqrt(-a)
        wd=w0*sa
        phi=np.arctan(sa/xi)
        return 1-(1/sa)*np.exp(-xi*w0*t)*np.sin(wd*t+phi)

def tracer_reponses(xis,ts):
    f=open("all.tab","w")
    for xi in xis :
        for t in ts:
            s=second(t,1,xi)
            f.write(str(t)+" "+str(s)+"\n")
        f.write("\n")
        f.write("\n")
    f.close()

def dans_bande(v,x):
    if v>=1-x/100 and v<=1+x/100 :
        return True                                                                                               
    else:
        return False

def temps_de_reponse(xpct=5):

    pas_xi=0.01
    pas_t=0.01
    omega=1.0
    xis=[]
    twos=[]

    #z<0.6
    #On teste la sortie de bande en partant d'une valeur de t suffisamment grande.
    #Le temps de réponse réduit étant décroissant, on peut à chaque itération de xi,
    #repartir avec la dernière valeur de t déterminée.

    t=400
    xi=0.01
    while xi<0.6:
#        print(xi)
        while dans_bande(second(t,omega,xi),xpct) :
            t-=pas_t

        t+=pas_t
        xis.append(xi)
        twos.append(omega*t)
        xi+=pas_xi


    #xi>0.6 et xi<=1
    #On teste la sortie de bande en partant d'une valeur de t suffisamment grande.
    #A chaque itération de xi, on prend t=7 comme valeur de départ.

    xi=0.6
    while xi<=1:
 #       print(xi)
        t=20 ;
        while dans_bande(second(t,omega,xi),xpct):
            t-=pas_t
        t+=pas_t
        xis.append(xi)
        twos.append(omega*t)
        xi+=pas_xi


    # xi>=1
    #On teste l'entrée de bande en partant d'une valeur de two suffisamment petite.
    #Le temps de réponse réduit étant croissant, on peut à chaque itération de xi,
    #repartir avec la dernière valeur de trwo déterminée.

    xi=1.0
    t=0
    while xi<50:
 #       print(xi)
        while not (dans_bande(second(t,omega,xi),xpct)) :
            t+=pas_t
        t-=pas_t
        xis.append(xi)
        twos.append(omega*t)
        xi+=pas_xi

    return xis,twos

def status(index,tab):
    n=len(tab)
    period=n/8
    pct=(index/n)*100
    if (index % period) != 0 : return  
    print('running : {0:04.1f}%'.format(pct))

def temps_de_montee(xis,ts):
    tm=[]
    period=0
    for xi in xis :
        status(period,xis)
        find10=False
        find90=False
        k=0
        while not find90 :
            s=second(ts[k],1,xi)
            if not find10 and s > 0.1 :
                t10=ts[k]
                find10=True
            if not find90 and s > 0.9 :
                t90=ts[k]
                find90=True
            k+=1
        tm.append(t90-t10)
        period+=1
    return tm

def temps_de_montee_vf(xis,ts):
    tm=[]
    period=0
    for xi in xis :
        status(period,xis)
        find=False
        k=0
        while not find and k<len(ts) :
            s=second(ts[k],1,xi)
            if 1.0-s < 1e-8 :
                t=ts[k]
                find=True
            k+=1
        tm.append(t)
        #print(xi,t)
        period+=1
    return tm


def temps_de_pic(xis,ts):
    tp=[]
    period=0
    for xi in xis :
        status(period,xis)
        smax=-10
        k=0
        s=second(ts[k],1,xi)
        while s >= smax and k < len(ts)-1 :
            smax = s
            k+=1
            s=second(ts[k],1,xi)
        tp.append(ts[k])
        period+=1
    return tp


if __name__=="__main__":
    

    xis=np.linspace(0.01,1,10)
    ts=np.linspace(0,1000,8192)
    tracer_reponses(xis,ts)
    print("reponses temporelles : all.tab")
    
    # Temps de montée entre 10%-90%
    if False :
        xim=np.linspace(0.01,10,4096)
        ts=np.linspace(0,400,4096)
        tm=temps_de_montee(xim,ts)
        f=open("tm.tab","w")
        for xi,t in zip(xim,tm):
            f.write(str(xi)+' '+str(t)+'\n')
        f.close()
        print("temps de montee done : tm.tab")

    # Temps de montée atteindre la valeur finale 
    if True :
        xim=np.linspace(0.01,1,4096)
        ts=np.linspace(0,1000,8192)
        tm=temps_de_montee_vf(xim,ts)
        f=open("tm_vf.tab","w")
        for xi,t in zip(xim,tm):
            f.write(str(xi)+' '+str(t)+'\n')
        f.close()
        print("temps de montee (vf) done : tm_vf.tab")

    # Temps de pic
    if False :
        xip=np.linspace(0.01,1,4096)
        ts=np.linspace(0,100,4096)
        tp=temps_de_pic(xip,ts)
        print("temps de pic done : tp.tab")
        f=open("tp.tab","w")
        for xi,t in zip(xip,tp):
            f.write(str(xi)+' '+str(t)+'\n')
        f.close()

    # Temps de reponse
    if False :
        xir,tr=temps_de_reponse()
        print("temps de reponse à 5% done : tr.tab")
        f=open("tr.tab","w")
        for xi,t in zip(xir,tr):
            f.write(str(xi)+' '+str(t)+'\n')
        f.close()



