.SUFFIXES: .tex .aux .bib

pspdf:	ps 
	ps2pdf -sPAPERSIZE=a4 -dNOSAFER -dAutoRotatePages=/None ${filename}.ps

text: html
	html2text -width 100 -style pretty ${filename}/${filename}.html | sed -n '/./,$$p' | head -n-2 >${filename}.txt

html:
	@#latex2html -split +0 -info "" -no_navigation ${filename}
	htlatex ${filename}

ps:	dvi
	dvips -t a4 ${filename}.dvi

svg:	dvi
	dvisvgm ${filename}.dvi

dvi:
	latex -shell-escape ${filename}
	bibtex ${filename} ||true
	makeindex ${filename}
	makeglossaries ${filename}
	latex -shell-escape ${filename}
	latex -shell-escape ${filename}

clean:
	rm -f *.log *.auxlock *.ind *.ist *.aux *.out *.bbl *.blg *.mtc* *.toc *.maf *.idx *.gls *.ilg *.glo *.glg
	rm -f figtikz/*.dpth figtikz/*.glo figtikz/*.glo-abr figtikz/*.idx figtikz/*.ist figtikz/*.log figtikz/*.mtc figtikz/*.mtc0 figtikz/*.slo figtikz/*.maf figtikz/*.ilg figtikz/*.ind figtikz/*.acn figtikz/*.dep
	rm -f *.acn *.acr *.alg *.gl*-* *.slg *.slo *.sls
