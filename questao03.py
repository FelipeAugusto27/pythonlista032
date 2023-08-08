'''
Desenvolver um programa que pergunte ao usuário seu peso (em kg) e sua altura (em metros).
Ao final o programa deverá exibir na tela para o usuário o valor do peso informado em g e sua altura em cm.
'''

# Input
kg = float(input("Informe seu peso (Kg): "))
m = float(input("informe sua altura (M): "))

# Processamento
g = kg * 1000
cm = m * 100

# Output
print(f"Seu peso em gramas é de: {g}")
print(f"Sua altura em cm é de: {m}")
