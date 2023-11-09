# -------------------------------------------------------------------------------
# réponse indicielle d'un système du second ordre
# forme analytique pour la comparaison des résultats
# des méthodes numériques
# -------------------------------------------------------------------------------
def second_ordre(t,**kwargs):
    K=kwargs.get('K', 1.0)
    w=kwargs.get('w', 1.0)
    z=kwargs.get('z', 1.0)
    E0=kwargs.get('E0', 1.0)

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
        return K*E0*(1+(1.0/p1p2)*(p2*a1-p1*a2))
    if z == 1.0:
        p1=-w
        a1=np.exp(t*p1)
        return K*E0*(1-a1+p1*t*a1)
    if z < 1.0:
        b=np.sqrt(1-z*z)
        wd=w*b
        phi=np.arctan(b/z)
        a1=np.exp(-alpha*t)
        c=np.sin(wd*t+phi)
        return K*E0*(1-a1*c/b)
