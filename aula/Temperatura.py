__author__ = 'Fábio Henrique E Walison Filipe'

print("Escalas Termométricas")
print("")
print("")

escolha = str(input("Escolha a escala da temperatura:\n"
                    "1- Celsius\n"
                    "2- Farenheit\n"
                    "3- Kelvin\n"
                    "Digite Sua Opção: "))


print("")

#Celsius
if escolha=="1":
     tempCelsius= float(input("Digite A Temperatura em Celsius: "))
     celsiusParaFare = (9*tempCelsius +160)/5
     print("A Temperatura em Farenheit é %4.2f" %(celsiusParaFare) )
     celsiusParaKelvin = tempCelsius + 273
     print("A Temperatura em Kelvin é %4.2f" %(celsiusParaKelvin))

#Farenheit
if escolha=="2":
    tempFare = float(input("Digite A Temperatura em Farenheit: "))
    fareParaCel =  ((5*tempFare)-160)/9
    print("A Temperatura Em Celsius é %4.2f" %(fareParaCel))
    fareParaKelvin = fareParaCel + 273
    print("A Temperatura Em Kelvin é %4.2f" %(fareParaKelvin))

#Kelvin
if escolha=="3":
    tempKelvin = float(input("Digite A Temperatura Em Kelvin: "))
    kelvinParaCel = tempKelvin+273
    print("A Temperatura em Celsius é %4.2f" %(kelvinParaCel))
    kelvinParaFare = (9*kelvinParaCel +160)/5
    print("A Temperatura em Faranheit é %4.2f" %(kelvinParaFare))
