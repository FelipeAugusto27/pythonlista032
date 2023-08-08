'''
Escreva um algoritmo que pergunte o número total de eleitores de um município, número de votos em branco, nulos e válidos
e apresente como resposta o percentual que cada um representa em relação ao total de eleitores.
'''

# Input
eleitores = int(input("Informe o número de eleitores: "))  # 100%
brancos = int(input("Informe o números de votos em branco: "))  # x/100
nulos = int(input("Informe o números de votos nulos: "))

# Processamento
percentual_brancos = (brancos*100) / eleitores
percentual_nulos = (nulos*100) / eleitores

# Output
print(f"O percentual de brancos é de: {percentual_brancos:.0f}%")
print(f"O percentual de nulos é de: {percentual_nulos:.0f}%")
