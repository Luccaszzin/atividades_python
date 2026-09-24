idade = int(input("Digite a idade do cliente: "))
renda = float(input("Digite a renda anual do cliente: R$ "))

# Menores de idade não entram nas categorias definidas neste exemplo.
if idade < 18:
    categoria = "Não classificado: é necessário ter 18 anos ou mais."
elif renda >= 1_000_000:
    categoria = "Diamante"
elif renda >= 500_000:
    categoria = "Ouro"
elif renda >= 100_000:
    categoria = "Prata"
elif renda >= 50_000:
    categoria = "Bronze"
else:
    categoria = "Não classificado"

print(f"Categoria do cliente: {categoria}")
