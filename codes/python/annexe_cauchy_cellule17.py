zeros=[(-0.75,0.5),(-0.75,-0.5),(-1.65,0),(-2,1),(-2,-1)]
poles=[(-1,0),(-2.25,0)]
gain=0.75
F_6=Ftransfert(zeros=zeros,poles=poles,gain=gain,name="F_6")
C3=circle(center=(-1,0),radius=0.75)
F_6.cauchy(C3,xlim=(-2.5,1.5),ylim=(-1.5,1.5))
