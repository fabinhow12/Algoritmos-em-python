__author__ = 'Fábio Henrique E Walison Filipe'


# Verifica se o Ano é bissexto
def VerificaAno(ano):
    if (int(ano) % 4 == 0 and int(ano) % 100 != 0) or (int(ano) % 400 == 0):
        print("O Ano é Bissexto")
    else:
        print("O Ano Não É Bissexto")


print("Programa Do Ano Bissexto\n\n")


ano = str(input("Digite O Ano: "))
print("")

if int(ano) < 0:
    print("Não Tem Ano Negativo")
elif len(ano) != 4:
    print("Digite Um Ano Válido")

else:

    VerificaAno(ano)  # Chama A Função
