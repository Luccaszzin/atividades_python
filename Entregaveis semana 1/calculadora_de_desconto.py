valor = float(input("Digite o valor do produto: ")) #input para o usuario colocar o valor do produto
desconto = float(input("Digite o valor do desconto: ")) #input para o usuario colocar o valor do desconto
preco_final = valor - (valor * desconto / 100) #calcula o valor final do produto

print(f"O valor final do produto é: {preco_final:.2f}")