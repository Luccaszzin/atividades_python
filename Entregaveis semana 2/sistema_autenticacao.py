senha_correta = "Python123"
tentativas = 0
limite_tentativas = 3
acesso_liberado = False

# O laço continua enquanto houver tentativas disponíveis.
while tentativas < limite_tentativas:
    senha_digitada = input("Digite a senha: ")

    if senha_digitada == senha_correta:
        acesso_liberado = True
        print(f"Acesso liberado na tentativa {tentativas + 1}.")
        break

    # A variável de controle é atualizada para evitar um laço infinito.
    tentativas += 1
    tentativas_restantes = limite_tentativas - tentativas
    print(f"Senha incorreta. Tentativas restantes: {tentativas_restantes}.")

if not acesso_liberado:
    print(f"Acesso bloqueado após {limite_tentativas} tentativas incorretas.")
