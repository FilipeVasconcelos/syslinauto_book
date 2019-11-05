.SUFFIXES: .tex .aux .bib

filename=c7
simple:	ps-simple 
	ps2pdf -sPAPERSIZE=a4 ${filename}.ps

pspdfd:	psd
	ps2pdf -sPAPERSIZE=a4 ${filename}.ps

pspdf:	ps 
	ps2pdf -sPAPERSIZE=a4 ${filename}.ps

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
	ps2pdf -sPAPERSIZE=a4 -dColorConversionStrategy=/LeaveColorUnchanged -dPDFSETTINGS=/printer ${filename}.ps

text: html
	html2text -width 100 -style pretty ${filename}/${filename}.html | sed -n '/./,$$p' | head -n-2 >${filename}.txt

html:
	@#latex2html -split +0 -info "" -no_navigation ${filename}
	htlatex ${filename}

ps:	dvi
	dvips ${filename}.dvi
ps-simple:	dvi-simple
	dvips ${filename}.dvi

psd: dvid
	dvips ${filename}.dvi

dvi:
	latex --shell-escape ${filename}
	bibtex ${filename} ||true
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
