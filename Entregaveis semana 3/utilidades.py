"""Funções reutilizáveis para os desafios da Semana 03."""


def converter_temperatura(celsius):
    """Converte graus Celsius para Fahrenheit e Kelvin."""
    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15
    # Um dicionário permite devolver os dois resultados juntos.
    return {"fahrenheit": fahrenheit, "kelvin": kelvin}


def validar_senha(senha):
    """Retorna True para senha com 8 caracteres, letra e número."""
    tem_tamanho_minimo = len(senha) >= 8
    tem_letra = any(caractere.isalpha() for caractere in senha)
    tem_numero = any(caractere.isdigit() for caractere in senha)
    return tem_tamanho_minimo and tem_letra and tem_numero


def calcular_total_caixa(*precos):
    """Recebe vários preços e retorna a soma deles."""
    # *precos reúne os valores recebidos em uma tupla.
    if any(preco < 0 for preco in precos):
        return "Erro: os preços não podem ser negativos."
    return sum(precos)


def criar_ficha_aluno(**dados):
    """Cria uma ficha de aluno com informações nomeadas."""
    # **dados reúne pares como nome="Lucas" em um dicionário.
    return dados.copy()


def adicionar_item_seguro(lista_original, novo_item):
    """Adiciona um item em uma cópia, sem alterar a lista original."""
    # list(...) cria uma cópia defensiva da lista recebida.
    nova_lista = list(lista_original)
    nova_lista.append(novo_item)
    return nova_lista
