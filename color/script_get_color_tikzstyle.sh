#!/bin/bash
filename=$1
ncol=$2
thickness=$3
grep -v "####" $filename | \
grep -v "\*\*\*" | \
grep -v -E "^$" | \
grep -oE "rgb\( ? ?[0-9]+, ? ?[0-9]+, ? ?[0-9]+)?" | \
sed -e 's/rgb(//g' -e 's/)//g' | \
sed -e 's/ //g' | \
awk 'BEGIN{i=0;j=0} 
     {printf("\\definecolor{cq%d%d}{RGB}{%s}\n\\tikzstyle{vtq%d%d}=[ultra thick,cq%d%d]\n",i,j,$1,i,j,i,j); 
      j++; 
      j=j%5; if (j==0) {i++}}'
