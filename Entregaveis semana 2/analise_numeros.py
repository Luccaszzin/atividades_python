numeros = []

# range(1, 6) repete cinco vezes: 1, 2, 3, 4 e 5.
for posicao in range(1, 6):
    numero = float(input(f"Digite o {posicao}º número: "))
    numeros.append(numero)

soma = sum(numeros)
media = soma / len(numeros)
maior_numero = max(numeros)
menor_numero = min(numeros)

print(f"Soma: {soma}")
print(f"Média: {media:.2f}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
