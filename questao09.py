'''
Faça o algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas em dias.
Obs: Considere que 1 ano tem 365 dias.
'''

# Input
anos = int(input("Informe seus anos de idade: "))
meses = int(input("Informe os meses de idade (considerando os anos informados): "))
dias = int(input("Informe os dias de idade (Considerando anos e meses informados): "))

# Processamento
ano_para_dia = (anos * 365)
mes_para_dia = (meses * 30)
total = mes_para_dia + ano_para_dia + dias

# Output
print(f"total:{total:.0f}")