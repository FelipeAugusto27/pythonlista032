'''
Desenvolver um programa que faça duas perguntas:
O valor referente às horas atuais
E o valor referente aos minutos atuais.
Exemplo: Se forem 09:35 o usuário deverá informar como resposta às horas atuais o valor 09 e como resposta os minutos atuais o valor 35.
Em seguida o programa deverá informar como resposta quantos minutos já se passaram desde às 00:00 deste dia.
'''

# Input
h = int(input("Informe as horas: "))
min = int(input("Informe os minutos "))

# Processamento
total = min + (h * 60)

# Output
print(f"Passaram se {total} minutos até o horário informado.")
