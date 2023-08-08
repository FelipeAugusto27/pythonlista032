'''
A loja Mamão com Açucar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que pergunte
o valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das prestações.
'''

# Input
valor = float(input("Insira o valor da compra: R$"))
pres = float(input("Insira o número de prestações: "))

# Processamento
total = valor / pres

#Output
print(f"O valor de cada prestação será de R${total:.2f}")
