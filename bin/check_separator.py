#!/usr/bin/python3
import sys
import argparse
beginendenv=["figure","align","align*","center","table","bequation","itemize","criteria",
            "theorem","definition","tcolorbox"]
braketenv=["chapter","section","subsection","susubsection","paragraph",
         "exercice","question"]
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# =============================================================================
def main_parser():
    parser = argparse.ArgumentParser(description='Check separator in tex files')
    parser.add_argument('filename', metavar='filename', type=str,
                        help='file name to parse')
    return parser.parse_args()
# =============================================================================
def check(line,context):
    if context in beginendenv:
        return "\\begin{"+context+"}" in line
    if context in braketenv:
        return "\\"+context+"{" in line or  "\\"+context+"[" in line
# =============================================================================
def braket(line,psep):
    for c in line :
        if c == "{":
            psep.append(0)
        elif c == "}" and len(psep)!=0:
            psep.pop()
        elif c == "}" and len(psep)==0:
            return None
    return psep 
# =============================================================================
def env(context,line):
    if "\\end{"+context+"}" in line :
        return []
    else:
        return [0]
# =============================================================================
def check_separator(nsep,sep,startline,finishline,lines):
    separators=True
    for i in range(startline-nsep,startline):
        if lines[i].replace("\n","") != "%"+79*sep:
            separators=False
    for i in range(finishline+1,finishline+nsep+1):
        if lines[i].replace("\n","") != "%"+79*sep:
            separators=False
    return separators
# =============================================================================
def iofile(lines,context,data):
    startcontext=[]
    endcontext=[]
    # premier passage pour déterminer le début de ligne du context
    for kline,line in enumerate(lines):
        if check(line,context) :
            startcontext.append(kline)
    psep=[]
    looking = False
    for startline in startcontext:
        kline=startline
        line=lines[kline]
        if context in braketenv:
            if '{' in line and '{' :
                psep=braket(line,psep)
            else:
                print(f"ligne : {kline:4d} {context:>10s} special")
                looking=True 
        if context in beginendenv:
            psep=env(context,line)
        while len(psep)!=0 or looking :
            kline+=1
            line=lines[kline]
            if context in braketenv:
                psep=braket(line,psep)
            if context in beginendenv:
                psep=env(context,line)
            if len(psep)==0 and looking :
                looking=False
                break
        endcontext.append(kline)
    #print(startcontext,endcontext)
    for start,end in zip(startcontext,endcontext):
        if not check_separator(data[0],data[1],start,end,lines):
            print(bcolors.FAIL+f"problème séparateur ligne : {start} {context}"+bcolors.ENDC)
# =============================================================================
if __name__=="__main__":

    args=main_parser()
    filename=args.filename
    print("check nombre de séparateurs des environnements LaTeX (script Python)")

    f=open(filename,'r')
    lines=f.readlines()
    f.close()

    sep={"chapter":[4,"%"],
         "section":[3,"%"],
         "subsection":[2,"%"],
         "susubsection":[1,"%"],
         "paragraph":[1,"%"],
         "exercice":[1,"%"],
         "question":[1,"%"],
         "figure":[1,"-"],
         "center":[1,"-"],
         "align":[1,"-"],
         "align*":[1,"-"],
         "table":[1,"-"],
         "bequation":[1,"-"],
         "itemize":[1,"-"],
         "criteria":[1,"-"],
         "theorem":[1,"-"],
         "definition":[1,"-"],
         "tcolorbox":[1,"-"]
         }

    for context,data in sep.items() :
        iofile(lines,context,data)


