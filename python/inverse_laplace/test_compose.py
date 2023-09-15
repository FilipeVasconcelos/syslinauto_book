# ====================================================================== 
# second ordre
def SO(p,**kwargs):
    K=kwargs.get('K', 1.0)
    w=kwargs.get('w', 1.0)
    z=kwargs.get('z', 1.0)
    """
    système du 2nd ordre
    K : gain
    w : pulsation propre
    z : coefficient d'amortissement
    """
    return (K*w**2)/(p**2+2*z*w*p+w**2)
# ====================================================================== 
# premier ordre
def PO(p,**kwargs):
    K=kwargs.get('K', 1.0)
    tau=kwargs.get('tau', 1.0)
    """
    système du 1er ordre
    K : gain
    tau : constante de temps
    """
    return K/(tau*p+1)


def test(p,**kwargs):

    COp=0.0
    P1er=kwargs.get('P1er', [])
    P2nd=kwargs.get('P2nd', [])

    # premier ordre
    for k in range(len(P1er)):
        K=kwargs['P1er'][k][0]
        tau=kwargs['P1er'][k][1]
        print("K=",K)
        print("tau=",tau)
        COp*=PO(p,K=K,tau=tau)
    # second ordre
    for k in range(len(P2nd)):
        K=kwargs['P2nd'][k][0]
        w=kwargs['P2nd'][k][1]
        z=kwargs['P2nd'][k][2]
        print("K=",K)
        print("w=",w)
        print("z=",z)
        COp*=SO(p,K=K,w=w,z=z)
    #for k,v in kwargs.items():
    #    print(k,v)

if __name__ == "__main__":

    test(1.0,P1er=[[1.0,1.0],[2.0,0.1]],P2nd=[[1.0,1.0,0.5]])
