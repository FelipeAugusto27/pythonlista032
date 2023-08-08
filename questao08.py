'''
Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda.
Sabendo que o preço de receberá um acrescimo de acordo com um percentual informado pelo usuário.
'''

# Input
custo = float(input("Informe o custo de um produto R$"))
acrescimo = float(input("Informe o percentual de acrescimo (sem '%'):"))

# Processamento
pagar = custo + (custo * acrescimo / 100)

# Output
print(f"O valor de venda do produto será de R${pagar:.2f}")
6