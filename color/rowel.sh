#!/bin/bash
filename=$1
ncol=$2
thickness=$3
code=${thickness::1}
if [ $ncol -gt 8 ]
then
    echo only 8 color available
    exit 1;
fi
if [ $code == "t" ]
then
    code=""
fi
grep -oE "rgb\( ? ?[0-9]+, ? ?[0-9]+, ? ?[0-9]+)?" $filename | \
sed -e 's/rgb(//g' -e 's/)//g' | \
sed -e 's/ //g' | \
head -n $ncol |awk -v t="$thickness" -v c="$code" 'BEGIN{i=1} {
                    printf("\\definecolor{col%d}{RGB}{%s}\n",i,$1);
                    printf("\\tikzstyle{%stcol%d}=[%s,col%d]\n",c,i,t,i);
                    i++
                
                
                }'
#awk -v t=$thickness 'BEGIN{i=0} {printf("\\definecolor{cq%d}{RGB}{%s}\n\\tikzstyle{%s tq%d}=[%s,cq%d]\n",i,$1,i,i);i++}'
