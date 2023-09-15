#!/usr/bin/env python
import numpy as np
import math as m
import argparse
# ------------------------------------------------------------------------------
# analytical impulse response of a second ordre system
def imp(K,xi,w0,t):
    if xi > 1 :
        p1=-xi*w0+w0*np.sqrt(xi*xi-1)
        p2=-xi*w0-w0*np.sqrt(xi*xi-1)
        return K*w0*w0/(p1-p2)*(np.exp(p1*t)-np.exp(p2*t))
    elif xi == 1 :
        return K*w0*w0*t*np.exp(-t*w0)
    elif xi < 1 :
        b=(1-xi**2)**0.5
        wd=w0*b
        return K*w0*(1/b)*np.exp(-xi*w0*t)*np.sin(t*wd)
# ------------------------------------------------------------------------------
# analytical step response of a second ordre system
def step(K,xi,w0,t):
    if xi > 1 :
        p1=-xi*w0+w0*np.sqrt(xi*xi-1)
        p2=-xi*w0-w0*np.sqrt(xi*xi-1)
    #    print(f"p1 {p1} p2 {p2}")
    #    print(p2*np.exp(p1*t)-p1*np.exp(p2*t))
        return K*(1+(1/(p1-p2))*(p2*np.exp(p1*t)-p1*np.exp(p2*t)))
    elif xi == 1 :
        p1=-w0
        return K*(1-np.exp(p1*t)+p1*t*np.exp(p1*t))
    elif xi < 1 :
        b=(1-xi**2)**0.5
        wd=w0*b
        p=np.arctan2(b,xi)
        return K*(1-(1/b)*np.exp(-xi*w0*t)*np.sin(t*wd+p))

# write data to file tmp.data 
def data(basename,K,xi,w0,ktmax=5,response="step"):
    if xi < 1 :
        b=(1-xi**2)**0.5
        wd=w0*b
        tmax=ktmax*np.pi/wd
    elif xi >= 1 :
        tmax = 4*ktmax/w0
    ts=np.linspace(0,tmax,256)
    if response=="step":
        y=step(K,xi,w0,ts)
    else:
        y=imp(K,xi,w0,ts)
    with open(basename+'.dat','w') as f:
        f.write("t response\n")
        for k,t in enumerate(ts):
            f.write(str(t)+" "+str(y[k])+'\n')

def gentex(basename):
    with open(basename+'.tex','w') as f:
        f.write("\\begin{tikzpicture}\n")
        f.write("""     \\begin{axis}
    [   
            width=0.65\\textwidth,
            axis lines=middle,
            axis line style = {-latex,thick},
            axis x line=center,
            axis y line=center,
            xlabel=$t$,
            ylabel=$s(t)$,
    ]\n""")
        f.write("   \\addplot[signalb] table[x=t,y=response] {"+basename+".dat};\n")
        f.write("\\end{axis}\n")
        f.write("\\end{tikzpicture}\n")

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("basename", help="basename.tex basename.dat",type=str)
    parser.add_argument("K", help="gain",type=float)
    parser.add_argument("xi", help="amortissement",type=float)
    parser.add_argument("w0", help="pulsation propre",type=float)
    parser.add_argument("resp", help="response : imp/step",type=str)
    parser.add_argument("ktmax", help="coefficient tmax: (default : 5)",type=int)
    args = parser.parse_args()
    basename=args.basename
    K=args.K
    xi=args.xi
    w0=args.w0
    resp=args.resp
    ktmax=args.ktmax
    data(basename,K,xi,w0,ktmax=ktmax,response=resp)
    gentex(basename)
