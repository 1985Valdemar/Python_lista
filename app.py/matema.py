#Neste quiz você fará alguns cálculos para um ladrilhador. Duas partes de um piso precisam de ladrilhos. Uma parte tem 9 peças de largura por 7 peças de comprimento , a outra tem 5 peças de largura por 7 peças de comprimento . As peças vêm em pacotes de 6.

#Quantas peças são necessárias?
#Você compra 17 pacotes de peças contendo 6 peças cada . Quantas peças sobrarão?



# Dimensões das duas partes do piso
parte1_largura = 9
parte1_comprimento = 7
parte2_largura = 5
parte2_comprimento = 7

# Número de peças em um pacote
peças_por_pacote = 6

# Calcular o número total de peças necessárias para cada parte
peças_necessárias_parte1 = parte1_largura * parte1_comprimento
peças_necessárias_parte2 = parte2_largura * parte2_comprimento

# Calcular o número total de peças necessárias
total_peças_necessárias = peças_necessárias_parte1 + peças_necessárias_parte2

# Quantidade de pacotes comprados
pacotes_comprados = 17

# Calcular quantas peças sobrarão
peças_sobrando = (pacotes_comprados * peças_por_pacote) - total_peças_necessárias

# Exibir os resultados
print("Número total de peças necessárias:", total_peças_necessárias)
print("Quantidade de peças sobrando:", peças_sobrando)