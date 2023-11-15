def gaver_stehfest(t,f,N=16):
    """
    Méthode de Gaver-Stehfest
    (equation 31) JcO.pdf
    """
    if N%2 !=0 :
        print("Error N should be even")
        return
    c=m.log(2)/t
    return c*sum([zeta*f((k+1)*c) for k,zetav in enumerate(zeta_stehfest(N))])
