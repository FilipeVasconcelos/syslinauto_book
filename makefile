.SUFFIXES: .tex .aux .bib

filename=sma_auto
#filename=tes
#filename=test_tikz
simple:	ps-simple 
	ps2pdf -sPAPERSIZE=a4 ${filename}.ps

pspdfd:	psd
	ps2pdf -sPAPERSIZE=a4 ${filename}.ps

pspdf:	ps 
	ps2pdf -sPAPERSIZE=a4 -dNOSAFER -dAutoRotatePages=/None ${filename}.ps

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
	#makeindex ${filename}.idx
	#makeindex ${filename}.gls 
	pdflatex ${filename}
	pdflatex ${filename}

pdf-print: ps
	ps2pdf -sPAPERSIZE=a4 -dAutoRotatePages=/None -dColorConversionStrategy=/LeaveColorUnchanged -dPDFSETTINGS=/printer ${filename}.ps

text: html
	html2text -width 100 -style pretty ${filename}/${filename}.html | sed -n '/./,$$p' | head -n-2 >${filename}.txt

html:
	@#latex2html -split +0 -info "" -no_navigation ${filename}
	htlatex ${filename}

ps:	dvi
	dvips -t a4 ${filename}.dvi
ps-simple:	dvi-simple
	dvips -t a4 ${filename}.dvi

psd: dvid
	dvips -t a4 ${filename}.dvi

dvi:
	latex --shell-escape ${filename}
	bibtex ${filename} ||true
	makeindex ${filename}
	makeglossaries ${filename}
	latex ${filename}
	latex ${filename}
dvi-simple:
	latex --shell-escape ${filename}

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
	rm -f fig/*.log fig/*.auxlock fig/*.ind fig/*.ist fig/*.aux fig/*.out fig/*.bbl fig/*.blg fig/*.mtc* fig/*.toc fig/*.maf fig/*.idx fig/*.gls fig/*.ilg fig/*.glo fig/*.glg fig/*.md5
