.SUFFIXES: .tex .aux .bib
timelimit=120
tlformat=$(shell date -u -d @${timelimit} +"%T")
mainfile=sma_auto

fast: dvifast 
	dvips -t a4 ${mainfile}.dvi
	ps2pdf -sPAPERSIZE=a4 -dNOSAFER -dAutoRotatePages=/None ${mainfile}.ps

pspdf: dvi 
	dvips -t a4 ${mainfile}.dvi > /dev/null 2>&1
	ps2pdf -sPAPERSIZE=a4 -dNOSAFER -dAutoRotatePages=/None ${mainfile}.ps > /dev/null 2>&1
pdf:  
	pdflatex -shell-escape ${mainfile} | pv -w 40 -i 0.001 -F "run 1 : %t %p (${tlformat})" > /dev/null 
	bibtex ${mainfile} ||true
	makeindex ${mainfile}
	makeglossaries ${mainfile}
	pdflatex -shell-escape ${mainfile}
	pdflatex -shell-escape ${mainfile}

text: html
	html2text -width 100 -style pretty ${mainfile}/${mainfile}.html | sed -n '/./,$$p' | head -n-2 >${mainfile}.txt

html:
	@#latex2html -split +0 -info "" -no_navigation ${mainfile}
	htlatex ${mainfile}

svg:	dvi
	dvisvgm ${mainfile}.dvi

dvi:
	@latex -shell-escape ${mainfile} | pv -w 60 -i 0.001 -F "latex run 1 : %t %p (${tlformat})" > /dev/null
	@bibtex ${mainfile} > /dev/null 2>&1 ||true
	@makeindex -q ${mainfile} 
	@makeglossaries -q ${mainfile} 
	@latex -shell-escape ${mainfile} | pv -w 60 -i 0.001 -F "latex run 2 : %t %p (${tlformat})" > /dev/null  
	@latex -shell-escape ${mainfile} | pv -w 60 -i 0.001 -F "latex run 3 : %t %p (${tlformat})" > /dev/null 

dvifast:
	latex -shell-escape ${mainfile}
clean:
	rm -f *.log *.auxlock *.ind *.ist   *.aux *.out *.bbl *.blg *.mtc* *.toc *.maf *.idx *.gls *.ilg *.glo *.glg *.acn *.acr     *.alg *.gl*-* *.slg *.slo *.sls tex/*.aux
cleanfig: 
	rm -f figtikz/*.dpth figtikz/*.glo figtikz/*.glo-abr figtikz/*.idx figtikz/*.ist figtikz/*.log figtikz/*.mtc figtikz/*.mtc0 figtikz/*.slo figtikz/*.maf     figtikz/*.ilg figtikz/*.ind figtikz/*.acn figtikz/*.dep figtikz/*.mw
mrproper: clean cleanfig

