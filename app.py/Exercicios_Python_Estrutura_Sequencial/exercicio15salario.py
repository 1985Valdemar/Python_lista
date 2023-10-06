#15 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
# o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
n10 = float(input("Digite Valor sua Hora "))
n11 = float(input("Quantas horas trabalhou mes "))
bruto = (n10*n11)
vale = (n10*n11)*0.40

#a)salário bruto.
sb = bruto
#b)quanto pagou ao INSS + IR
inss = sb * 0.08
ir = sb * 0.11
#c)quanto pagou ao sindicato.
sind = sb * 0.05
#d)o salário líquido.
sl = sb - (ir + inss + sind)
#e)calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto Descontar : R$
print(f"Seu Salario Bruto a Descontar R$ {sb:.2f}")
#- IR (11%) : R$
print(f"Será Descontado IR R$ {ir:.2f} ")
#- INSS (8%) : R$
print(f"Será Descontado INSS R$ {inss:.2f}")
#- Sindicato ( 5%) : R$
print(f"Será Descontado Sindicato R$ {sind:.2f}")
#= Salário Liquido : R$
print(f"Seu Salario Liquido Será R$ {sl:.2f}" )
#Obs.: Salário Bruto - Descontos = Salário Líquido.