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
grf=0


function r=dans_bande(v,x)
if v>=1-x/100 & v<=1+x/100 then
    r=%T
else
    r=%F
end
endfunction


//temps d'etablissement à 5%
pct_bande=5.0  // 5%
liste_xi=[]
liste_two=[]
pas_xi=0.001
pas_t=0.005
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
plot2d(liste_xi,liste_two,logflag="ll",style=2)
xgrid(0,0.1,0)
a=get("current_axes");
a.auto_scale="off";
a.data_bounds=[0.1;10;1;100];
a.auto_ticks="off";
a.sub_ticks=[8,8];
p=a.children;
p1=p.children(1);
p1.thickness=2; 
p1.polyline_style=2;
p1.line_style=0;
ticks = a.x_ticks
ticks.locations = [0.01;0.1;1;10;100]
ticks.labels = ["0.01";"0.1";"1";"10";"100"]
a.x_ticks = ticks
ticks = a.y_ticks
ticks.locations = [1;10;100]
ticks.labels = ["1";"10";"100"]
a.y_ticks = ticks
a.font_size=3;
xlabel("$\xi$","fontsize",5);
ylabel("$\omega_0\cdot t_{5\%}$","fontsize",5); 
//title("Temps de réponse réduit","fontsize",4);
xs2eps(grf-1,'fig_temps_de_reduit.eps')

    
