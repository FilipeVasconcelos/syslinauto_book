PI=\%pi                                   // Constante pi
p=\%s                                     // indéterminée du polynôme
hbo_nc=syslin('c',5*p+10,p^3+3*p^2+4*p+2) // Boucle Ouverte Non Corrigée
scf(0);clf(0);
bode(hbo_nc,'rad')                        // diagramme de Bode en rad/s
