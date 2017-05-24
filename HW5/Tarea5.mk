Resultados_hw5.pdf: Resultados_hw5.tex
	pdflatex Resultados_hw5.tex

Resultados_hw5.tex: XH.pdf X1H.pdf YH.pdf Y1H.pdf FitCircle.pdf FitCircle1.pdf CH.pdf RH.pdf CL.pdf RL.pdf Fit.pdf

XH.pdf: plots_canal_ionico.py Canal_ionico.txt Canal_ionico1.txt
	python plots_canal_ionico.py

X1H.pdf: plots_canal_ionico.py Canal_ionico.txt Canal_ionico1.txt
	python plots_canal_ionico.py

YH.pdf: plots_canal_ionico.py Canal_ionico.txt Canal_ionico1.txt
	python plots_canal_ionico.py

Y1H.pdf: plots_canal_ionico.py Canal_ionico.txt Canal_ionico1.txt
	python plots_canal_ionico.py

FitCircle.pdf: plots_canal_ionico.py Canal_ionico.txt Canal_ionico1.txt
	python plots_canal_ionico.py

FitCircle1.pdf: plots_canal_ionico.py Canal_ionico.txt Canal_ionico1.txt
	python plots_canal_ionico.py

CH.pdf: CircuitoRC.py CircuitoRC.txt
	python CircuitoRC.py

RH.pdf: CircuitoRC.py CircuitoRC.txt
	python CircuitoRC.py

CL.pdf: CircuitoRC.py CircuitoRC.txt
	python CircuitoRC.py

RL.pdf: CircuitoRC.py CircuitoRC.txt
	python CircuitoRC.py

Fit.pdf: CircuitoRC.py CircuitoRC.txt
	python CircuitoRC.py

