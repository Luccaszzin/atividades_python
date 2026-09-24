# Mostra as opções que o usuário pode escolher.
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = int(input("Escolha uma operação: "))
primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

# match/case escolhe o bloco de código conforme a opção digitada.
match opcao:
    case 1:
        resultado = primeiro_numero + segundo_numero
        print(f"Resultado da soma: {resultado}")
    case 2:
        resultado = primeiro_numero - segundo_numero
        print(f"Resultado da subtração: {resultado}")
    case 3:
        resultado = primeiro_numero * segundo_numero
        print(f"Resultado da multiplicação: {resultado}")
    case 4:
        # A divisão por zero precisa ser tratada antes da operação.
        if segundo_numero == 0:
            print(f"Erro: não é possível dividir {primeiro_numero} por zero.")
        else:
            resultado = primeiro_numero / segundo_numero
            print(f"Resultado da divisão: {resultado}")
    case _:
        print(f"A opção {opcao} é inválida.")
