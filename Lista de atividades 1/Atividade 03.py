#3. Criar um algoritmo que efetue o cálculo da quantidade de litros de combustível
# gastos em uma viagem, sabendo-se que o carro faz 12 km com um litro. Deverão
# ser fornecidos o tempo gasto na viagem e a velocidade média. Distância = Tempo *
# Velocidade. Litros = Distância / 12. O algoritmo deverá apresentar os valores da
# distância percorrida e a quantidade de litros utilizados na viagem.

temp = int(input("Qual tempo gasto na viagem? "))
vm = int(input("Velocidade media: "))
dist = temp * vm
litros = dist / 12
print("Sua distancia percorrida foi: ",dist,"Km")
print(f"A quantidade de litros gastos foi: {litros:.2f} Litros")