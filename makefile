.SUFFIXES: .tex .aux .bib
.PHONY: standalone pdf
mainfile=syslinauto

pdf: standalone
	pdflatex -shell-escape ${mainfile}  
bibtex:
	bibtex ${mainfile} ||true
makeindex:
	makeindex ${mainfile}
makeglossaries:
	makeglossaries ${mainfile}

standalone:
	$(MAKE) -f makefile_standalone
	
full: standalone pdf bibtex makeindex makeglossaries
	pdflatex -shell-escape ${mainfile}  
	pdflatex -shell-escape ${mainfile}  

clean:
	rm -f *.log *.auxlock *.ind *.ist   *.aux *.out *.bbl *.blg *.mtc* *.toc *.maf *.idx *.gls *.ilg *.glo *.glg *.acn *.acr     *.alg *.gl*-* *.slg *.slo *.sls tex/*.aux
cleanfig: 
	rm -f figtikz/*.dpth figtikz/*.glo figtikz/*.glo-abr figtikz/*.idx figtikz/*.ist figtikz/*.log figtikz/*.mtc figtikz/*.mtc0 figtikz/*.slo figtikz/*.maf     figtikz/*.ilg figtikz/*.ind figtikz/*.acn figtikz/*.dep figtikz/*.mw
mrproper: clean cleanfig

