Resultados_hw4.pdf: Resultados_hw4.tex Plots_Temperatura.py
	python Plots_Temperatura.py
	pdflatex Resultados_hw4.tex

Caso2Mean.png: Plots_temperatura.py DT.txt
	python Plots_Temperatura.py

Caso1Mean.png: Plots_temperatura.py DT.txt
	python Plots_Temperatura.py

CASO2t2500sfronteraAbierta.png: Plots_temperatura.py DT.txt
	python Plots_Temperatura.py

CASO2t100sfronteraAbierta.png: Plots_temperatura.py DT.txt
	python Plots_Temperatura.py

CASO2t0sfronteraAbierta.png: Plots_temperatura.py DT.txt
	python Plots_Temperatura.py

CASO2t2500sfronteraPeriodica.png: Plots_temperatura.py DT.txt
	python Plots_Temperatura.py

CASO2t100sfronteraPeriodica.png: Plots_temperatura.py DT.txt
	python Plots_Temperatura.py

CASO2t0sfronteraPeriodica.png: Plots_temperatura.py DT.txt
	python Plots_Temperatura.py

CASO2t2500sfronteraCerrada.png: Plots_temperatura.py DT.txt
	python Plots_Temperatura.py

CASO2t100sfronteraCerrada.png: Plots_temperatura.py DT.txt
	python Plots_Temperatura.py

CASO2t0sfronteraCerrada.png: Plots_temperatura.py DT.txt
	python Plots_Temperatura.py

CASO1t2500sfronteraAbierta.png: Plots_temperatura.py DT.txt
	python Plots_Temperatura.py

CASO1t100sfronteraAbierta.png: Plots_temperatura.py DT.txt
	python Plots_Temperatura.py

CASO1t0sfronteraAbierta.png: Plots_temperatura.py DT.txt
	python Plots_Temperatura.py

CASO1t2500sfronteraPeriodica.png: Plots_temperatura.py DT.txt
	python Plots_Temperatura.py

CASO1t100sfronteraPeriodica.png: Plots_temperatura.py DT.txt
	python Plots_Temperatura.py

CASO1t0sfronteraPeriodica.png: Plots_temperatura.py DT.txt
	python Plots_Temperatura.py

CASO1t2500sfronteraCerrada.png: Plots_temperatura.py DT.txt
	python Plots_Temperatura.py

CASO1t100sfronteraCerrada.png: Plots_temperatura.py DT.txt
	python Plots_Temperatura.py

CASO1t0sfronteraCerrada.png: Plots_temperatura.py DT.txt
	python Plots_Temperatura.py

DT.txt: caminata.out
	./DT.out > DT.txt

DT.out: caminata.c
	gcc DifusionTemperatura.c -o DT.out


