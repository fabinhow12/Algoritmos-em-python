dba__author__ = 'fabio'

#Função que faz Todas as Somas
def somaCodigo(codigo):
 somaDigitosImpar = (int(codigo[0])) + (int(codigo[2])) + (int(codigo[4])) + (int(codigo[6])) + (int(codigo[8])) + (int(codigo[10]))
 somaDigitosPar = (int(codigo[1])) + (int(codigo[3])) + (int(codigo[5])) + (int(codigo[7])) + (int(codigo[9])) + (int(codigo[11]))
 somaDigitosTotal = somaDigitosImpar + (3*somaDigitosPar)

 return somaDigitosTotal

#Função que verifica o ultimo digito a partir da soma
def verificaUltD(somadigitos):
    divisor = 10
    x = 0
    for x in range(0,9):
        if (somadigitos + x) % divisor == 0:
            getnum = (somadigitos + x) / divisor
            #Multiplica o valor por 10 para fazer a subtração com as somas
            getnum= getnum*10

    numVerificador = getnum


    return numVerificador

codigo = str(input("Digite O Código de Barras: "))

#Validação Básica de quatidades de digitos e algumas letras
if (len(codigo)>13):
    print("Quantidades de digitos acima de 13")
elif(len(codigo)<=0):
    print("Nenhum número digitado")
elif ("a" in codigo or "b" in codigo or "c" in codigo or "d" in codigo or "e" in codigo or "f" in codigo):
     print("Não Pode Ter Letras Apenas Números")
else:

   #Variável Que Recebe O Valor Da Função
   somadigitos = somaCodigo(codigo)
   print("A Soma De Todos Os Digitos:",somadigitos)

   #Variavél Que Recebe O Valor Da Função
   numVerificador = verificaUltD(somadigitos)
   print("Número Multiplo de 10:",numVerificador)

   #Variavel que recebe O Valor da verificação
   resultado = numVerificador - somadigitos
   print("Número Para Verificar: ",resultado)

   if resultado == (int(codigo[12])):
    print("\n=====================================")
    print("O Código de Barras é Válido")
    print("O Número de Verificação é:",resultado)
    print("=====================================")
   else:
    print("=============================")
    print("O Código de barras É Inválido")
