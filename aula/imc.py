__author__ = 'Fábio Henrique E Walison Filipe'

#Função Para Calcular IMC
def Cimc(p,a):
    return p/(a*a)

print("Cálculo Do Imc")
print("")
print("")

peso =float(input("Digite seu Peso Em Kilogramas: "))
altura = float(input("Digite Sua Altura: "))

imc = Cimc(peso,altura)

print ("Seu Imc é %2.2f" %imc)

float(imc)

if imc<17.0 :
    print ("Muito Abaixo Do Peso")
elif imc<=18.49:
    print ("Abaixo Do Peso")
elif imc<=24.99 :
    print("Peso Normal")
elif imc<=29.99:
    print("Acima Do Peso")
elif imc<=34.99 :
    print("Obesidade 1")
elif imc<=39.99:
    print("Obesidade Severa")
else:
    print("Obesidade mórbida")

