__author__ = 'Fábio Henrique e Walison Filipe'

print("Programa De Figura Geométrica")
print("")
print("")


escolha = str(input(" Escolha Uma Opção\n "
                    "1-Área\n"
                    " 2-Volume\n"
                    "Digite Sua Opção: "))


#Calcula A área
if escolha=="1" :
      print("")

      figura = str(input("Escolha A Figura Geométrica:\n"
                   "1- Quadrado\n"
                   "2- Retângulo\n"
                   "3- Círculo\n"
                   "4- Triângulo\n"
                   "5- Paralelogramo\n"
                   "6- Losangulo\n"
                         "Digite Sua Opção: "))

      print("")

      #Quadrado
      if figura=="1":
          lado1 = float(input("Digite O Tamanho Do Primeiro Lado: "))
          lado2 = float(input("Digite O Tamanho Do Outro Lado: "))
          areaQuadrado= lado1*lado2
          print("A área  Do Quadrado é %3.2f Unidades De Área" %(areaQuadrado))
      #Retangulo
      if figura=="2":
          ladomenor = float(input("Digite O Tamanho Do Menor Lado:"))
          ladoMaior = float(input("Digite O Tamanho DO Maior Lado:"))
          areaRetangulo = ladomenor*ladoMaior
          print("A área Do Retângulo é %4.2f Unidades De Área" %(areaRetangulo))

      #Círculo
      if figura=="3":
          raio = float(input("Digite O Raio do Círculo: "))
          areacirculo = raio*(3.14*3.14)
          print("A área Do Círculo é %4.2f Unidades De Área" %(areacirculo) )

      #Triangulo
      if figura=="4":
         base = float(input("Digite A Base Do Triângulo: "))
         altura = float(input("Digite A Altura Do Triângulo: "))
         areaTriangulo = (base*altura)/2
         print("A área Do Triângulo é %4.2f Unidades De Área" %(areaTriangulo))

      #Paralelogramo
      if figura=="5":
          baser = float(input("Digite A Base Do Paralelogramo: "))
          alturar = float(input("Digite A Altura Do Paralelogramo: "))
          areaParalelogramo= baser*alturar
          print("A área do Paralelogramo %4.2f Unidades De Área" %(areaParalelogramo))

      #Losangulo
      if figura=="6":
          D = float(input("Digite A Diagonal Maior: "))
          d = float(input("Digite A Diagonal Menor: "))

          areaLosangulo = (D*d)/2
          print("A Área Do Losangulo  é %4.2f Unidades De Área" %(areaLosangulo))


#Calcula Volume
print("")

if escolha=="2":
    figura = str(input("Escolha A Figura Geométrica: \n"
                       "1- Esfera\n"
                       "2- Pirâmide\n"
                       "3- Prisma\n"
                       "4- Cilindro\n"
                       "Digite Sua Opção: "))
    print("")

    #Volume Esfera
    if figura=="1":
        raioe= float(input("Digite O Raio Da Esfera: "))
        volumeEsfera = (4*3.14*(raioe*raioe*raioe))/3
        print("O Volume Da Esfera é %4.2f Unidades De Volume" %(volumeEsfera))

    #Volume Pirâmide
    if figura=="2":
       areaBasep = float(input("Digite Um Valor Para A Área Da Base Da Pirâmide: "))
       alturap = float(input("DIgite A Altura Da Pirâmide: "))
       volumePiramide = (1/3)*areaBasep*alturap
       print("O Volume Da Pirâmide É %4.2f Unidades De Volume" %(volumePiramide))

    #Volume Prisma
    if figura=="3":
        areaprisma = float(input("Digite A Área Da base Do Prisma: "))
        altprisma = float(input("Digite A Altura Do Prisma: "))
        volumeprisma = areaprisma*altprisma
        print("O Volume do Prisma é %4.2f Unidades De Volume" %(volumeprisma))

    #Volume Cílindro
    if figura=="4":
        raioCilindro = float(input("Digite O Raio da Aréa Da Base Do Cilindro: "))
        areacilindro = 3.14*(raioCilindro*raioCilindro)
        alturaCilindro = float(input(("Digite A Altura Do Cílindro: ")))
        volumecilindro = areacilindro*alturaCilindro
        print("O Volume Do Cílindro É %4.2f Unidades De Volume" %(volumecilindro) )


