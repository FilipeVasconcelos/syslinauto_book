def premier_ordre(t,**kwargs):
    """
    Réponse indicielle d'un système du premier ordre :
        s(t) = K E0 ( 1 - exp(-t/tau)
    """
    K=kwargs.get('K', 1.0)
    tau=kwargs.get('tau', 1.0)
    E0=kwargs.get('E0', 1.0)
    return K*E0*(1-np.exp(-t/tau))
