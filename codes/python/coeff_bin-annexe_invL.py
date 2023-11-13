def coeff_bin(n,k):
    """
    Coefficients binomiaux :
         k          n!
       C     = -------------
        n       k! (n-k)!
    """
    a=m.factorial(n)
    b=m.factorial(k)
    c=m.factorial(n-k)
    return a/(b*c)
