#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário
#de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento 
#de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa
#que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso_peixes = float(input("Digite o peso dos peixes em quilos: "))

# Define o limite estabelecido
limite_peso = 50.0

# Calcula o excesso de peso, se houver
if peso_peixes > limite_peso:
    excesso = peso_peixes - limite_peso
    multa = excesso * 4.0
else:
    excesso = 0
    multa = 0

# Exibe os resultados
if excesso > 0:
    print(f"João Papo-de-Pescador excedeu o limite em {excesso} quilos.")
    print(f"O valor da multa a ser pago é de R$ {multa:.2f}.")
else:
    print("João Papo-de-Pescador não excedeu o limite de peso. Nenhuma multa é necessária.")

