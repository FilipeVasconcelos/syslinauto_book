// Cette partie peut être obtenue graphiquement
w0dB=2.38
frq=w0dB/(2*PI)
[frq1,repf] = repfreq(hbo_nc,frq)
[db_w0dB,phi_w0dB]= dbphi(repf)
//phi_w0dB : la phase du système non corrigé en w=2.38 rad/s
