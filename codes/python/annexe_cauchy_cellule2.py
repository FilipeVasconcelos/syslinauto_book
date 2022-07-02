zeros=[]  
poles=[(-1,0),(-2,0)]
gain=6
F=Ftransfert(zeros=zeros,poles=poles,gain=gain)
print(repr(F))
print(str(F))
