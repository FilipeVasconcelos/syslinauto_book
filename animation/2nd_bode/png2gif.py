import sys
import re
def sortNat( l ):
    """ 
    Sort the given list in the way that humans expect.
    """
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    l.sort( key=alphanum_key )
    return l

def rmext(filename,extsize=4):
    return filename[:-extsize]

if __name__=="__main__":

    import os

    rep='2nd_bode_files'
    outputfile='2nd_bode'
    cmd_argument=''
    for path in sortNat(os.listdir(rep)):
        full_path=os.path.join(rep, path)
        if full_path.endswith(".png") and os.path.isfile(full_path):
            cmd_argument+=rmext(full_path)+".png "
    os.system("convert -verbose -dispose 2 -delay 10 -loop 0 -density 600 "+cmd_argument+" "+outputfile+".gif")
