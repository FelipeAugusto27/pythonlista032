'''
Desenvolver um programa que pergunte ao usuário o seu peso e sua altura.
Ao final o programa deverá exibir na tela o IMC dessa pessoa. OBS: Peso em kg e altura em M
'''

# Input
kg = float(input("Informe seu em Kg:"))
m = float(input("Informe sua altura em M:"))

# Processamento
imc = kg / pow(m,2)

# Output
print(f"Seu Indice de Massa Corporea é de {imc:.1f}")