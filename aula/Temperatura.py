__author__ = 'Fábio Henrique E Walison Filipe'


def verifica_celsius():
    tempCelsius = float(input("Digite A Temperatura em Celsius: "))
    celsiusParaFare = (9 * tempCelsius + 160) / 5
    print("A Temperatura em Farenheit é %4.2f" % (celsiusParaFare))
    celsiusParaKelvin = tempCelsius + 273
    print("A Temperatura em Kelvin é %4.2f" % (celsiusParaKelvin))


def verifica_fare():
    tempFare = float(input("Digite A Temperatura em Farenheit: "))
    fareParaCel = ((5 * tempFare) - 160) / 9
    print("A Temperatura Em Celsius é %4.2f" % (fareParaCel))
    fareParaKelvin = fareParaCel + 273
    print("A Temperatura Em Kelvin é %4.2f" % (fareParaKelvin))


def verifica_kelvin():
    tempKelvin = float(input("Digite A Temperatura Em Kelvin: "))
    kelvinParaCel = tempKelvin + 273
    print("A Temperatura em Celsius é %4.2f" % (kelvinParaCel))
    kelvinParaFare = (9 * kelvinParaCel + 160) / 5
    print("A Temperatura em Faranheit é %4.2f" % (kelvinParaFare))


print("Escalas Termométricas\n")

escolha = str(input("Escolha a escala da temperatura:\n"
                    "1- Celsius\n"
                    "2- Farenheit\n"
                    "3- Kelvin\n"
                    "Digite Sua Opção: "))

print("")

# Celsius
if escolha == "1":
    verifica_celsius()
# Farenheit
if escolha == "2":
    verifica_fare()
# Kelvin
if escolha == "3":
    verifica_kelvin()
#Escolha Diferente Das 3
if escolha != "1" and escolha != "2" and escolha != "3":
    print("Escolha Inválida")
