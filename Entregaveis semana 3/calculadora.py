"""Módulo com operações matemáticas básicas."""

PI = 3.14159


def somar(primeiro_numero, segundo_numero):
    """Retorna a soma de dois números."""
    return primeiro_numero + segundo_numero


def subtrair(primeiro_numero, segundo_numero):
    """Retorna a subtração de dois números."""
    return primeiro_numero - segundo_numero


def multiplicar(primeiro_numero, segundo_numero):
    """Retorna a multiplicação entre dois números."""
    return primeiro_numero * segundo_numero


def dividir(dividendo, divisor):
    """Retorna a divisão ou uma mensagem se o divisor for zero."""
    # Esta condição evita que o programa pare com ZeroDivisionError.
    if divisor == 0:
        return "Erro: não é possível dividir por zero."

    return dividendo / divisor
