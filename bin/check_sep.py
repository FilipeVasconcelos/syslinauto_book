#!/usr/bin/python3
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
def check_finish(line,sep):
    return sep[2] in line
# =============================================================================
def return_start(kline,lines):
    k=0
    while not check_start(lines[kline+k]) :
        k+=1
    return k+kline
# =============================================================================
def return_finish(kline,lines,sep):
    k=0
    while not check_finish(lines[kline+k],sep) :
        k+=1
    return k+kline
# =============================================================================
def check_separator(sep,startline,finishline,lines):
    separators=True
    for i in range(startline-sep[0],startline):
        if lines[i].replace("\n","") != "%"+79*sep[1]:
            separators=False
    for i in range(finishline+1,finishline+sep[0]+1):
        if lines[i].replace("\n","") != "%"+79*sep[1]:
            separators=False
    return separators
# =============================================================================
def eomacro(lines,context,sep):
    for kline,line in enumerate(lines):
        f=kline
        if check(line,checking) :
            f=return_finish(kline,lines,sep)
            if not check_separator(sep,kline,f,lines):
               print("problème séparateur ligne :",kline,checking)
# =============================================================================
if __name__=="__main__":

    args=main_parser()
    filename=args.filename
    print("check nombre de séparateurs des environnements LaTeX (script Python)")

    f=open(filename,'r')
    lines=f.readlines()
    f.close()

    sep={"\chapter":[4,"%","}"],
         "\section":[3,"%","}"],
         "\subsection":[2,"%","}"],
         "\susubsection":[1,"%","}"],
         "\paragraph":[1,"%","}"],
         "\exercice":[1,"%","}"],
         "\question":[1,"%","}"],
         "\\begin{figure}":[1,"-","\\end{figure}"],
         "\\begin{center}":[1,"-","\\end{center}"],
         "\\begin{align}":[1,"-","\\end{align}"],
         "\\begin{align*}":[1,"-","\\end{align*}"],
         "\\begin{table}":[1,"-","\\end{table}"],
         "\\begin{bequation}":[1,"-","\\end{bequation}"],
         "\\begin{itemize}":[1,"-","\\end{itemize}"],
         "\\begin{criteria}":[1,"-","\\end{criteria}"],
         "\\begin{theorem}":[1,"-","\\end{theorem}"],
         "\\begin{definition}":[1,"-","\\end{definition}"],
         "\\begin{tcolorbox}":[1,"-","\\end{tcolorbox}"]
         }

    for checking,data in sep.items() :
        eomacro(lines,checking,data)


