// ======================================================================
//                        Correcteur PID (AP + PI)
// ======================================================================
w0=4                                     // pulsation de coupure
phi_i_pid=(135+(phi_4-M_phi)*0.5)*PI/180 // radian
phi_d_pid=(-45+(M_phi-phi_4)*0.5)*PI/180 // radian
// ----------------------------------------------------------------------
// Paramètres du correcteur AP
a_pid=(1+sin(phi_d_pid))/(1-sin(phi_d_pid))
tau_d_pid=1/(sqrt(a_pid)*w0)
kd_pid=1/sqrt(a_pid)
// Fonction de transfert AP
CAP_pid=syslin('c',kd_pid*(1+a_pid*tau_d_pid*p),1+tau_d_pid*p)
// ----------------------------------------------------------------------
// Paramètres du correcteur PI
tau_i_pid=1/(w0*tan(phi_i_pid))
ki_pid=(tau_i_pid*w0)/(sqrt(1+tau_i_pid*w0*tau_i_pid*w0))
// Fonction de transfert PI
CPI_pid=syslin('c',ki_pid*(1+tau_i_pid*p),tau_i_pid*p)
// ----------------------------------------------------------------------
// PID
kp=10^(-db_4/20)
// ----------------------------------------------------------------------
// Fonction de transfert du correcteur
CPID=kp*CAP_pid*CPI_pid               // Correcteur PID
hbo_c_pid=CPID*hbo_nc                 // FTBO corrigée PID
hbf_c_pid=hbo_c_pid/(1+hbo_c_pid)     // FTBF corrigée PID
sr_hbf_c_pid=csim('step',t,hbf_c_pid) // réponse indicielle BF PID
// ----------------------------------------------------------------------
// Diagramme de Bode de la BO corrigée PID
scf(4);clf(4);
bode(hbo_c_pid,'rad')
