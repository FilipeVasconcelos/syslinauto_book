// ----------------------------------------------------------------------
// TD 22 Correction des systèmes asservis -- Etude et
// Conception de correcteur AP, PI et PID
// auteur : F. Vasconcelos (ESME Sudria Lille)
// Problème adapté de H. Bourles et H. Guillard 
// ("Commande des systèmes. Performances et robustesse")
// ----------------------------------------------------------------------
clear();
p=%s                                      // indéterminée du polynôme
PI=%pi
hbo_nc=syslin('c',5*p+10,p^3+3*p^2+4*p+2) // FTBO Non Corrigée
scf(0);clf(0);
bode(hbo_nc,'rad')                        // diagramme de Bode en rad/s
t=0:0.05:10                               // Vecteur temps
hbf_nc=hbo_nc/(1+hbo_nc)                  // FTBF Non Corrigée
poles_hbf_nc=roots(hbf_nc.den)            // poles de la FTBF
sr_hbf_nc=csim('step',t,hbf_nc)           // réponse indicielle FTBF
// ----------------------------------------------------------------------
// tracé de la réponse indicielle
// et récupération des données dans un fichier texte
scf(1);clf(1);
plot2d(t,sr_hbf_nc,style=1)
fd = mopen('step_response_hbf_NC_td19.dat','wt');
for i=1:length(t)
    mfprintf(fd,'%.3f %.3f\n',t(i),sr_hbf_nc(i));
end
mclose('all')
// ======================================================================
//                      Correcteur à avance de phase.
// ======================================================================
w0=4         // pulsation de coupure souhaitée (rad/s)
M_phi=60     // marge de phase souhaitée
// ----------------------------------------------------------------------
// Cette partie peut être obtenue graphiquement
frq=w0/(2*%pi)
[frq1,repf] = repfreq(hbo_nc,frq)
[db_4,phi_4]= dbphi(repf)
//phi_4 : la phase du système non corrigé en w0=4 rad/s
//db_4  : le gain du système non corrigé en w0=4 rad/s
// ----------------------------------------------------------------------
phi_d=(-180+M_phi-phi_4)*%pi/180          // en degrée
Gd=-db_4                                  // gain à apporté => 0dB
// ----------------------------------------------------------------------
// paramètre du correcteur à avance de phase
a=(1+sin(phi_d))/(1-sin(phi_d))           // alpha
tau_d=1/(sqrt(a)*w0)                      // temps caractéristique
kd=10^(Gd/20)/sqrt(a) 
// ----------------------------------------------------------------------
// Fonction de transfert du correcteur
CAP=syslin('c',kd*(1+a*tau_d*p),1+tau_d*p)// Correcteur AP
hbo_c_ap=hbo_nc*CAP                       // FTBO corrigée AP
hbf_c_ap=hbo_c_ap/(1+hbo_c_ap)            // FTBF corrigée AP
sr_hbf_c_ap=csim('step',t,hbf_c_ap)       // réponse indicielle FTBF AP
// ----------------------------------------------------------------------
// tracé de la réponse indicielle
// et récupération des données dans un fichier texte
scf(1);
plot2d(t,sr_hbf_c_ap,style=2)
fd = mopen('step_response_hbf_C_AP_td19.dat','wt');
for i=1:length(t)
    mfprintf(fd,'%.3f %.3f\n',t(i),sr_hbf_c_ap(i));
end
mclose('all')
// ---------------------------------------------------------------------- 
// diagramme de Bode
scf(2);clf(2);
bode(hbo_c_ap,'rad')
// ======================================================================
//                           Correcteur PI.
// ======================================================================
w0=1                                      // pulsation de Bourles
// ----------------------------------------------------------------------
// Cette partie peut être obtenue graphiquement
frq=w0/(2*PI)
[frq1,repf] = repfreq(hbo_nc,frq)
[db_1,phi_1]= dbphi(repf)
//phi_1 : la phase du système non corrigé en w0=1 rad/s
//db_1  : le gain  du système non corrigé en w0=1 rad/s
// ----------------------------------------------------------------------
phi_i=(phi_1+180-M_phi)*PI/180             
Gi=1/(10^(db_1/20))
// paramètres du correcteur
tau_i=1/(w0*tan(phi_i))                      // temps caractéristiques 
ki=(Gi*tau_i*w0)/(sqrt(1+tau_i*w0*tau_i*w0)) // gain du correcteur
// ----------------------------------------------------------------------
// Fonction de transfert du correcteur
CPI=syslin('c',ki*(1+tau_i*p),tau_i*p)       // Correcteur PI
hbo_c_pi=hbo_nc*CPI                          // FTBO corrigée PI
hbf_c_pi=hbo_c_pi/(1+hbo_c_pi)               // FTBF corrigée PI
sr_hbf_c_pi=csim('step',t,hbf_c_pi)          // réponse indicielle BF PI
// ----------------------------------------------------------------------
// tracé de la réponse indicielle
// et récupération des données dans un fichier texte
scf(1);
plot2d(t,sr_hbf_c_pi,style=3)
fd = mopen('step_response_hbf_C_PI_td19.dat','wt');
for i=1:length(t)
    mfprintf(fd,'%.3f %.3f\n',t(i),sr_hbf_c_pi(i));
end
mclose('all')
// ---------------------------------------------------------------------- 
// Diagramme de Bode de la BO corrigée PI
scf(3);clf(3);
bode(hbo_c_pi,'rad')
// ======================================================================
//                        Correcteur PID (AP + PI)
// ======================================================================
w0=4                                      // pulsation de coupure
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
// tracé de la réponse indicielle
// et récupération des données dans un fichier texte
scf(1);
plot2d(t,sr_hbf_c_pid,style=4)
fd = mopen('step_response_hbf_C_PID_td19.dat','wt');
for i=1:length(t)
    mfprintf(fd,'%.3f %.3f\n',t(i),sr_hbf_c_pid(i));
end
mclose('all')
// ---------------------------------------------------------------------- 
// Diagramme de Bode de la BO corrigée PID
scf(4);clf(4);
bode(hbo_c_pid,'rad')
// ----------------------------------------------------------------------
// tracé de l'écart u (dans la notation de Bourles) 
// avec u(t) = e(t)-s(t) ici e(t)=1 (échelon) 
scf(5);clf(5);
cap_u=csim(1-sr_hbf_c_ap,t,CAP)
cpi_u=csim(1-sr_hbf_c_pi,t,CPI)
cpid_u=csim(1-sr_hbf_c_pid,t,CPID)
plot2d(t,1-sr_hbf_nc,style=1)
plot2d(t,cap_u,style=2)
plot2d(t,cpi_u,style=3)
plot2d(t,cpid_u,style=4)
// ----------------------------------------------------------------------
// Superposition des diagrammes de Bode
scf(6);clf(6);
bode([hbo_nc;hbo_c_ap;hbo_c_pi;hbo_c_pid],'rad')
hl=legend(['FTBO NC';'FTBO + AP';'FTBO + PI';'FTBO +PID']);
