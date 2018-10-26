//ESME-Sudria Lille
//F. Vasconcelos
//CC-BY-SA

// ======================================
//      Système du second ordre
// ======================================
clear;
s=poly(0,'s')
grf=0

// ---------------------------------------
omega=1.0
xi=0.2
num=omega**2
den=s**2+2*xi*omega*s+omega**2
SO=syslin('c',[num],[den])
PO=syslin('c',[1],[0.5*s+1])
PO2=syslin('c',[1],[0.001*s+1])
PO3=syslin('c',[10*s],[1+s])
// ---------------------------------
fMin =0.01,fMax=100;
scf(grf);clf(grf);grf=grf+1;
//nyquist([SO(1,1);SO(1,2);SO(1,3);SO(1,4);SO(1,5);SO(1,6);SO(1,7);SO(1,8);SO(1,9);SO(1,10)]);
//nyquist([SO(1,1)*PO;SO(1,2)*PO;SO(1,3)*PO;SO(1,4)*PO;SO(1,5)*PO;SO(1,6)*PO;SO(1,7)*PO;SO(1,8)*PO;SO(1,9)*PO;SO(1,10)*PO]);
//nyquist([SO(1,1)*PO*PO2;SO(1,2)*PO*PO2;SO(1,3)*PO*PO2;SO(1,4)*PO*PO2;SO(1,5)*PO*PO2;SO(1,6)*PO*PO2;SO(1,7)*PO*PO2;SO(1,8)*PO*PO2;SO(1,9)*PO*PO2;SO(1,10)*PO*PO2]);
nyquist(SO*PO*PO2*PO3)
abort

