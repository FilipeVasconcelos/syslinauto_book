def zeta_stehfest(N):
    """
    Coefficients zeta de la relation (32) de 
    http://www.columbia.edu/~ww2040/JoC.pdf
    """
    if N%2 !=0 :
        return
    else :
        M=N//2
    zetas=[]
    for k in range(1,2*M+1):
        coeff=(-1)**(M+k)/m.factorial(M)
        zetass.append(coeff)
        jmi=(k+1)//2
        jma=min(k,M)
        zetak=0.0
        for j in range(jmi,jma+1):
            a=j**(M+1)
            c=coeff_bin(M,j)
            d=coeff_bin(2*j,j)
            e=coeff_bin(j,k-j)
            zetak+=a*c*d*e
        zetas[-1]*=zetak
    return zeta
