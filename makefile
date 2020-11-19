.SUFFIXES: .tex .aux .bib

mainfile=sma_auto

fast: dvifast
	dvips -t a4 ${mainfile}.dvi
pspdf: ps 
	ps2pdf -sPAPERSIZE=a4 -dNOSAFER -dAutoRotatePages=/None ${mainfile}.ps

text: html
	html2text -width 100 -style pretty ${mainfile}/${mainfile}.html | sed -n '/./,$$p' | head -n-2 >${mainfile}.txt

html:
	@#latex2html -split +0 -info "" -no_navigation ${mainfile}
	htlatex ${mainfile}

ps:	dvi
	dvips -t a4 ${mainfile}.dvi

svg:	dvi
	dvisvgm ${mainfile}.dvi

dvi:
	latex -shell-escape ${mainfile}
	bibtex ${mainfile} ||true
	makeindex ${mainfile}
	makeglossaries ${mainfile}
	latex -shell-escape ${mainfile}
	latex -shell-escape ${mainfile}

dvifast:
	latex -shell-escape ${mainfile}

clean:
	rm -f *.log *.auxlock *.ind *.ist   *.aux *.out *.bbl *.blg *.mtc* *.toc *.maf *.idx *.gls *.ilg *.glo *.glg 
	      *.acn *.acr     *.alg *.gl*-* *.slg *.slo *.sls
cleanfig: 
	rm -f figtikz/*.dpth figtikz/*.glo figtikz/*.glo-abr figtikz/*.idx figtikz/*.ist figtikz/*.log figtikz/*.mtc 
	      figtikz/*.mtc0 figtikz/*.slo figtikz/*.maf     figtikz/*.ilg figtikz/*.ind figtikz/*.acn figtikz/*.dep
mrproper: clean cleanfig

