clear();
pp=%s;                   // définition de l'indéterminé de polynôme
h=syslin('c',1,pp*(pp+1)+1)//ft en boucle fermée
tmax=30                 //temps max de la simulation
step=0.05
tc=0:step:tmax/2         //intervalle de la consigne seule"
tp=tc($)+step:step:tmax  //intervalle consigne+perturbation
t=0:step:tmax            //durée totale
Ec=[ones(1,length(t))]  //échelon Eo=1 
Ep=[zeros(1,length(tc)) 0.5*ones(1,length(tp))] // perturbation Po=0.5

//sans correction
sc=csim(Ec,t,h)  // réponse consigne seule
sp=csim(Ep,t,h)  // réponse pertutbation seule
ss=sc+sp         // réponse globale
scf(0);clf(0);
plot2d(t,ss,style=2)
plot2d(t,Ec,style=0)
plot2d(t,Ep+Ec,style=3)
filename='pert1_data.tab'
if isfile(filename) then
    unix('rm -f '+filename)
end
write(filename,[t' ss'],'(2(f24.12))')

//correction (un intégrateur en amont de la perturbation)
scf(1);clf(1);
//h=syslin('c',1,pp^2+1)//ft en boucle fermée
hp=syslin('c',pp,pp*(pp+1)+1) // ft de la perturbation seule
//sc=csim(Ec,t,h)  // réponse consigne seule
sp=csim(Ep,t,hp)
ss=sc+sp
plot2d(t,ss,style=2)
plot2d(t,Ec,style=0)
plot2d(t,Ep+Ec,style=3)
filename='pert2_data.tab'
if isfile(filename) then
    unix('rm -f '+filename)
end
write(filename,[t' ss'],'(2(f24.12))')
