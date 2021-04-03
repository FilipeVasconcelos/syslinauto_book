
if __name__ == "__main__":  
    import matplotlib.pyplot as plt
    from ftransfert import Ftransfert
    from contour import plot_contour,circle,rectangle

    poles=[(0,0),(0,0),(0,0)]
    zeros=[(-1,0)]
    gain=1
    F=Ftransfert(zeros=zeros,poles=poles,gain=gain)
    C1=rectangle((1.0,-1),(1.5,1),npts=64)
    F.cauchy(C1,xlim=[(-2,2),(-3,3)],ylim=[(-1.5,1.5),(-2,2)],contourLabel="rectangle")
    plt.show()
    C2=circle(center=(0.0,0.0),radius=0.99,npts=512)
    F.cauchy(C2,xlim=[(-2,2),(-2.5,2.5)],ylim=[(-1.5,1.5),(-2.5,2.5)],colors=["tab:blue","tab:green"],contourLabel="cercle r<1")
    plt.show()
    C3=circle(center=(0.0,0.0),radius=1.5,npts=512)
    F.cauchy(C3,xlim=[(-2.5,2.5),(-1,1)],ylim=[(-2,2),(-1,1)],colors=["tab:blue","tab:green"],contourLabel="cercle r>1")
    plt.show()
    
    #FT roots
    zeros=[(-1,0),(-4,0),(-3,0)]
    poles=[(-0.75,-0.5),(-0.75,0.5)]
    gain=0.25
    F2=Ftransfert(zeros=zeros,poles=poles,gain=gain,name="F")
    # Definition d'un contour npts : nombre de points par segments
    C=circle(center=(-1.0,0),radius=1.0,npts=512)
    F2.cauchy(C,xlim=[(-2.5,1.0),(-1.75,5)],ylim=[(-1.5,1.5),(-3,3)],colors=["tab:blue","tab:green"],contourLabel="cercle")
    plt.show()
    
