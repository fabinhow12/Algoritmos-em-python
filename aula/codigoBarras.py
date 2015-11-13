dba__author__ = 'fabio'

#Função Que Verifica de qual País é o Código
def verifica_pais(codigo):

    #Variável Para Retornar Nome Do País
    pais = ""

    if codigo >= 2 and codigo <= 139:
        pais = "EUA"
    elif 300 <= codigo <= 379:
        pais = "França"
    elif codigo == 380:
        pais = "Bulgaria"
    elif codigo == 383:
        pais = "Eslovênia"
    elif codigo == 385:
        pais = "Croácia"
    elif codigo == 387:
        pais = "Bósnia e Herzegovina"
    elif 400 <= codigo <= 440:
        pais = "Alemanhã"
    elif 450 <= codigo <= 459:
        pais = "Japão"
    elif 490 <= codigo <= 499:
        pais = "Japão"
    elif 460 <= codigo <= 469:
        pais = "Rússia"
    elif codigo == 470:
        pais = "Quirguistão"
    elif codigo == 471:
        pais = "Ilha de Taiwan"
    elif codigo == 474:
        pais = "Estônia"
    elif codigo == 475:
        pais = "Letônia"
    elif codigo == 476:
        pais = "Azerbaijão"
    elif codigo == 477:
        pais = "Lituânia"
    elif codigo == 478:
        pais = "Usbequistão"
    elif codigo == 479:
        pais = "Sri Lanka"
    elif codigo == 480:
        pais = "Filipinas"
    elif codigo == 481:
        pais = "Bielorrússia"
    elif codigo == 482:
        pais = "Ucrânia"
    elif codigo == 484:
        pais = "Moldávia"
    elif codigo == 485:
        pais = "Armênia"
    elif codigo == 486:
        pais = "Géorgia"
    elif codigo == 487:
        pais = "Cazaquistão"
    elif codigo == 489:
        pais = "Hong Kong"
    elif 500 <= codigo <= 509:
        pais = "Reino Unido"
    elif codigo == 520:
        pais = "Grécia"
    elif codigo == 528:
        pais = "Líbano"
    elif codigo == 529:
        pais = "Chipre"
    elif codigo == 530:
        pais = "Albânia"
    elif codigo == 531:
        pais = "República da Macêdonia"
    elif codigo == 535:
        pais = "Malta"
    elif codigo == 539:
        pais = "República da Irlanda"
    elif 540 <= codigo <= 549:
        pais = "Bélgica"
    elif codigo == 560:
        pais = "Portugal"
    elif codigo == 569:
        pais = "Islândia"
    elif 570 <= codigo <= 579:
        pais = "Dinamarca"
    elif codigo == 590:
        pais = "Polónia"
    elif codigo == 594:
        pais = "Romênia"
    elif codigo == 599:
        pais = "Hungria"
    elif 600 <= codigo <= 601:
        pais = "África do Sul"
    elif codigo == 603:
        pais = "Gana"
    elif codigo == 608:
        pais = "Bahrein"
    elif codigo == 609:
        pais = "Ilhas Maurício"
    elif codigo == 611:
        pais = "Marrocos"
    elif codigo == 613:
        pais = "Argélia"
    elif codigo == 616:
        pais = "Quênia"
    elif codigo == 618:
        pais = "Costa do Marfim"
    elif codigo == 619:
        pais = "Tunísia"
    elif codigo == 621:
        pais = "Síria"
    elif codigo == 622:
        pais = "Egito"
    elif codigo == 624:
        pais = "Líbia"
    elif codigo == 625:
        pais = "Jordânia"
    elif codigo == 626:
        pais = "Irã"
    elif codigo == 627:
        pais = "Kuwait"
    elif codigo == 628:
        pais = "Arábia Saudita"
    elif codigo == 629:
        pais = "Emirados Árabes"
    elif 640 <= codigo <= 649:
        pais = "Finlândia"
    elif 690 <= codigo <= 699:
        pais = "China"
    elif 700 <= codigo <= 709:
        pais = "Noruega"
    elif codigo == 729:
        pais = "Israel"
    elif 730 <= codigo <= 739:
        pais = "Suécia"
    elif codigo == 740:
        pais = "Guatemala"
    elif codigo == 741:
        pais = "El Salvador"
    elif codigo == 742:
        pais = "Honduras"
    elif codigo == 743:
        pais = "Nicarágua"
    elif codigo == 744:
        pais = "Costa Rica"
    elif codigo == 745:
        pais = "Panamá"
    elif codigo == 746:
        pais = "República Dominicana"
    elif codigo == 750:
        pais = "México"
    elif 754 <= codigo <= 755:
        pais = "Canadá"
    elif codigo == 759:
        pais = "Venezuela"
    elif 760 <= codigo <= 769:
        pais = "Suiça"
    elif codigo == 770:
        pais = "Colômbia"
    elif codigo == 773:
        pais = "Uruguai"
    elif codigo == 775:
        pais = "Peru"
    elif codigo == 777:
        pais = "Bolívia"
    elif codigo == 779:
        pais = "Argentina"
    elif codigo == 780:
        pais = "Chile"
    elif codigo == 784:
        pais = "Paraguai"
    elif codigo == 786:
        pais = "Equador"
    elif 789 <= codigo <= 790:
        pais = "Brasil"
    elif 800 <= codigo <= 839:
        pais = "Itália"
    elif 840 <= codigo <= 849:
        pais = "Espanha"
    elif codigo == 850:
        pais = "Cuba"
    elif codigo == 858:
        pais = "Eslováquia"
    elif codigo == 859:
        pais = "Républica Checa"
    elif codigo == 860:
        pais = "Sérvia"
    elif codigo == 865:
        pais = "Mongólia"
    elif codigo == 867:
        pais = "Coréia do Norte"
    elif codigo == 869:
        pais = "Turquia"
    elif 870 <= codigo <= 879:
        pais = "Holanda"
    elif codigo == 880:
        pais = "Coréia do Sul"
    elif codigo == 884:
        pais = "Cambdoja"
    elif codigo == 885:
        pais = "Tailândia"
    elif codigo == 888:
        pais = "Singapura"
    elif codigo == 890:
        pais = "Índia"
    elif codigo == 893:
        pais = "Vietnam"
    elif codigo == 899:
        pais = "Indonésia"
    elif 900 <= codigo <= 919:
        pais = "Áustria"
    elif 930 <= codigo <= 939:
        pais = "Austrália"
    elif codigo == 955:
        pais = "Malásia"
    elif codigo == 958:
        pais = "Macau"

    return pais

# Função que faz Todas as Somas
def somaCodigo(codigo):
    somaDigitosImpar = (int(codigo[0])) + (int(codigo[2])) + (int(codigo[4])) + (int(codigo[6])) + (int(codigo[8])) + (int(codigo[10]))
    somaDigitosPar = (int(codigo[1])) + (int(codigo[3])) + (int(codigo[5])) + (int(codigo[7])) + (int(codigo[9])) +(int(codigo[11]))
    somaDigitosTotal = somaDigitosImpar + (3 * somaDigitosPar)

    return somaDigitosTotal

# Função que verifica o ultimo digito a partir da soma
def verificaUltD(somadigitos):

    for x in range(0, 10):
        if (somadigitos + x) % 10 == 0:
            numVerificador = x
            break

    return numVerificador


print("\n========================================")
print("VERIFICADOR DE CÓDIGO DE BARRAS EAN13")
print("========================================")

# Variável Que Recebe O Valor de Código de Barras
codigo = str(input("Digite o código de barras: "))

# Variável QUe Recebe O PAÍS
in_pais = str(input("Digite o país Onde o produto foi feito: "))


# Validação Dos Valores Recebidos
if codigo.isdigit():

    if len(codigo) == 13:

        # Variável Que Recebe O Valor Da Função Soma
        somadigitos = somaCodigo(codigo)

        # Variavél Que Recebe O Número Verificador
        numVerificador = verificaUltD(somadigitos)

        #Lógica Para Saber os 3 Digitos Dos Países
        if codigo[0:1] == "0":
            codigo_absoluto = codigo[2]
        elif codigo[0] == "0":
            codigo_absoluto = codigo[1:2]
        else:
            codigo_absoluto = codigo[0:3]

        #Variável Para Verificação Do País
        paisve = verifica_pais(int(codigo_absoluto))

        if numVerificador == (int(codigo[12])):
            print("\n==============================================================")
            print("O Código de Barras é Válido")

            if paisve.lower() == in_pais.lower():
                print("O código do país é:", int(codigo[0:3]),"e foi feito no(a): "+paisve)

            else:
                print("O produto não foi feito No(a):",in_pais+", foi feito no(a): "+paisve)

            print("O Código da Empresa é:", int(codigo[3:7]))
            print("O Código do Produto é:", int(codigo[7:12]))
            print("O Número de verificação é:", int(numVerificador))
            print("==============================================================")
        else:
            print("=======================================")
            print("O Código de barras é Inválido")
            print("=======================================")

    else:
       print("É preciso ter 13 digitos para verificação")

else:
    print("O Código só deve ter números")