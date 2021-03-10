import matplotlib.pyplot as plt
import numpy as np

from contour import rectangle,circle, add_arrow

class Ftransfert():
    """
    Fonction de transfert :
    """
    def __init__(self,zeros=None,poles=None,num=None,den=None,gain=1,name="F"):
        self.gain=gain
        self.num=num
        self.den=den
        self.name=name
        if zeros: 
            self.rzeros=zeros
            self.zeros=[complex(zero[0],zero[1]) for zero in zeros]
        else:
            self.rzeros=[]
            self.zeros=[]
        if poles: 
            self.rpoles=poles
            self.poles=[complex(pole[0],pole[1]) for pole in poles]
        else:
            self.rpoles=[]
            self.poles=[]
        defOK=(self.zeros!=[] or self.poles!=[]) or (self.num!=None and self.den!=None)
        if defOK:
            if self.num!=None or self.den!=None :
                self.type="function"
                self.zeros=[]
                self.poles=[]
            else:
                self.type="roots"
        else:
            self.type=None
            print('error in Transfert definition')

        if self.type == "function" :
            self.integrators= self.den(0.0) == 0.0
        else:
            if len(poles)>0 : self.integrators = not all(self.poles).real!=0
        
        #Nyquist plot
        self.XNyq=[]
        self.YNyq=[]
        
        #Cauchy plot
        self.Corigin=[]
        self.Cimage=[]
    # ------------------------------------------------------------------------------
    def __repr__(self):
        if self.type == "roots": 
            return f'Ftranfert(zeros={self.rzeros},poles={self.rpoles},gain={self.gain},name="{self.name}")'
        if self.type == "function":
            return f'Ftranfert(num={type(self.num)},den={type(self.den)},gain={self.gain},name="{self.name}")'
    # ------------------------------------------------------------------------------
    def __str__(self):
        """
                          (p-z1)(p-z2)(p-z3)...
            F(p) = gain  ------------------------
                          (p-p1)(p-p2)(p-p3)...
        """
        if self.type == "function": return "FT define with lambda functions" 
        def strc(c):
            # retourne si possible le string de la
            # valeure absolue du int de la partie 
            # réelle et imaginaire d'un complexe
            if c.real == int(c.real) :
                r=str(int(abs(c.real)))
            else:
                r=str(abs(c.real))
            if abs(c.imag) == 1.0 :
                return r,''
            if c.imag == int(c.imag) :
                i=str(int(abs(c.imag)))
            else:
                i=str(abs(c.imag))
            return r,i
        def strroot(roots):
            #retourne une chaine de caractères 
            # de toute les racines (poles et zeros)
            out=''
            for root in roots:
                r,i=strc(root)
                if root.real<0:
                    out+='(p+'+r
                else:
                    out+='(p-'+r
                if root.imag<0 :
                    out+='+'+i+'j'
                elif root.imag>0:
                    out+='-'+i+'j'
                out+=')'
            return out
        outz=strroot(self.zeros)
        outp=strroot(self.poles)
        outname=self.name+'(p) = '
        if len(outz) == 0 :
            outz=str(self.gain)
            outgain=''
        else:
            outgain= str(self.gain)+' ' if self.gain !=1 else ''

        lz,lp=len(outz),len(outp)
        diff=(lz-lp)//2
        if diff>0:
            dz,dp=0,diff
        else:
            dz,dp=-diff,0
        spacenum=len(outname)+len(outgain)+dz
        spaceden=len(outname)+len(outgain)+dp
        dashed=max(len(outz),len(outp))
        out='\n'
        if len(outp) !=0 :
            out+=spacenum*' '+outz+'\n'
            out+=outname+outgain+dashed*'-'+'\n'
        else:
            out+=outname+outgain+outz+'\n'
        out+=spaceden*' '+outp+'\n'
        return out

    def evaluate(self,p):
        """
        evaluate the transfert function according
        to his definition.
        if function : just return the evaluation of num and den 
        in p.
        if "roots"  : 

                                      (p-z1)(p-z2) ...
        return the evaluation of   K -------------------  
                                      (p-p1)(p-p2) ...
        """ 
        if self.type == "function":
            if abs(p) == 0.0 and self.integrators : return
            return self.gain*self.num(p)/self.den(p)
        elif self.type == "roots" :
            zz=complex(1,0)
            for zero in self.zeros:
                zz*=(p-zero)
            for pole in self.poles:
                zz/=(p-pole)
            zz*=self.gain
            return zz
        
    def nyquist(self,fig=None,replot=False,**kwargs):
        """
        Plot Nyquist chart for p= -∞ j -> +∞ j
        in practice from -dw*n/2 -> dw*n/2
        """
        xlim=kwargs.get('xlim', (-5,5))
        ylim=kwargs.get('ylim', (-5,5))
        dw=kwargs.get('dw',0.01)
        n=kwargs.get('n',10000)
        label=kwargs.get('label','')
        color=kwargs.get('color','tab:blue')
       
        print(60*'*')
        print("Nyquist plot : "+self.name+'(p)')
        print("Pulsation pas :",dw)
        print("Interval des pulsations",-dw*n/2,dw*n/2)
        print("Nombre de points",n)
        print(self)
        print(60*'*'+'\n')
        
        # evaluer F(p) pour p=-infty j -> +infty j
        for step in range(n):
            k=step-n//2
            om=k*dw
            h=self.evaluate(complex(0,om))
            self.XNyq.append(h.real)
            self.YNyq.append(h.imag)
            if k == 0 : zeroPulse=om
        inftyPulse=n-1
        
        # matplotlib instructions
        if not replot : fig = plt.figure(figsize=(6,4),dpi=100)
        ax = fig.add_subplot(1, 1, 1,label=label)
        ax.set(xlim=xlim, ylim=ylim)
        ax.title.set_text(r'Nyquist $'+self.name+'(p)$')
        ax.title.set_size(16)
        ax.xaxis.label.set_text(r'$\operatorname{Re}['+self.name+'(p)]$')
        ax.xaxis.label.set_size(12)
        ax.yaxis.label.set_text(r'$\operatorname{Im}['+self.name+'(p)]$')
        ax.yaxis.label.set_size(12)
        #plt.grid()
        line,=plt.plot(self.XNyq,self.YNyq,color=color,label=label)
        add_arrow(line,pcts=[0.2],middle=True)
        ax.legend()
        plt.tight_layout()
        return fig
        
    def cauchy(self,contour,**kwargs):
        """
        Plot "Cauchy" chart.
            left  chart: origin contour C and poles and zeros of F(p)
            right chart: image contour by F(C)
        """
        x=kwargs.get('xlim', [(-5,5),(-5,5)])
        y=kwargs.get('ylim', [(-5,5),(-5,5)])
        colors=kwargs.get('colors', None)
        label=kwargs.get('label','')
        contourLabel=kwargs.get('contourLabel','')
        middle=kwargs.get('middle',True)
        if isinstance(x,tuple):
            xlim=[x,x]
        else:
            xlim=x
        if isinstance(y,tuple):
            ylim=[y,y]
        else:
            ylim=y
        if not colors:
            colorO=None
            colorI=None
        else:
            colorO=colors[0]
            colorI=colors[1]

        self.Corigin=[]
        self.Cimage=[]
        print(60*'*')
        print("Cauchy plot : contour "+contourLabel)
        print(self)
        print(60*'*'+'\n')
        
        for path in contour:
            self.Corigin.append([complex(p[0],p[1]) for p in path])
            self.Cimage.append([self.evaluate(complex(p[0],p[1])) for p in path])
        
        # matlplotlib instruction
        fig = plt.figure(figsize=(9,4),dpi=100)
        #fig.suptitle('Cauchy plot',fontsize=24,y=1.0) 
        # Origin chart (left)
        ax = fig.add_subplot(1, 2, 1)
        ax.set(xlim=xlim[0], ylim=ylim[0])
        ax.title.set_text(r'origin $\mathcal{C}$')
        ax.title.set_size(20)
        ax.xaxis.label.set_text(r'$\operatorname{Re}[p]$')
        ax.xaxis.label.set_size(16)
        ax.yaxis.label.set_text(r'$\operatorname{Im}[p]$')
        ax.yaxis.label.set_size(16)
        #plt.grid()
        for path in self.Corigin:
            line,=plt.plot([x.real for x in path],[x.imag for x in path],color=colorO)
            add_arrow(line,middle=True)
        # carte des pôles et zéros
        for zero in self.zeros:
            plt.scatter(zero.real,zero.imag,facecolors='none',color='g',marker='o',linewidth=2,s=[64])
        for pole in self.poles:
            plt.scatter(pole.real,pole.imag,color='r',marker='x',linewidth=2,s=[64])    
            
        # Image chart (right)
        ax = fig.add_subplot(1, 2, 2)
        ax.set(xlim=xlim[1], ylim=ylim[1])
        ax.title.set_text(r'image $'+self.name+'(\mathcal{C}$)')
        ax.title.set_size(20)
        ax.xaxis.label.set_text(r'$\operatorname{Re}['+self.name+'(\mathcal{C})]$')
        ax.xaxis.label.set_size(16)
        ax.yaxis.label.set_text(r'$\operatorname{Im}['+self.name+'(\mathcal{C})]$')
        ax.yaxis.label.set_size(16)
        #plt.grid()
        for path in self.Cimage:
            line,=plt.plot([x.real for x in path],[x.imag for x in path],color=colorI)
            add_arrow(line,middle=middle)
        plt.scatter(0,0,color='black',marker='+',linewidth=2,s=[64])
        plt.tight_layout()
        #plt.show()
        
if __name__ == "__main__":  
    from contour import plot_contour

    #H_0
    gain=1
    num=lambda p : 1
    den=lambda p : 1+p+p**2
    H0=Ftransfert(num=num,den=den,gain=gain,name="H_0")
    print(repr(H0))
    print(str(H0))
    H0.nyquist(xlim=(-1,4),ylim=(-2,2),n=20000,dw=0.01,label="$K=1$",color="tab:green")

    # H_1
    gain=4
    poles=[]
    zeros=[(-1,0),(-2,0)]
    H1=Ftransfert(zeros=zeros,poles=poles,gain=gain,name="H_1")
    print(repr(H1))
    print(str(H1))

    # H_2
    gain=4
    zeros=[]
    poles=[(-1,0),(-2,0)]
    H2=Ftransfert(zeros=zeros,poles=poles,gain=gain,name="H_2")
    print(repr(H2))
    print(str(H2))
    
    # H_3
    gain=5
    zeros=[]
    poles=[(-1,0),(-2,0)]
    H3=Ftransfert(zeros=zeros,poles=poles,gain=gain,name="H_3")
    print(repr(H3))
    print(str(H3))
    
    # H_4
    gain=1
    zeros=[(1,-1),(1,1),(-3,7)]
    poles=[(-1,0),(-2,0)]
    H4=Ftransfert(zeros=zeros,poles=poles,gain=gain,name="H_4")
    print(repr(H4))
    print(str(H4))
    # exemples de lieux de Nyquist
    figH2=H2.nyquist(xlim=(-1,4),ylim=(-2,2),n=20000,dw=0.01,label="$K=4$",color="tab:green")
    H3.nyquist(figH2,xlim=(-1,4),ylim=(-2,2),n=20000,dw=0.01,label="$K=5$",replot=True,color="tab:blue")
    
    #FT roots
    zeros=[(-1,0),(-4,0),(-3,0)]
    poles=[(-0.75,-0.5),(-0.75,0.5)]
    gain=0.25
    F2=Ftransfert(zeros=zeros,poles=poles,gain=gain,name="F")
    print(repr(F2))
    print(str(F2))
    # Definition d'un contour npts : nombre de points par segments
    C=circle(center=(-1.0,0),radius=1.0,npts=256)
    F2.cauchy(C,xlim=[(-2.5,1.0),(-1.75,5)],ylim=[(-1.5,1.5),(-3,3)],colors=["tab:blue","tab:green"],contourLabel="cercle")
    plt.show()
    

    poles=[]
    zeros=[(-1,0)]
    gain=1
    F=Ftransfert(zeros=zeros,poles=poles,gain=gain)
    print(F)
    print(repr(F))
    C1=rectangle((1,-1),(2,1),npts=64)
    plot_contour(C1,xlim=(-2,3.5),ylim=(-1.5,1.5))
    F.cauchy(C1,xlim=(-2,3.5),ylim=(-1.5,1.5),contourLabel="C1")
    plt.show()
