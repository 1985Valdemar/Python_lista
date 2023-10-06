#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58 mulher (62.1 * altura) - 44.7

def calcular_peso_ideal(altura, genero):
    if genero == "homem":
        peso_ideal = (72.7 * altura) - 58
    elif genero == "mulher":
        peso_ideal = (62.1 * altura) - 44.7
    else:
        peso_ideal = None
    return peso_ideal

while True:
    print("Calculadora de Peso Ideal")
    print("1. Calcular para Homem")
    print("2. Calcular para Mulher")
    print("3. Sair")

    escolha = input("Escolha uma opção (1/2/3): ")

    if escolha == "1":
        altura = float(input("Digite a altura em metros: "))
        peso_ideal = calcular_peso_ideal(altura, "homem")
        print(f"O peso ideal para um homem com altura {altura}m é aproximadamente {peso_ideal} kg")
    elif escolha == "2":
        altura = float(input("Digite a altura em metros: "))
        peso_ideal = calcular_peso_ideal(altura, "mulher")
        print(f"O peso ideal para uma mulher com altura {altura}m é aproximadamente {peso_ideal} kg")
    elif escolha == "3":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
    