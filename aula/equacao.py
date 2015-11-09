__author__ = 'Fábio Henrique e Walison Filipe'

import math


# Calcula O DELTA
def CalculaDelta(a, b, c):

    return (b * b) - 4 * a * c


print("Cálculo de Raizes do Segundo Grau")
print("")

a = float(input("Digita O Valor De A: "))
b = float(input("Digite O VAlor De B: "))
c = float(input("Digite O Valor De C: "))


#Chama A Função

if  CalculaDelta(float(a), float(b), float(c)) >= 0:

    delta = CalculaDelta(float(a), float(b), float(c))
    x1 = (- b + math.sqrt(delta)) / 2 * a
    x2 = (- b - math.sqrt(delta)) / 2 * a
    print("As Raizes são: %3.1f e %3.1f" % (x1, x2))

else:
    print("\nNão Possui Raizes Reais")
