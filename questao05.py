'''
Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: A soma dos dois números,
a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a multiplicação entre os dois
números, a divisão do primeiro pelo segundo número, e também o resto da divisão do primeiro pelo segundo.
'''

# Input
a = float(input("Informe um valor para a:"))
b = float(input("Informe um valor para b:"))

# Processamento
'''
Eu posso fazer assim (criando novas variáveis ou fazer no print).
soma = a + b
sub = a - b
sub2 = b - a
mult = a * b
div = a / b
rest = a // b
'''

# Output
print(f"a+b= {a+b}")
print(f"a-b= {a-b}")
print(f"b-a= {b-a}")
print(f"a*b= {a*b}")
print(f"a/b= {a/b}")
print(f"a//b= {a//b}")
