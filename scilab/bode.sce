//ESME-Sudria Lille
//F. Vasconcelos
//CC-BY-SA

// ======================================
//      Système du second ordre
// ======================================
clear;
s=poly(0,'s')
grf=0

// ---------------------------------------
// intégrateur pur
// ---------------------------------------
num=1
den=s
SO=syslin('c',[num],[den])
// ---------------------------------
fMin =0.0001,fMax=10000;
scf(grf);clf(grf);grf=grf+1;
bode(SO,fMin,fMax,"rad")//;bode_asymp(SO,fMin,fMax);
f=get("current_figure")
a=f.children            // the handle on the Axes child
a.font_size=3;
x_label=a.x_label;
x_label.font_size=4;
y_label=a.y_label;
y_label.font_size=4;
e=a.children
p1=e.children(1)
p1.foreground=2;
p1=e.children(2)
p1.foreground=2;
xs2eps(grf-1,'fig_bode_integrateur_pur.eps')

// ---------------------------------------
// dérivateur pur
// ---------------------------------------
num=s
den=1
SO=syslin('c',[num],[den])
// ---------------------------------
fMin =0.0001,fMax=10000;
scf(grf);clf(grf);grf=grf+1;
bode(SO,fMin,fMax,"rad")//;bode_asymp(SO,fMin,fMax);
f=get("current_figure")
a=f.children // the handle on the Axes child
a.font_size=3;
x_label=a.x_label;
x_label.font_size=4;
y_label=a.y_label;
y_label.font_size=4;
e=a.children
p1=e.children(1)
p1.foreground=2;
p1=e.children(2)
p1.foreground=2;
xs2eps(grf-1,'fig_bode_derivateur_pur.eps')

// ---------------------------------------
// 1er ordre 1/1+s
// ---------------------------------------
num=1.
den=1+s
SO=syslin('c',[num],[den])
// ---------------------------------
fMin =0.0001,fMax=10000;
scf(grf);clf(grf);grf=grf+1;
bode(SO,fMin,fMax,"rad");bode_asymp(SO,fMin,fMax);
f=get("current_figure")
a=f.children // the handle on the Axes child
a.font_size=3;
x_label=a.x_label;
x_label.font_size=4;
y_label=a.y_label;
y_label.font_size=4;
e=a.children
p1=e.children(1)
p1.foreground=2;
p1=e.children(2)
p1.foreground=2;
xs2eps(grf-1,'fig_bode_1er_ordre_den_ps.eps')

// ---------------------------------------
// 1er ordre 1/1-s
// ---------------------------------------
num=1.
den=-s+1
SO=syslin('c',[num],[den])
// ---------------------------------
fMin =0.0001,fMax=10000;
scf(grf);clf(grf);grf=grf+1;
bode(SO,fMin,fMax,"rad");bode_asymp(SO,fMin,fMax);
f=get("current_figure")
a=f.children // the handle on the Axes child
a.font_size=3;
x_label=a.x_label;
x_label.font_size=4;
y_label=a.y_label;
y_label.font_size=4;
e=a.children
p1=e.children(1)
p1.foreground=2;
p1=e.children(2)
p1.foreground=2;
xs2eps(grf-1,'fig_bode_1er_ordre_den_ms.eps')
abort


// ---------------------------------------
// 1er ordre passe haut
// ---------------------------------------
num=1+s
den=1
SO=syslin('c',[num],[den])
// ---------------------------------
fMin =0.0001,fMax=10000;
scf(grf);clf(grf);grf=grf+1;
bode(SO,fMin,fMax,"rad");bode_asymp(SO,fMin,fMax);
f=get("current_figure")
a=f.children // the handle on the Axes child
a1=a.children(1)
a2=a.children(2)
a.font_size=3;
x_label=a.x_label;
x_label.font_size=4;
y_label=a.y_label;
y_label.font_size=4;
e=a.children
p1=e.children(1)
p1.foreground=2;
xs2eps(grf-1,'fig_bode_1er_ordre_num.eps')

// ---------------------------------------
// 1er ordre passe haut
// ---------------------------------------
num=0.1*s
den=1+0.1*s
SO=syslin('c',[num],[den])
// ---------------------------------
fMin =0.0001,fMax=10000;
scf(grf);clf(grf);grf=grf+1;
bode(SO,fMin,fMax,"rad")//;bode_asymp(SO,fMin,fMax);
f=get("current_figure")
a=f.children // the handle on the Axes child
a1=a.children(1)
a2=a.children(2)
a.font_size=3;
x_label=a.x_label;
x_label.font_size=4;
y_label=a.y_label;
y_label.font_size=4;
e=a.children
p1=e.children(1)
p1.foreground=2;
xs2eps(grf-1,'fig_bode_1er_ordre_haut.eps')



// ---------------------------------------
// 2 1er ordre en serie
// ---------------------------------------
num=1.
den=(1+s)*(1+0.1*s)
H2=num/den
SO=syslin('c',H2)
// ---------------------------------
fMin =0.01,fMax=100;
scf(grf);clf(grf);grf=grf+1;
bode(SO,fMin,fMax,"rad");bode_asymp(SO,fMin,fMax);
f=get("current_figure")
a=f.children // the handle on the Axes child
a1=a.children(1)
a2=a.children(2)
a.font_size=3;
x_label=a.x_label;
x_label.font_size=4;
y_label=a.y_label;
y_label.font_size=4;
e=a.children
p1=e.children(1)
p1.foreground=2;
xs2eps(grf-1,'fig_bode_2_1er_ordre_den.eps')

// ---------------------------------------
// 2 1er ordre en serie
// ---------------------------------------
num=1.
den=(1+s)*(1+0.1*s)
H2=num/den
SO=syslin('c',[den],[num])
// ---------------------------------
fMin =0.01,fMax=100;
scf(grf);clf(grf);grf=grf+1;
bode(SO,fMin,fMax,"rad");bode_asymp(SO,fMin,fMax);
f=get("current_figure")
a=f.children // the handle on the Axes child
a1=a.children(1)
a2=a.children(2)
a.font_size=3;
x_label=a.x_label;
x_label.font_size=4;
y_label=a.y_label;
y_label.font_size=4;
e=a.children
p1=e.children(1)
p1.foreground=2;
xs2eps(grf-1,'fig_bode_2_1er_ordre_num.eps')


// ---------------------------------------
// 2nd ordre en serie
// ---------------------------------------
omega=1.0
xi=0.1
num=omega**2
den=s**2+2*xi*omega*s+omega**2
H2=num/den
SO=syslin('c',H2)
// ---------------------------------
fMin =0.01,fMax=100;
scf(grf);clf(grf);grf=grf+1;
bode(SO,fMin,fMax,"rad");bode_asymp(SO,fMin,fMax);
f=get("current_figure")
a=f.children // the handle on the Axes child
a1=a.children(1)
a2=a.children(2)
a.font_size=3;
x_label=a.x_label;
x_label.font_size=4;
y_label=a.y_label;
y_label.font_size=4;
e=a.children
p1=e.children(1)
p1.foreground=2;
xs2eps(grf-1,'fig_bode_2nd_ordre_xi_resonance.eps')


// ---------------------------------------
// 2nd ordre en serie
// ---------------------------------------
omega=1.0
xi=0.8
num=omega**2
den=s**2+2*xi*omega*s+omega**2
H2=num/den
SO=syslin('c',H2)
// ---------------------------------
fMin =0.01,fMax=100;
scf(grf);clf(grf);grf=grf+1;
bode(SO,fMin,fMax,"rad");bode_asymp(SO,fMin,fMax);
f=get("current_figure")
a=f.children // the handle on the Axes child
a1=a.children(1)
a2=a.children(2)
a.font_size=3;
x_label=a.x_label;
x_label.font_size=4;
y_label=a.y_label;
y_label.font_size=4;
e=a.children
p1=e.children(1)
p1.foreground=2;
xs2eps(grf-1,'fig_bode_2nd_ordre_xi_pas_de_resonance.eps')


// ---------------------------------------
// exemples
// ---------------------------------------

fMin =0.0001,fMax=10000;
scf(grf);clf(grf);grf=grf+1;
// ---------------------------------
num=100*(s+1)^2
den=(100*s+1)*(10*s+1)*(0.01*s+1)
H2=num/den
SO=syslin('c',H2)
// ---------------------------------
bode(SO,fMin,fMax,"rad");bode_asymp(SO,fMin,fMax);
f=get("current_figure")
a=f.children // the handle on the Axes child
a1=a.children(1)
a2=a.children(2)
a.font_size=3;
x_label=a.x_label;
x_label.font_size=4;
y_label=a.y_label;
y_label.font_size=4;
e=a.children
p1=e.children(1)
p1.foreground=2;
xs2eps(grf-1,'fig_bode_exemple_1.eps')

scf(grf);clf(grf);grf=grf+1;
fMin=0.0001,fMax=10000;
// ---------------------------------
num=(10*s+1)*(0.1*s+1)
den=s*(0.001*s+1)^2
H2=num/den
SO=syslin('c',H2)
// ---------------------------------
bode(SO,fMin,fMax,"rad");bode_asymp(SO,fMin,fMax);
f=get("current_figure")
a=f.children // the handle on the Axes child
a1=a.children(1)
a2=a.children(2)
a.font_size=3;
x_label=a.x_label;
x_label.font_size=4;
y_label=a.y_label;
y_label.font_size=4;
e=a.children
p1=e.children(1)
p1.foreground=2;
xs2eps(grf-1,'fig_bode_exemple_2.eps')

scf(grf);clf(grf);grf=grf+1;
fMin=0.0001,fMax=100;
// ---------------------------------
num=10*(10*s+1)
den=(s+1)*(100*s+1)
H2=num/den
SO=syslin('c',H2)
// ---------------------------------
bode(SO,fMin,fMax,"rad");bode_asymp(SO,fMin,fMax);
f=get("current_figure")
a=f.children // the handle on the Axes child
a1=a.children(1)
a2=a.children(2)
a.font_size=3;
x_label=a.x_label;
x_label.font_size=4;
y_label=a.y_label;
y_label.font_size=4;
e=a.children
p1=e.children(1)
p1.foreground=2;
xs2eps(grf-1,'fig_bode_exemple_3.eps')







