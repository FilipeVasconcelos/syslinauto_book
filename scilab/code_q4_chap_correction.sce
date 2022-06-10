t=0:0.05:10 // vecteur temps
hbf_nc=hbo_nc/(1+hbo_nc) // FTBF Non Corrigée
sr_hbf_nc=csim('step',t,hbf_nc) // sr : step_response
scf(1);clf(1);
plot2d(t,sr_hbf_nc,style=1) // tracé de la réponse en fonction du temps
