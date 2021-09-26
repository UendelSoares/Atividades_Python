#2. Fazer um algoritmo que leia o valor do salário mínimo e o valor do salário de uma
#pessoa. Calcular e escrever quantos salários mínimos essa pessoa ganha.

salario = float(input("Qual seu salario (R$)? "))
s_min = 1100
if (salario < s_min):
    print("Você recebe menos que um salario minimo")
else:
    t_salario = salario / s_min
print (f"Você recebe {t_salario:.2f} em salarios minimos")