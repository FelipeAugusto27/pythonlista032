'''
Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês
(em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, exibir ao final o seu nome,
o salário fixo, a comissão e o salário completo (fixo + comissão de vendas) no final do mês
'''

# Input
nome = input("Informe o nome do vendedor: ")
salario = float(input("Informe o salário fixo: R$ "))
vendas = float(input("Informe o valor total em vendas: R$"))

# Processamento
ganho = salario + (vendas * 17/100)

# Output
print(f"Vendedor: {nome}")
print(f"Salário R${salario:.2f}")
print(f"Comissão: 15%")
print(f"Salário + comissão: R${ganho:.2f}")
