clear;
s=%s;
grf=0;
fd = mopen('step_response_hbf_NC.dat    ','wt');
hbo_NC=syslin('c',1,s*(s+0.2)) 
npoints=256
tmax=25
tmin=0
incr=(tmax-tmin)/npoints
t=tmin:incr:tmax;
hbf_NC=hbo_NC/(1+hbo_NC);
step_response_hbf_NC=csim('step',t,hbf_NC);
scf(grf);clf(grf);grf=grf+1
plot2d(t,step_response_hbf_NC);
for i=1:length(t)
    mfprintf(fd,'%.3f %.3f\n',t(i),step_response_hbf_NC(i));    
end
mclose('all')

scf(grf);clf(grf);grf=grf+1
bode(hbo_NC,0.01,10,'rad')

Kp=1
a=5.47
tau=0.43
CAP=syslin('c',Kp*(1+a*tau*s),(1+tau*s))
hbo_C=CAP*hbo_NC

scf(grf);clf(grf);grf=grf+1
bode([hbo_NC;hbo_C],0.01,10,'rad')

Kp=0.44
CAP=syslin('c',Kp*(1+a*tau*s),(1+tau*s))
hbo_C=CAP*hbo_NC
hbf_C=hbo_C/(hbo_C+1)
step_response_hbf_C=csim('step',t,hbf_C);
scf(0);
plot2d(t,step_response_hbf_C);
fd = mopen('step_response_hbf_C.dat','wt');
for i=1:length(t)
    mfprintf(fd,'%.3f %.3f\n',t(i),step_response_hbf_C(i));    
end
mclose('all')
