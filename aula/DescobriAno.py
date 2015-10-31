__author__ = 'Fábio Henrique E Walison Filipe'

#Verifica se o Ano é bissexto
def VerificaAno(ano):
    if (int(ano)%4 == 0 and int(ano)%100 != 0) or (int(ano)%400 == 0) :
       print("O Ano é Bissexto")
    else:
        print("O Ano Não É Bissexto")



print("Programa Do Ano Bissexto")
print("")
print("")

ano = str(input("Digite O Ano: "))
print("")
len(ano)

if len(ano) != 4 and len(ano)>0:
    print("Digite Um Ano Válido")
else:

    VerificaAno(ano)#Chama A Função















