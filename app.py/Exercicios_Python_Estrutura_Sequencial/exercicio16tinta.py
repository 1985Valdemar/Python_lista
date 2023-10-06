#16 Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
# da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades 
# de latas de tinta a serem compradas e o preço total.
#Metros Quadrados
m2 = float(input("Digite m3 Por Gentileza "))

#tinta 1L cada 3m lata18L
tinta = m2*1
print(tinta,"m2")
#lata 18L 80$ quantidade latas
lata = 18*3
print(lata,"m2 Uma lata pinta")
quantia_lata = int( m2 / lata)
if quantia_lata != int:
    quantia_lata += 1
print(quantia_lata,"lata 18L")
#preco total
total = quantia_lata*80
print("R$ ",total)