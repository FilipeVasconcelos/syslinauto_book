.SUFFIXES: .tex .aux .bib

filename=sma_auto
#filename=tes
#filename=test_tikz
fast:	ps-simple 
	ps2pdf -sPAPERSIZE=a4 -dNOSAFER ${filename}.ps

pspdfd:	psd
	ps2pdf -sPAPERSIZE=a4 ${filename}.ps

pspdf:	ps 
	ps2pdf -sPAPERSIZE=a4 -dNOSAFER -dAutoRotatePages=/None ${filename}.ps
#	ps2pdf -sPAPERSIZE=a4 -dNOSAFER -dColorConversionStrategy=/LeaveColorUnchanged -dAutoRotatePages=/None ${filename}.ps

pdfd: 
	pdflatex -draftmode ${filename}
	bibtex ${filename} ||true
	makeindex ${filename}.idx
	makeindex ${filename}.gls 
	pdflatex -draftmode ${filename}
	pdflatex ${filename}
	
pdf: 
	pdflatex -shell-escape ${filename}
	bibtex ${filename} ||true
	makeindex ${filename}.idx
	makeindex ${filename}.gls 
	pdflatex -shell-escape ${filename}
	pdflatex -shell-escape ${filename}

pdf-print: ps
	ps2pdf -sPAPERSIZE=a4 -dAutoRotatePages=/None -dColorConversionStrategy=/LeaveColorUnchanged -dPDFSETTINGS=/printer ${filename}.ps

text: html
	html2text -width 100 -style pretty ${filename}/${filename}.html | sed -n '/./,$$p' | head -n-2 >${filename}.txt

html:
	@#latex2html -split +0 -info "" -no_navigation ${filename}
	htlatex ${filename}

ps:	dvi
	dvips -t a4 ${filename}.dvi

svg:	dvi
	dvisvgm ${filename}.dvi

ps-simple:	dvi-simple
	dvips -t a4 ${filename}.dvi

psd: dvid
	dvips -t a4 ${filename}.dvi

dvi:
	latex -shell-escape ${filename}
	bibtex ${filename} ||true
	makeindex ${filename}
	makeglossaries ${filename}
	latex -shell-escape ${filename}
	latex -shell-escape ${filename}
dvi-simple:
	latex -shell-escape ${filename}

dvid:
	latex -draftmode ${filename}
	bibtex ${filename} 
	makeindex ${filename}
	makeglossaries ${filename}
	latex -draftmode ${filename}
	latex -draftmode ${filename}

read:  pdf
	xpdf ${filename}.pdf 

aread: pdf
	acroread ${filename}.pdf

gvread: ps
	gv ${filename}.ps 

clean:
	rm -f *.log *.auxlock *.ind *.ist *.aux *.out *.bbl *.blg *.mtc* *.toc *.maf *.idx *.gls *.ilg *.glo *.glg
	rm -f figtikz/*.md5 figtikz/*.dpth figtikz/*.glo figtikz/*.glo-abr figtikz/*.idx figtikz/*.ist figtikz/*.log figtikz/*.md5 figtikz/*.mtc figtikz/*.mtc0 figtikz/*.slo figtikz/*.maf figtikz/*.ilg figtikz/*.ind figtikz/*.acn figtikz/*.dep
	rm -f *.acn *.acr *.alg *.gl*-* *.slg *.slo *.sls
