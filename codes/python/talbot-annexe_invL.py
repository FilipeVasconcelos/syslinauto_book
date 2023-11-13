def talbot(t,f,M=20):
    """
    Algorithme fixe de Talbot :
    (equation (18) abate2004.pdf
    """
    r=2.0*M/(5.0*t)
    sumk=0.5*f(r)*np.exp(r*t)
    step=np.pi/M
    for k in range(1,M):
        tk=k*step
        cotk=1.0/np.tan(tk)
        stk=r*tk*(cotk+1j)
        sigtk=tk+(tk*cotk-1)*cotk
        sumk_tmp=f(stk)*(1+1j*sigtk)*np.exp(t*stk)
        sumk+=sumk_tmp.real # real part
    return sumk*r/M
