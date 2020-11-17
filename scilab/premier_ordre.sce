//ESME-Sudria Lille
//F. Vasconcelos
//CC-BY-SA
//le 17/11/20 Initiation à Scilab
// =================================================================
//                       Réponses Temporelles
// =================================================================

// -------------------------------------
//  Définir un système du premier ordre
// -------------------------------------
clear;
p=poly(0,"p");
K=1,tau=1;            // paramètres du système
H=K/(1+tau*p);        // fonction de tranfert
PO=syslin("c",H)      // définition du SLCI
// -------------------------------------
//  Réponse indicielle
// -------------------------------------
grf=0;                //variable de la fenêtre
scf(grf);clf(grf);grf=grf+1
e1="step"
t=0:0.01:10
elt=ones(t)
K=1.
plot2d(t,elt,style=1)
for tau=1:6
    num=K
    den=1+tau*p
    H2 = syslin('c',[num],[den])
    plot2d(t,csim('step',t,H2),style=modulo(tau,6)+1)
end
a=get("current_axes")
ticks = a.x_ticks
ticks.locations = [0;2;4;6;8;10]
ticks.labels = ["0";"2";"4";"6";"8";"10"]
a.x_ticks = ticks
ticks = a.y_ticks
ticks.locations = [0.0;0.2;0.4;0.6;0.8;1.0]
ticks.labels = ["0";"0.2";"0.4";"0.6";"0.8";"1"]
a.y_ticks = ticks
a.font_size=4;
legend('échelon','$\tau=1$','$\tau=2$','$\tau=3$',
                 '$\tau=4$','$\tau=5$','$\tau=6$',
                 '$\tau=7$','$\tau=8$','$\tau=9$','$\tau=10$',4)   
xlabel("$t$","fontsize",5);
ylabel("$s(t)$","fontsize",5); 
xs2eps(grf-1,'fig_1er_'+string(grf)+'.eps')
// -------------------------------------
// Réponse impulsionnelle
// -------------------------------------
e2="imp"
scf(grf);clf(grf);grf=grf+1
for tau=1:6
    // Définition du système linéaire 
    // défini par la fonction de transfert H2
    num=K
    den=1+tau*p
    H2 = syslin('c',[num],[den])
    plot2d(t,csim('imp',t,H2),style=modulo(tau,6)+1)
end
a=get("current_axes")
ticks = a.x_ticks
ticks.locations = [0;2;4;6;8;10]
ticks.labels = ["0";"2";"4";"6";"8";"10"]
a.x_ticks = ticks
ticks = a.y_ticks
ticks.locations = [0.0;0.2;0.4;0.6;0.8;1.0]
ticks.labels = ["0";"0.2";"0.4";"0.6";"0.8";"1"]
a.y_ticks = ticks
a.font_size=4;
legend('$\tau=1$','$\tau=2$','$\tau=3$','$\tau=4$',
       '$\tau=5$','$\tau=6$','$\tau=7$','$\tau=8$',
       '$\tau=9$','$\tau=10$',1)   
xlabel("$t$","fontsize",5);
ylabel("$s(t)$","fontsize",5); 
xs2eps(grf-1,'fig_1er_'+string(grf)+'.eps')
// -------------------------------------
// Réponse à une rampe
// -------------------------------------
scf(grf);clf(grf);grf=grf+1
plot2d(t,t,style=1)
for tau=1:6
    // Définition du système linéaire 
    // défini par la fonction de transfert H2
    num=K
    den=1+tau*p
    H2 = syslin('c',[num],[den])
    plot2d(t,csim(t,t,H2),style=modulo(tau,6)+1)
end
a=get("current_axes")
ticks = a.x_ticks
ticks.locations = [0;2;4;6;8;10]
ticks.labels = ["0";"2";"4";"6";"8";"10"]
a.x_ticks = ticks
a.y_ticks = ticks
a.font_size=4;
legend('rampe','$\tau=1$','$\tau=2$','$\tau=3$',
               '$\tau=4$','$\tau=5$','$\tau=6$',
               '$\tau=7$','$\tau=8$','$\tau=9$','$\tau=10$',2)   
xlabel("$t$","fontsize",5);
ylabel("$s(t)$","fontsize",5); 
xs2eps(grf-1,'fig_1er_'+string(grf)+'.eps')
// -------------------------------------
// réponse harmonique (temporelle)
// -------------------------------------
scf(grf);clf(grf);grf=grf+1;
t=0.0:0.01:200;
om=0.1
e1=sin(om*t)
s1=csim(e1,t,PO);
subplot(3,1,1)
plot2d(t,e1,style=2)
plot2d(t,s1,style=5)
title('$\omega=0.1$',"fontsize",4);
xlabel("$t$","fontsize",4);
ylabel("$s(t)$","fontsize",4); 

t=0.0:0.01:20;
om=1.
e1=sin(om*t)
s1=csim(e1,t,PO);
subplot(3,1,2)
plot2d(t,e1,style=2)
plot2d(t,s1,style=5)
title('$\omega=1$',"fontsize",4);
xlabel("$t$","fontsize",4);
ylabel("$s(t)$","fontsize",4); 

t=0.0:0.01:2;
om=10.
e1=sin(om*t)
s1=csim(e1,t,H2);
subplot(3,1,3)
plot2d(t,e1,style=2)
plot2d(t,s1,style=5)
title('$\omega=10$',"fontsize",4);
xlabel("$t$","fontsize",4);
ylabel("$s(t)$","fontsize",4); 
xs2eps(grf-1,'fig_1er_'+string(grf)+'.eps')
// =================================================================
//                   Réponse Fréquentielle
// =================================================================
scf(grf);clf(grf);grf=grf+1;
fMin =0.001,fMax=100;
p=poly(0,"p")
K=1.,tau=1.;
H=K/(1+tau*p);
PO=syslin("c",[K],[1+tau*p])
// -------------------------------------
// diagrammme de Bode
// -------------------------------------
bode(PO,fMin,fMax,'rad'); 
bode_asymp(PO,fMin,fMax);
f=get("current_figure");
a=f.children; 
a1=a.children(1);
a2=a.children(2);
a.font_size=3;
x_label=a.x_label;
x_label.font_size=4;
y_label=a.y_label;
y_label.font_size=4;
e=a.children;
p1=e.children(1);
p1.foreground=2;
xs2eps(grf-1,'fig_1er_'+string(grf)+'.eps')
// ----------------------------------
// Comparaison des diagrammes de Bode
// ----------------------------------
scf(grf);clf(grf);grf=grf+1
tau=[1.0]
K=[1,10,100]
fMin =0.001,fMax=100;
num=K
den=1+tau*p
H2=num./den
H2tf = syslin('c',H2)
bode([H2tf(1,1);H2tf(1,2);H2tf(1,3)],fMin,fMax,"rad");
f=get("current_figure")
a=f.children; 
a1=a.children(1);
a2=a.children(2);
a.font_size=3;
x_label=a.x_label;
x_label.font_size=4;
y_label=a.y_label;
y_label.font_size=4;
e=a.children(1,1);
p1=e.children(1);
p1.foreground=1;
e=a.children(1,2);
p1=e.children(1);
p1.foreground=1;
p1=e.children(2);
p1.foreground=1;
p1=e.children(3);
p1.foreground=1;
xs2eps(grf-1,'fig_1er_'+string(grf)+'.eps')
//----------------------------------------------------------
// exemple d'évolution de la réponse 
// fréquentielle pour différentes valeur du paramètre tau
//----------------------------------------------------------
scf(grf);clf(grf);grf=grf+1;
fMin =0.001,fMax=100;
tau=[1,10,100]
K=1.
H2=K./(1+tau*p)
PO=syslin("c",H2)
bode([PO(1,1);PO(1,2);PO(1,3)],fMin,fMax,['$\tau=1$',
                                          '$\tau=10$',
                                          '$\tau=100$']);
a=f.children;
a1=a.children(1);
a2=a.children(2);
a.font_size=3;
x_label=a.x_label;
x_label.font_size=4;
y_label=a.y_label;
y_label.font_size=4;
e=a.children;
p1=e.children(1);
p1.foreground=2;
xs2eps(grf-1,'fig_1er_'+string(grf)+'.eps')
