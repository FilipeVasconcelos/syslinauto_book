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
