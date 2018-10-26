//ESME-Sudria Lille
//F. Vasconcelos
//CC-BY-SA
//le 28/02/18 Initiation à Scilab

// ======================================
//      Système du second ordre
// ======================================
clear;
function r=D(k,xi)
    r=exp((-xi*k*%pi)/sqrt(1-xi**2))
endfunction


//Définition de la variable de Laplace p et polynome en p
p = poly(0,'p')

// ---------------------------
// Cas du régime apériodique
// ---------------------------
// échelon
grf=0
scf(grf);clf(grf);grf=grf+1;
t=0:0.01:20
omega=1.
for xi=1:6
    // Définition du système linéaire défini par la fonction de transfert H2
    num=omega**2
    den=p**2+2*xi*omega*p+omega**2
    H2 = syslin('c',[num],[den])
    plot2d(t,csim('step',t,H2),style=xi)
end
a=get("current_axes")
a.font_size=3;
legend(["$\xi=1$","$\xi=2$","$\xi=3$","$\xi=4$","$\xi=5$","$\xi=6$","$\xi=7$","$\xi=8$","$\xi=9$","$\xi=10$"],4)
xlabel("$t$","fontsize",5);
ylabel("$s(t)$","fontsize",5); 
//title("Régime apériodique (réponse indicielle)","fontsize",4);
xs2eps(grf-1,'fig_2nd_'+string(grf)+'.eps')


// --------
//  dirac
// --------
scf(grf);clf(grf);grf=grf+1;
t=0:0.01:20
omega=1.
for xi=1:10
    // Définition du système linéaire défini par la fonction de transfert H2
    num=omega**2
    den=p**2+2*xi*omega*p+omega**2
    H2 = syslin('c',[num],[den])
    plot2d(t,csim('imp',t,H2),style=xi)
end
legend(["$\xi=1$","$\xi=2$","$\xi=3$","$\xi=4$","$\xi=5$","$\xi=6$","$\xi=7$","$\xi=8$","$\xi=9$","$\xi=10$"],1)
xlabel("$t$","fontsize",4);
ylabel("$s(t)$","fontsize",4); 
title("Régime apériodique (réponse impulsionnelle)","fontsize",4);
xs2eps(grf-1,'fig_2nd_'+string(grf)+'.eps')

// ------------------
//    rampe
// ------------------
scf(grf);clf(grf);grf=grf+1;
t=0:0.1:20
omega=1.
plot2d(t,t,style=1)
for xi=1:10
    // Définition du système linéaire défini par la fonction de transfert H2
    num=omega**2
    den=p**2+2*xi*omega*p+omega**2
    H2 = syslin('c',[num],[den])
    plot2d(t,csim(t,t,H2),style=xi+1)
end
legend(["rampe","$\xi=1$","$\xi=2$","$\xi=3$","$\xi=4$","$\xi=5$","$\xi=6$","$\xi=7$","$\xi=8$","$\xi=9$","$\xi=10$"],2)
xlabel("$t$","fontsize",4);
ylabel("$s(t)$","fontsize",4); 
title("Régime apériodique (réponse à une rampe)","fontsize",4);
xs2eps(grf-1,'fig_2nd_'+string(grf)+'.eps')


// -------------------------------
//Cas du régime pseudopériodique
// -------------------------------
// -------------
//  indicielle
// -------------
scf(grf);clf(grf);grf=grf+1;
t=0:0.01:20
for xi=0.1:0.1:1
    num=omega**2
    den=p**2+2*xi*omega*p+omega**2
    H2 = syslin('c',[num],[den])
    plot2d(t,csim('step',t,H2),style=10*xi)
end
legend(["$\xi=0.1$","$\xi=0.2$","$\xi=0.3$","$\xi=0.4$","$\xi=0.5$","$\xi=0.6$","$\xi=0.7$","$\xi=0.8$","$\xi=0.9$","$\xi=1$"],4)
xlabel("$t$","fontsize",4);
ylabel("$s(t)$","fontsize",4); 
title("Régime pseudo-périodique (réponse indicielle)","fontsize",4);
xs2eps(grf-1,'fig_2nd_'+string(grf)+'.eps')
// ----------------
// impulsionnelle
// ----------------
scf(grf);clf(grf);grf=grf+1;
t=0:0.01:20
for xi=0.1:0.1:1
    num=omega**2
    den=p**2+2*xi*omega*p+omega**2
    H2 = syslin('c',[num],[den])
    plot2d(t,csim('imp',t,H2),style=10*xi)
end

legend(["$\xi=0.1$","$\xi=0.2$","$\xi=0.3$","$\xi=0.4$","$\xi=0.5$","$\xi=0.6$","$\xi=0.7$","$\xi=0.8$","$\xi=0.9$","$\xi=1$"],1)
xlabel("$t$","fontsize",4);
ylabel("$s(t)$","fontsize",4); 
title("Régime pseudo-périodique (réponse impulsionnelle)","fontsize",4);
xs2eps(grf-1,'fig_2nd_'+string(grf)+'.eps')
// ----------------------------------------
//Tracé du dépassement en fonction de ksi
// ----------------------------------------
scf(grf);clf(grf);grf=grf+1;
xi=0.01:0.01:0.99
for k=1:10
    f=[]
    for x=0.01:0.01:0.99
        f=[f,D(k,x)]
    end
    plot2d("ll",xi,f,style=k,strf="011",rect=[0.01,0.01,1,1])
end
//xtitle("Dépassement en fonction de $\xi$")
legend(["$k=1$","$k=2$","$k=3$","$k=4$","$k=5$","$k=6$","$k=7$","$k=8$","$k=9$","$k=10$"],3)
xlabel("$\xi$","fontsize",4);
ylabel("$D$","fontsize",4); 
title("Dépassement en fonction de l''amortissement","fontsize",4);
xs2eps(grf-1,'fig_2nd_'+string(grf)+'.eps')

// ================================================
// Forme analytique de la reponse indicielle 
// ================================================

// reponse indicielle 2nd ordre analytique
function r=second_order(t,w0,xi)
    a=xi**2-1
    if xi>1 then
        sa=sqrt(a);
        r1=w0*(-xi+sa);
        r2=w0*(-xi-sa);
        r=(1/(r1-r2))*(r1*(1-exp(r2*t))-r2*(1-exp(r1*t)))
    end
    if xi<1 then
        sa=sqrt(-a);
        wd=w0*sa
        phi=atan(sa/xi)
        r=1-(1/sa)*exp(-xi*w0*t)*sin(wd*t+phi)
    end
    if xi==1 then
        r=1-(1+w0*t)*exp(-w0*t)
    end    
endfunction

// test xi > 1
scf(grf);clf(grf);grf=grf+1;
omega=1.
t=0:0.01:20
for xi=1:20
    f=[]
    for x=0:0.01:20
        f=[f,second_order(x,omega,xi)]
    end
    plot2d(t,f,style=xi)
end


xgrid(14)
xtitle("Régime apériodique (forme analytique)")
legend(["$\xi=1$","$\xi=2$","$\xi=3$","$\xi=4$","$\xi=5$","$\xi=6$","$\xi=7$","$\xi=8$","$\xi=9$","$\xi=10$"],4)
xlabel("$t$","fontsize",4);
ylabel("$s(t)$","fontsize",4); 
title("réponse impulsionnelle","fontsize",4);
// test xi < 1
scf(grf);clf(grf);grf=grf+1;
t=0:0.01:20
for xi=0.1:0.1:1
    f=[]
    for x=0:0.01:20
        f=[f,second_order(x,omega,xi)]
    end
    plot2d(t,f,style=xi*10)
end
xgrid(14)
xtitle("Régime pseudopériodique (forme analytique)")
xlabel("$t$","fontsize",4);
ylabel("$s(t)$","fontsize",4); 
title("réponse impulsionnelle","fontsize",4);

grf=grf-2;


function r=dans_bande(v,x)
if v>=1-x/100 & v<=1+x/100 then
    r=%T
else
    r=%F
end
endfunction


//temps d'etablissement à 5%
pct_bande=5  // 5%
liste_xi=[]
liste_two=[]
pas_xi=0.01
pas_t=0.05
omega=1.0

//z<0.6
//On teste la sortie de bande en partant d'une valeur de t suffisamment grande.
//Le temps de réponse réduit étant décroissant, on peut à chaque itération de xi,
//repartir avec la dernière valeur de t déterminée.

t=400
xi=0.01
while xi<0.6

    while dans_bande(second_order(t,omega,xi),pct_bande)
        t=t-pas_t
    end

    t=t+pas_t ;
    liste_xi=[liste_xi,xi] ;
    liste_two=[liste_two,omega*t] ;
    xi=xi+pas_xi
end


//xi>0.6 et xi<=1
//On teste la sortie de bande en partant d'une valeur de t suffisamment grande.
//A chaque itération de xi, on prend t=7 comme valeur de départ.

xi=0.6
while xi<=1
    t=20 ;
    while dans_bande(second_order(t,omega,xi),pct_bande)
        t=t-pas_t
    end
    t=t+pas_t
    liste_xi=[liste_xi,xi] ;
    liste_two=[liste_two,omega*t];
    xi=xi+pas_xi
end


// xi>=1
//On teste l'entrée de bande en partant d'une valeur de two suffisamment petite.
//Le temps de réponse réduit étant croissant, on peut à chaque itération de xi,
//repartir avec la dernière valeur de trwo déterminée.

xi=1.0
t=0
while xi<50
    while ~(dans_bande(second_order(t,omega,xi),pct_bande)) /// ~ not 
    t=t+pas_t
    end
    t=t-pas_t
    liste_xi=[liste_xi,xi] ;
    liste_two=[liste_two,omega*t] ;
    xi=xi+pas_xi
end

scf(grf);clf(grf);grf=grf+1;
plot2d(liste_xi,liste_two,logflag="ll")
//xgrid(14)
xlabel("$\xi$","fontsize",4);
ylabel("$\omega_0t_{5\%}$","fontsize",4); 
//title("Temps de réponse réduit","fontsize",4);
//xs2eps(grf-1,'fig_temps_de_reduit.eps')

