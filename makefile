Resultados_hw4.pdf: Resultados_hw4.tex
	pdflatex Resultados_hw4.tex

Resultados_hw4.tex: Caso2Mean.png Caso1Mean.png CASO2t2500sfronteraAbierta.png CASO2t100sfronteraAbierta.png CASO2t0sfronteraAbierta.png CASO2t2500sfronteraPeriodica.png CASO2t100sfronteraPeriodica.png CASO2t0sfronteraPeriodica.png CASO2t2500sfronteraCerrada.png CASO2t100sfronteraCerrada.png CASO2t0sfronteraCerrada.png CASO1t2500sfronteraAbierta.png CASO1t100sfronteraAbierta.png CASO1t0sfronteraAbierta.png CASO1t2500sfronteraPeriodica.png CASO1t100sfronteraPeriodica.png CASO1t0sfronteraPeriodica.png CASO1t2500sfronteraCerrada.png CASO1t100sfronteraCerrada.png CASO1t0sfronteraCerrada.png

Caso2Mean.png: Plots_Temperatura.py DT.txt
	python Plots_Temperatura.py

Caso1Mean.png: Plots_Temperatura.py DT.txt
	python Plots_Temperatura.py

CASO2t2500sfronteraAbierta.png: Plots_Temperatura.py DT.txt
	python Plots_Temperatura.py

CASO2t100sfronteraAbierta.png: Plots_Temperatura.py DT.txt
	python Plots_Temperatura.py

CASO2t0sfronteraAbierta.png: Plots_Temperatura.py DT.txt
	python Plots_Temperatura.py

CASO2t2500sfronteraPeriodica.png: Plots_Temperatura.py DT.txt
	python Plots_Temperatura.py

CASO2t100sfronteraPeriodica.png: Plots_Temperatura.py DT.txt
	python Plots_Temperatura.py

CASO2t0sfronteraPeriodica.png: Plots_Temperatura.py DT.txt
	python Plots_Temperatura.py

CASO2t2500sfronteraCerrada.png: Plots_Temperatura.py DT.txt
	python Plots_Temperatura.py

CASO2t100sfronteraCerrada.png: Plots_Temperatura.py DT.txt
	python Plots_Temperatura.py

CASO2t0sfronteraCerrada.png: Plots_Temperatura.py DT.txt
	python Plots_Temperatura.py

CASO1t2500sfronteraAbierta.png: Plots_Temperatura.py DT.txt
	python Plots_Temperatura.py

CASO1t100sfronteraAbierta.png: Plots_Temperatura.py DT.txt
	python Plots_Temperatura.py

CASO1t0sfronteraAbierta.png: Plots_Temperatura.py DT.txt
	python Plots_Temperatura.py

CASO1t2500sfronteraPeriodica.png: Plots_Temperatura.py DT.txt
	python Plots_Temperatura.py

CASO1t100sfronteraPeriodica.png: Plots_Temperatura.py DT.txt
	python Plots_Temperatura.py

CASO1t0sfronteraPeriodica.png: Plots_Temperatura.py DT.txt
	python Plots_Temperatura.py

CASO1t2500sfronteraCerrada.png: Plots_Temperatura.py DT.txt
	python Plots_Temperatura.py

CASO1t100sfronteraCerrada.png: Plots_Temperatura.py DT.txt
	python Plots_Temperatura.py

CASO1t0sfronteraCerrada.png: Plots_Temperatura.py DT.txt
	python Plots_Temperatura.py

DT.txt: DT.out
	./DT.out > DT.txt

DT.out: DifusionTemperatura.c
	gcc DifusionTemperatura.c -o DT.out


