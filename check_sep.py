#!/usr/local/bin/python3.7
import argparse

# =============================================================================
def main_parser():
    parser = argparse.ArgumentParser(description='Check separator in tex files')
    parser.add_argument('filename', metavar='filename', type=str,
                        help='file name to parse')
    return parser.parse_args()
# =============================================================================
def check(line,context):
    if context == "\chapter" :
        return context+"{" in line or context+"[" in line
    return context in line
# =============================================================================
def check_start(line):
    return "{" in line
# =============================================================================
def check_finish(line):
    return "}" in line
# =============================================================================
def return_start(kline,lines):
    k=0
    while not check_start(lines[kline+k]) :
        k+=1
    return k+kline
# =============================================================================
def return_finish(kline,lines):
    k=0
    while not check_finish(lines[kline+k]) :
        k+=1
    return k+kline
# =============================================================================
def check_separator(nb_sep,startline,finishline,lines):
    separators=True
    for i in range(startline-nb_sep,startline):
        if lines[i].replace("\n","") != 80*"%":
            separators=False
    for i in range(finishline+1,finishline+nb_sep+1):
    #    print(i,lines[i],end='')
        if lines[i].replace("\n","") != 80*"%":
            separators=False
    return separators
# =============================================================================
def eomacro(lines,context,nb_sep):
    for kline,line in enumerate(lines):
        f=kline
        if check(line,checking) :
            f=return_finish(kline,lines)
            if not check_separator(nb_sep,kline,f,lines):
               print("problème séparateurs ligne :",kline,checking)
# =============================================================================
if __name__=="__main__":

    args=main_parser()
    filename=args.filename
    print("début du script python")
    print("check nombre de séparateurs des environnement LaTeX")

    f=open(filename,'r')
    lines=f.readlines()
    f.close()

    checkings=["\chapter","\section","\subsection",
               "\susubsection","\paragraph","\exercice","\question"]
    nb_sep={"\chapter":4,"\section":3,"\subsection":2,
            "\susubsection":1,"\paragraph":1,"\exercice":1,"\question":1}

    for checking in checkings :
        eomacro(lines,checking,nb_sep[checking])
    print("fin du script python")
