#1. Crie um algoritmo que leia o valor gasto com despesas realizadas em um
# restaurante e escreva o valor da gorjeta (10%) e o valor total com a gorjeta.

v_gast = float(input("Qual o valor gasto (R$)? "))
gorjeta = v_gast * 0.10
v_total = v_gast + gorjeta
print ("Sua conta: R$",v_total)
print ("O valor pago de gorjeta (10%) foi: R$",gorjeta)