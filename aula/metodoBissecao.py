from pylab import * 
from math import* 

### entrada de dados 
funcao = str(input("Informe a função: "))
a = float(input("Informe o inicio do intervalo: "))
b = float(input("Informe o fim do intervalo: "))
precisao = float(input("Informe a precisão: "))

### aplica o intervalo a funcao e retorna os valores 
def f(x):
	return eval(funcao) 

### método 
if f(a)*f(b)<0: 
	x=a 
	while abs(f(x))>precisao: 
		x=(a+b)/2 
		if f(a)*f(x)<0: 
			b=x 
		else: 
			a=x 
	print("A raíz do intervalo informado é %f" %(x))
else: 
	print("Não foi possivel encontrar raizes no intervalo informado através do metodo da bissecção") 

