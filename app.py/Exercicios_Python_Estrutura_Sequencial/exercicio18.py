#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link
# de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link 
# (em minutos).
# Solicita o tamanho do arquivo para download em MB
tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))

# Solicita a velocidade da conexão à Internet em Mbps
velocidade_internet_mbps = float(input("Digite a velocidade da conexão à Internet (em Mbps): "))

# Converte a velocidade de Mbps para MB por segundo
velocidade_internet_mb_por_segundo = velocidade_internet_mbps / 8

# Calcula o tempo de download em segundos
tempo_download_segundos = tamanho_arquivo_mb / velocidade_internet_mb_por_segundo

# Converte o tempo de download em minutos
tempo_download_minutos = tempo_download_segundos / 60

# Exibe o resultado
print(f"O tempo aproximado de download do arquivo é de {tempo_download_minutos:.2f} minutos.")