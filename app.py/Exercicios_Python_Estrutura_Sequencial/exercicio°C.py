#9 Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura
# em graus Celsius. C = 5 * ((F-32) / 9).
n11 = float(input("Digite Temperatura em Fahrenheit °F "))
C = (5*(n11-32)/9)
print("Sua temperatura é ",C,"°C" )

#10 Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
n12 = float(input("Digite Sua Temperatura °C "))
f = (n12*9/5)+32 
print("Sua Temperatura em Fahreinheit é ", f ,"°F")