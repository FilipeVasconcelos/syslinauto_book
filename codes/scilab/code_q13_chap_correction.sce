// ======================================================================
//                           Correcteur PI.
// ======================================================================
w0=1                               // pulsation arbitraire 1 rad/s
frq=w0/(2*PI)
[frq1,repf] = repfreq(hbo_nc,frq)
[db_1,phi_1]=dbphi(repf)        // calcul du module et de la phase à w0=1 rad/s
phi_i=(phi_1+180-60)*PI/180 
tau_i=1/(w0*tan(phi_i)) 
Gi=1/(10^(db_1/20))
ki=(Gi*tau_i*w0)/(sqrt(1+tau_i*w0*tau_i*w0))
CPI=syslin('c',ki*(1+tau_i*p),tau_i*p) // FT du correcteur
bode(hbo_c_pi,'rad')
