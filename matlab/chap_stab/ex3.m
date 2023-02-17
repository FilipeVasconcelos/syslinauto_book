K=1
num=K*(-1+2*rand(1,5));
den=[ rand(1,6)]  ;
num=0.6*[-0.4942    0.7679   -0.6074   -0.7573    0.0874]
den=[0.3146    0.3820    0.7915    0.8392    0.6802    0.4169]
H=tf(num,den)
subplot(1,3,1);
nyquist(H);
HBF=feedback(H,1)
subplot(1,3,2);
step(HBF)
subplot(1,3,3);
impulse(HBF)
pole(H)
pole(HBF)
