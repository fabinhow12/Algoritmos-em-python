_author_ = "Fábio Henrique e Walison Filipe"


# Função Para Verificar Se é Primo
def verificaPrimo(num):

    if num > 0:

        # Variável Booleana Para Verificar
        é_primo = True

        # procura por um divisor de num entre 2 e n-1
        dividi = 2
        while dividi < num and é_primo:
            if num % dividi == 0:
                é_primo = False
            dividi += 1

        if é_primo and num != 1:
            print(num, "É primo")
        else:
            print(num, "Não é primo")

    else:
        print("O Número Tem que ser Maior que zero")

print("Verificador de Número Primo\n\n")
# Pega O Valor
num = str(input("Digite o valor Para Verificar: "))

if num.isalpha():
    print("Só Pode Números E Não Letras")

elif num.isspace():
    print("Não Pode Ter Só Espaços , Digite Um Número")
else:
    #Chama A Função
    verificaPrimo(int(num))