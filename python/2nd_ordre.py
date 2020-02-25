import numpy as np

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
    pas_t=0.05
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


def temps_de_montee(xis,ts):
    tm=[]
    for xi in xis :
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
    return tm

def temps_de_pic(xis,ts):
    tp=[]
    for xi in xis :
        smax=-10
        k=0
        s=second(ts[k],1,xi)
        #print(k,s,smax)
        while s >= smax and k < len(ts)-1 :
            smax = s
            k+=1
            s=second(ts[k],1,xi)
        #    print(k,s,smax)
        tp.append(ts[k])
    return tp


if __name__=="__main__":
    

    xis=np.linspace(0.1,1,10)
    ts=np.linspace(0,100,1024)
    tracer_reponses(xis,ts)
    print("reponses temporelles : all.tab")
    
    xim=np.linspace(0.01,10,2048)
    ts=np.linspace(0,100,2048)
    tm=temps_de_montee(xim,ts)
    f=open("tm.tab","w")
    for xi,t in zip(xim,tm):
        f.write(str(xi)+' '+str(t)+'\n')
    f.close()
    print("temps de montee done : tm.tab")

    xip=np.linspace(0.01,1,2048)
    ts=np.linspace(0,100,2048)
    tp=temps_de_pic(xip,ts)
    print("temps de pic done : tp.tab")
    f=open("tp.tab","w")
    for xi,t in zip(xip,tp):
        f.write(str(xi)+' '+str(t)+'\n')
    f.close()

    xir,tr=temps_de_reponse()
    print("temps de reponse à 5% done : tr.tab")
    f=open("tr.tab","w")
    for xi,t in zip(xir,tr):
        f.write(str(xi)+' '+str(t)+'\n')
    f.close()



