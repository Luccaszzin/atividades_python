N = int(input("Digite um número: ")) #input para o usuario colocar o valor em segundos
horas = N // 3600 #calcula o número de horas
minutos = (N % 3600) // 60 #calcula o número de minutos
segundos = N % 60 #calcula o número de segundos
print(f"{horas}:{minutos}:{segundos}") #print para o usuario ver o tempo em horas, minutos e segundos