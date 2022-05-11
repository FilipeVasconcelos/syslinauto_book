// ===============================
// Correcteur à avance de phase.
// ===============================
phi_d_d=42.8 //degree
phi_d=phi_d_d*PI/180
wc=4
a=(1+sin(phi_d))/(1-sin(phi_d))
tau_d=1/(sqrt(a)*wc)
Gd=9.46
kd=10^(Gd/20)/sqrt(a) 
CAP=syslin('c',kd*(1+a*tau_d*p),1+tau_d*p)
hbo_c_ap=hbo_nc*CAP
bode(hbo_c_ap,'rad')
