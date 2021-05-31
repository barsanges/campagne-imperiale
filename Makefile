all: Artanis\ des\ Hauts\ -\ Caractéristiques.pdf \
	Baldr\ Karadrin\ -\ Caractéristiques.pdf \
	Brondol\ Snotson\ -\ Caractéristiques.pdf \
	Grotius\ Onderhoud\ -\ Caractéristiques.pdf \
	Heinrich\ Fälscher\ -\ Caractéristiques.pdf \
	Karl\ von\ Schwangau\ -\ Caractéristiques.pdf

clean:
	latexmk -c

Artanis\ des\ Hauts\ -\ Caractéristiques.pdf: artanis-des-hauts.yml
	python topdf.py $<

Baldr\ Karadrin\ -\ Caractéristiques.pdf: baldr-karadrin.yml
	python topdf.py $<

Brondol\ Snotson\ -\ Caractéristiques.pdf: brondol-snotson.yml
	python topdf.py $<

Grotius\ Onderhoud\ -\ Caractéristiques.pdf: grotius-onderhoud.yml
	python topdf.py $<

Heinrich\ Fälscher\ -\ Caractéristiques.pdf: heinrich-fälscher.yml
	python topdf.py $<

Karl\ von\ Schwangau\ -\ Caractéristiques.pdf: karl-von-schwangau.yml
	python topdf.py $<
