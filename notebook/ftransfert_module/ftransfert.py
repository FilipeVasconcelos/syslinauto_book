import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math
from contour import add_arrow

TWO_PI=2*np.pi
HALF_PI=0.5*np.pi

def rad2deg(rad) : return rad*180/np.pi   # radian  -> degrée  (phase)
def deg2rad(deg) : return deg*np.pi/180   # degrée  -> radian  (phase)
def nat2dB(g)    : return 20*np.log10(g)  # naturel -> dB      (gain)
def dB2nat(dB)   : return 10**(dB/20)     # dB      -> naturel (gain)
def bo2bf(z)     : return z/(1+z)         # BO      -> BF



# ------------------------------------------------------------------------------
class Ftransfert():
    """
    Fonction de transfert :
    """
    def __init__(self,zeros=None,poles=None,num=None,den=None,gain=1,name="F",DPI=200,verbeux=1):
        self.gain=gain
        self.num=num
        self.den=den
        self.name=name
        self.DPI=DPI
        self.verbeux=verbeux
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

        # options for plotting phase
        self.phaseWrapping=False
        # riemann index,sign
        self.riemann=[0,-1]

        if self.type == "function" :
            self.integrators= self.den(0.0) == 0.0
        else:
            if len(poles)>0 : self.integrators = not all(self.poles).real!=0
    
    # ------------------------------------------------------------------------------
    def atanN(self,y,x):
        """
        Généralisation de la fonction atan2(y,x) 
        pour compter l'indice de la surface de Riemann.
        note : ça fonctionne mais est-ce que c'est pas un 
        overkill de quelque chose de plus simple.
        """
        if x > 0 :
            N=self.riemann[0]
            return np.arctan(y/x)-N*TWO_PI
        elif x<0 and y>=0 :
            if self.riemann[1] == -1 :
                self.riemann[0]+=1
                self.riemann[1]= 1
            N=self.riemann[0]
            return np.arctan(y/x)+np.pi-N*TWO_PI
        elif x<0 and y<0 :
            if self.riemann[1] == 1 :
                self.riemann[0]-=1
                self.riemann[1]=-1
            N=self.riemann[0]
            return np.arctan(y/x)-np.pi-N*TWO_PI
        elif x==0 and y>0 :
            N=self.riemann[0]
            return HALF_PI-N*TWO_PI
        elif x==0 and y<0 :
            N=self.riemann[0]
            return -HALF_PI-N*TWO_PI
        elif x==0 and y==0:
            return
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
        if self.type == "function": return "FT defined with lambda functions" 
        # ------------------------------------------------------------------------------
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
        # ------------------------------------------------------------------------------
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
            out+=outname+outgain+outz
        out+=spaceden*' '+outp+'\n'
        return out
    # ------------------------------------------------------------------------------
    def evaluate(self,p,gain):
        """
        evaluate the transfert function according
        to his definition.
        if function : just return the evaluation of num and den 
        in p.
        if "roots" : 
                                      (p-z1)(p-z2) ...
        return the evaluation of   K -------------------  
                                      (p-p1)(p-p2) ...
        """ 
        if self.type == "function":
            if np.any(abs(p) == 0.0) and self.integrators : return
            h=gain*self.num(p)/self.den(p)
            return h,abs(h),np.arctan2(h.imag,h.real)
        elif self.type == "roots" :
            zz=complex(1,0)
            phase=0
            for zero in self.zeros:
                zz*=(p-zero)
                phase+=np.arctan2((p-zero).imag,(p-zero).real)
            for pole in self.poles:
                zz/=(p-pole)
                phase-=np.arctan2((p-pole).imag,(p-pole).real)
            zz*=gain
            return zz,abs(zz),phase
    # ------------------------------------------------------------------------------
    def harm_response(self,w,gain):
        h,mag,phase=self.evaluate(w,gain)
        # wrapping matlab like ... il faut calculer la phase à partir de l'évaluation complète
        if self.phaseWrapping :
            phase=np.zeros(h.shape)
            k=0
            for hi in h:
                phase[k]=self.atanN(hi.imag,hi.real)
                k+=1
        return h.real,h.imag,mag,phase 
    # 
    def tabLaTeX(self,**kwargs):
        # Recast levels to new class
        class nf(float):
            def __repr__(self):
                return f'{self:.2f}'
        wlim=kwargs.get('wlim', (1e-2,1e2))
        n=kwargs.get('n',11)
        # array of pulsations
        ws=1j*np.logspace(np.log10(wlim[0]),np.log10(wlim[1]),n)
        response=self.harm_response(ws,self.gain)
        print("\\begin{center}")
        print("\\begin{tabular}{ccc}")
        print("\\hline")
        print("$\omega$ \si{\\radian\per\second} & Gain\si{\decibel} & Phase\si{\degree}\\\\")
        print("\\hline")
        for w,m,p in zip(ws,response[2],response[3]):
            print(str(nf(abs(w)))+" & "+str(nf(nat2dB(m)))+" & "+str(nf(rad2deg(p)))+"\\\\")
        print("\\hline")
        print("\end{tabular}")
        print("\\end{center}")

    # ------------------------------------------------------------------------------
    def nyquist(self,complet=False,**kwargs):
        """
        Plot Nyquist chart for p= -∞ j -> +∞ j
        in practice from :
            -fmax -> fmax if complet
                0 -> fmax if not complet
        """
        xlim=kwargs.get('xlim', (-5,5))
        ylim=kwargs.get('ylim', (-5,5))
        fmax=kwargs.get('fmax', 1e3)
        n=kwargs.get('n',4086)
        labels=kwargs.get('labels',[None])
        color=kwargs.get('color','tab:blue')
        gains=kwargs.get('gains',[])
        gains.insert(0,self.gain)
        if isinstance(labels,str):
            labels=[labels]
        if len(gains) > 2 :
            color=None
      
        if self.verbeux > 0 :
            print(60*'*')
            if complet :
                print("Complete Nyquist plot : "+self.name+'(p)')
                print("Interval des pulsations logarithmiques")
                w=-1j*np.logspace(np.log10(fmax),-np.log10(fmax),n)
                w+=1j*np.logspace(-np.log10(fmax),np.log10(fmax),n)
            else:
                print("Nyquist plot : "+self.name+'(p)')
                print("Interval des pulsations logarithmiques")
                w=1j*np.logspace(-np.log10(fmax),np.log10(fmax),n)
            print("Nombre de points",n,len(w))
            print(self)
            print(60*'*'+'\n')
       
        XNyq=[]
        YNyq=[]
        for kg,gain in enumerate(gains):
            # evaluer F(p) pour p=-infty j -> +infty j
            response=self.harm_response(w,gain)
            XNyq.append(response[0])
            YNyq.append(response[1])
        
        # matplotlib instructions
        fig = plt.figure(figsize=(6,4.5),dpi=self.DPI)
        ax = fig.add_subplot(1, 1, 1)
        ax.set(xlim=xlim, ylim=ylim)
        ax.title.set_text(r'Nyquist $'+self.name+'(p)$')
        ax.title.set_size(24)
        ax.xaxis.label.set_text(r'$\mathrm{Re}['+self.name+'(p)]$')
        ax.xaxis.label.set_size(18)
        ax.yaxis.label.set_text(r'$\mathrm{Im}['+self.name+'(p)]$')
        ax.yaxis.label.set_size(18)
        plt.grid()
        for kg in range(len(gains)):
            line,=plt.plot(XNyq[kg],YNyq[kg],color=color,label=labels[kg])
            add_arrow(line,pcts=[0.2],middle=True)
        if labels[0]: ax.legend()
        plt.tight_layout()
        plt.show()
        plt.close(fig)
    # ------------------------------------------------------------------------------
    def black(self,plot=True,nichols=False,**kwargs):
        """
        Plot Black (Nichols) chart for p= 0 -> +∞ j
        in practice from 0 -> fmax
        """
        xlim=kwargs.get('xlim', (-270,0))
        ylim=kwargs.get('ylim', (-40,40))
        fmax=kwargs.get('fmax', 1e3)
        n=kwargs.get('n',4096)
        labels=kwargs.get('labels',[None])
        color=kwargs.get('color','tab:blue')
        arrow_pcts=kwargs.get('arrow_pcts',[])
        if len(arrow_pcts)>0 : 
            middle=False
        else:
            middle=True
            arrow_pcts=[0.5]
        gains=kwargs.get('gains',[])
        gains.insert(0,self.gain)
        if isinstance(labels,str):
            labels=[labels]
        if len(gains) > 2 :
            color=None
        
        print(60*'*')
        print("Black plot : "+self.name+'(p)')
        print("Interval des pulsations logarithmiques")
        w=1j*np.logspace(-np.log10(fmax),np.log10(fmax),n)
        print("Nombre de points",n,len(w))
        print(self)
        print(60*'*'+'\n')
        
        XBlack=[]
        YBlack=[]
        for kg,gain in enumerate(gains):
            # evaluer F(p) pour p= 0 -> +infty j
            response=self.harm_response(w,gain)
            XBlack.append(rad2deg(response[3]))
            YBlack.append(nat2dB(response[2]))
        if not plot : return XBlack,YBlack
      
        # Black-Nichols
        if nichols :
            isomodules=[x for x in np.arange(xlim[0],-3)]
            isomodules+=[x for x in np.arange(-3.5,-1.5,0.5)]
            isomodules+=[x for x in np.arange(-1.8,-0.8,0.2)]
            isomodules+=[x for x in np.arange(-0.9,1.1,0.1)]
            isomodules+=[x for x in np.arange(1.5,3.5,0.5)]
            isomodules+=[4,5,6,8,10,12]
            isophases=[x for x in np.arange(-210,-40,10)]
            isophases+=[x for x in np.arange(-45,-15,5)]
            isophases+=[x for x in np.arange(-18,-8,2)]
            isophases+=[x for x in np.arange(-9,-2,1)]
            isophases+=[x for x in np.arange(-2.5,0,0.5)]
            isophases+=[x for x in np.arange(-0.4,0,0.1)]
            isophases+=[x for x in np.arange(0,0.5,0.1)]
            isophases+=[x for x in np.arange(0.5,3,0.5)]
            isophases+=[x for x in np.arange(3,11,1)]
            isophases+=[x for x in np.arange(12,22,2)]
            isophases+=[x for x in np.arange(25,55,5)]
            isophases+=[x for x in np.arange(60,240,10)]

            N=256
            phi=np.linspace(xlim[0],xlim[1],N)
            GdB=np.linspace(ylim[0],ylim[1],N)
            GdBbf=np.zeros((N,N))
            phibf=np.zeros((N,N))
            for i in range(N):
                for j in range(N):
                    g=dB2nat(GdB[i])
                    p=deg2rad(phi[j])
                    h=g*np.exp(1j*p)
                    z=bo2bf(complex(h.real,h.imag))
                    GdBbf[i][j]=nat2dB(np.abs(z))
                    phibf[i][j]=rad2deg(np.arctan2(z.imag,z.real))

        # matplotlib instructions
        fig = plt.figure(figsize=(6,4.5),dpi=self.DPI)
        ax = fig.add_subplot(1, 1, 1)
        ax.set(xlim=xlim, ylim=ylim)
        ax.title.set_text(r'Black $'+self.name+'(p)$')
        ax.title.set_size(24)
        ax.xaxis.label.set_text(r'$\phi(\omega)$ (degree)')
        ax.xaxis.label.set_size(18)
        ax.yaxis.label.set_text(r'$G_{dB}(\omega)$')
        ax.yaxis.label.set_size(18)
        if nichols:
            isom=ax.contour(phi, GdB,GdBbf,levels=isomodules,linewidths=0.3,colors="tab:gray",linestyles="solid")
            isop=ax.contour(phi, GdB,phibf,levels=isophases,linewidths=0.3,colors="tab:gray",linestyles="solid")
            # Recast levels to new class
            class nf(float):
                def __repr__(self):
                    s = f'{self:.1f}'
                    return f'{self:.0f}' if s[-1] == '0' else s
            isom.levels = [nf(val) for val in isom.levels]
            isop.levels = [nf(val) for val in isop.levels]
            fmtm = '%r dB'
            fmtp = '%r °'
            isop_loc_all=[(-260,10),(-260,11),(-260,12),(-260,13),(-260,15),(-260,16),(-260,17),(-260,18),(-260,19),
                    (-260,21),(-260,23),(-260,25),(-260,27),(-260,30),(-260,32),
                    (-100,10),(-100,11),(-100,12),(-100,13),(-100,15),(-100,16),(-100,17),(-100,18),(-100,19),
                    (-100,21),(-100,23),(-100,25),(-100,27),(-100,28),(-100,32),
                    (-20,-32),(-30,-32),(-40,-32),(-50,-32),
                    (-60,-32),(-70,-32),(-80,-32),(-90,-32),
                    (-100,-32),(-110,-32),(-120,-32),(-130,-32),
                    (-140,-32),(-150,-32),(-160,-32),(-170,-32),
                    (-190,-32),(-200,-32),(-210,-32),(-220,-32),
                    (-230,-32),(-240,-32),(-250,-32),(-260,-32),
                    (-270,-32),(-280,-32),(-290,-32),(-300,-32),
                    (-310,-32),(-320,-32),(-330,-32),(-340,-32)]
            isom_loc_all = [(-5,-21),(-5,-19),(-5,-17),
                        (-5,-15),(-5,-12),(-5,-10),
                        (-5,-7),(-5,-5),(-5,-3),(-5,-1),
                        (-5,0),(-5,2),(-5,4),(-5,6),
                        (-5,8),(-5,10),(-5,12),(-5,13),(-5,15),(-5,18),
                        (-175,3),(-175,4),(-175,6),(-175,7),(-175,8),(-175,10),
                        (-175,12),(-175,14),(-175,16),(-175,19),(-175,21),(-175,23),(-175,27)]
            isop_loc=[]
            for p in isop_loc_all:
                if (p[0]>xlim[0] and p[0]<xlim[1]) and (p[1]>ylim[0] and p[1]<ylim[1]):
                       isop_loc.append(p)
            isom_loc=[]
            for m in isom_loc_all:
                if (m[0]>xlim[0] and m[0]<xlim[1]) and (m[1]>ylim[0] and m[1]<ylim[1]):
                       isom_loc.append(m)
            ax.clabel(isop, isop.levels,inline=True,inline_spacing=-3, fontsize=5,fmt=fmtp,manual=isop_loc)
            ax.clabel(isom, isom.levels,inline=True,inline_spacing=-3, fontsize=5,fmt=fmtm,manual=isom_loc)
        else:
            plt.grid()
        for kg in range(len(gains)):
            line,=plt.plot(XBlack[kg],YBlack[kg],color=color,label=labels[kg])
            add_arrow(line,pcts=arrow_pcts,middle=middle)
        if labels[0]: ax.legend()
        #plt.tight_layout()
        return fig,line
    # ------------------------------------------------------------------------------
    def bode(self,**kwargs):
        """
        Plot Bode charts for p= 0 -> +∞ j
        in practice from 0 -> fmax
        """
        xlim=kwargs.get('xlim', (1e-2,1e2))
        y1lim=kwargs.get('y1lim', (-30,10))
        y2lim=kwargs.get('y2lim', (-90,0))
        fmax=kwargs.get('fmax', 1e3)
        n=kwargs.get('n',4096)
        labels=kwargs.get('labels',[None])
        color=kwargs.get('color','tab:blue')
        gains=kwargs.get('gains',[])
        gains.insert(0,self.gain)
        arrow_pcts=kwargs.get('arrow_pcts',[])
        if len(arrow_pcts)>0 : 
            middle=False
        else:
            middle=True
            arrow_pcts=[0.5]
        if isinstance(labels,str):
            labels=[labels]
        if len(gains) > 2 :
            color=None
        # array of pulsations
        w=1j*np.logspace(-np.log10(fmax),np.log10(fmax),n)
        
        if self.verbeux > 0 :
            print(60*'*')
            print("Bode plot : "+self.name+'(p)')
            print("Interval des pulsations logarithmiques",fmax)
            print("Nombre de points",n,len(w))
            print(self)
            print(60*'*'+'\n')
        
        XBode=[]  # Omega
        Y1Bode=[] # GdB(Omega)
        Y2Bode=[] # Phi(Omega)
        for kg,gain in enumerate(gains):
            response=self.harm_response(w,gain)
            XBode.append(w)
            Y1Bode.append(nat2dB(response[2]))
            Y2Bode.append(rad2deg(response[3]))
        
        # matlplotlib instruction
        fig = plt.figure(figsize=(6,8),dpi=self.DPI)
        # Gain chart (UP)
        ax1 = fig.add_subplot(2, 1, 1)
        ax1.title.set_text(r'Bode $'+self.name+'(p)$')
        ax1.title.set_size(24)
        ax1.set(xlim=xlim, ylim=y1lim)
        ax1.xaxis.label.set_text(r'$\omega$ (rad$\cdot$s$^{-1}$)')
        ax1.xaxis.label.set_size(18)
        ax1.yaxis.label.set_text(r'$G_{dB}$')
        ax1.yaxis.label.set_size(18)
        ax1.set_xscale('log')
        plt.grid()
        for kg in range(len(gains)):
            line,=plt.plot(XBode[kg].imag,Y1Bode[kg],color=color,label=labels[kg])
            add_arrow(line,pcts=arrow_pcts,middle=middle)
        # Phase chart (DOWN)
        ax2 = fig.add_subplot(2, 1, 2)
        ax2.set(xlim=xlim, ylim=y2lim)
        ax2.title.set_size(24)
        ax2.xaxis.label.set_text(r'$\omega$ (rad$\cdot$s$^{-1}$)')
        ax2.xaxis.label.set_size(18)
        ax2.yaxis.label.set_text(r'$\phi(\omega) (°)$')
        ax2.yaxis.label.set_size(18)
        ax2.set_xscale('log')
        plt.grid()
        for kg in range(len(gains)):
            line,=plt.plot(XBode[kg].imag,Y2Bode[kg],color=color,label=labels[kg])
            add_arrow(line,pcts=arrow_pcts,middle=middle)
        plt.tight_layout()
        return fig 
    
    # ------------------------------------------------------------------------------
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
        print(60*'*')
        print("Cauchy plot : contour "+contourLabel)
        print(self)
        print(60*'*'+'\n')
        Corigin=[]
        Cimage=[]
        for path in contour:
            Corigin.append([complex(p[0],p[1]) for p in path])
            Cimage.append([self.evaluate(complex(p[0],p[1]),self.gain) for p in path])
        # matlplotlib instruction
        fig = plt.figure(figsize=(9,4.5),dpi=self.DPI)
        # Origin chart (left)
        ax = fig.add_subplot(1, 2, 1)
        ax.set(xlim=xlim[0], ylim=ylim[0])
        ax.title.set_text(r'origin $\mathcal{C}$')
        ax.title.set_size(24)
        ax.xaxis.label.set_text(r'$\mathrm{Re}[p]$')
        ax.xaxis.label.set_size(18)
        ax.yaxis.label.set_text(r'$\mathrm{Im}[p]$')
        ax.yaxis.label.set_size(18)
        plt.grid()
        for path in Corigin:
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
        ax.title.set_size(24)
        ax.xaxis.label.set_text(r'$\mathrm{Re}['+self.name+'(\mathcal{C})]$')
        ax.xaxis.label.set_size(18)
        ax.yaxis.label.set_text(r'$\mathrm{Im}['+self.name+'(\mathcal{C})]$')
        ax.yaxis.label.set_size(18)
        plt.grid()
        for path in Cimage:
            line,=plt.plot([x.real for x in path],[x.imag for x in path],color=colorI)
            add_arrow(line,middle=middle)
        plt.scatter(0,0,color='black',marker='+',linewidth=2,s=[64])
        plt.tight_layout()
    # ------------------------------------------------------------------------------
        
if __name__ == "__main__":  
    
    #H_0
    gain=1
    num=lambda p : 1
    den=lambda p : 1+p+p**2
    H0=Ftransfert(num=num,den=den,gain=gain,name="H_0")
    print(repr(H0))
    print(str(H0))
        
    # H_1
    gain=4
    poles=[]
    zeros=[(-1,0),(-2,0)]
    H1=Ftransfert(zeros=zeros,poles=poles,gain=gain,name="H_1")
    print(repr(H1))
    print(str(H1))

    # H_4
    gain=1
    zeros=[(1,-1),(1,1),(-3,7)]
    poles=[(-1,0),(-2,0)]
    H4=Ftransfert(zeros=zeros,poles=poles,gain=gain,name="H_4")
    print(repr(H4))
    print(str(H4))
    
    #FT roots
    zeros=[(-1,0),(-4,0),(-3,0)]
    poles=[(-0.75,-0.5),(-0.75,0.5)]
    gain=0.25
    F2=Ftransfert(zeros=zeros,poles=poles,gain=gain,name="F")
    print(repr(F2))
    print(str(F2))
