'''
Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o valor com o acrescimo dos 10% da gorjeta do garçom.
'''

# Input
conta = float(input("Insira o valor da conta: "))

# Processamento
pagar = conta + (conta * 10/100)

# Output
print(f"O valor a pagar (com gorjeta) será de R${pagar:.2f}")
