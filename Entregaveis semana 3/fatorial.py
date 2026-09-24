"""Exemplo de fatorial usando recursão."""


def fatorial(numero):
    """Calcula o fatorial de um número inteiro não negativo."""
    if numero < 0:
        raise ValueError("O fatorial não existe para números negativos.")

    # Caso-base: é a condição que encerra as chamadas da função.
    if numero == 0 or numero == 1:
        return 1

    # Parte recursiva: a função chama a si mesma com um número menor.
    # Em Portugol, o equivalente normalmente usaria uma repetição "enquanto".
    return numero * fatorial(numero - 1)


if __name__ == "__main__":
    # O exemplo não é executado quando outro arquivo importa este módulo.
    numero_escolhido = 5
    print(f"{numero_escolhido}! = {fatorial(numero_escolhido)}")
