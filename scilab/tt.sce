s=poly(0,'s')
grf=0   
num=1.                                                                                                                        
den=1+s                                                                                                                       
SO=syslin('c',[num],[den])                                                                                                    
// ---------------------------------                                                                                    
fMin =0.0001,fMax=10000;                                                                                                      
scf(grf);clf(grf);grf=grf+1;                                                                                                  
bode(SO,fMin,fMax,"rad");bode_asymp(SO,fMin,fMax);                                                                            
f=get("current_figure")                                                                                                       
a=f.children // the handle on the Axes child                                                                                  
a.font_size=3;                                                                                                                
x_label=a.x_label;                                                                                                            
x_label.font_size=4;                                                                                                          
y_label=a.y_label;                                                                                                            
y_label.font_size=4;                                                                                                          
e=a.children                                                                                                                  
p1=e.children(1)                                                                                                              
p1.foreground=2;                                                                                                              
p1=e.children(2)                                                                                                              
p1.foreground=2;                                                                                                              
xs2eps(grf-1,'fig_bode_1er_ordre_den_ps.eps') 
