# Pede ao usuário o nome que será invertido.
nome = input("Digite seu nome: ")

# [::-1] percorre a string do último caractere até o primeiro.
nome_invertido = nome[::-1]

# Mostra o resultado para o usuário.
print(f"Nome invertido: {nome_invertido}")
