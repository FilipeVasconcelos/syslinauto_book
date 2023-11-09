def premier_ordre(t,name="step",**kwargs):
    K=kwargs.get('K', 1.0)
    tau=kwargs.get('tau', 1.0)
    a=np.exp(-t/tau)
    return K*(1-a)
