#17 Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
# da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, 
# que custam R$ 25,00.

m2 = float(input("Digite m3 Por Gentileza "))

#tinta 1L cada 3m lata18L
tinta = m2*1
print(tinta,"m2")
#lata 18L 80$ quantidade latas
#Lata 3.6L 25$
lata = 18*6
lata_pequena = 3.6*6
print(lata,"m2 Uma lata 18L pinta")
print(lata_pequena,"m2 uma lata 3.6L Pinta")
print()
#Quantidade latas tintas
quantia_lata = int( m2 / lata)
quantia_lata_pequena = int(m2 / lata_pequena)

#Condição para arrendondar valor devido lata de 3.6L ou 18L
if quantia_lata_pequena != int:
    quantia_lata_pequena += 1

if quantia_lata != int:
    quantia_lata += 1
print(quantia_lata,"lata 18L")
print(lata*quantia_lata,"Total m2 consegue pintar com lata 18L")
print()
print(quantia_lata_pequena,"Lata de 3.6L")
print(lata_pequena*quantia_lata_pequena,"Total m2 consegue pintar com lata 3.6L")
print()
#preco total
total = quantia_lata*80
total_pequena = quantia_lata_pequena*25
print("R$ ",total,"Lata 18L")
print("R$ ",total_pequena,"Lata 3.6L")
