"""Funções simples para calcular média, mediana e moda."""

import statistics as est


def calcular_estatisticas(numeros):
    """Retorna a média, a mediana e a moda de uma lista de números."""
    if not numeros:
        raise ValueError("A lista de números não pode estar vazia.")

    return {
        "media": est.mean(numeros),
        "mediana": est.median(numeros),
        "moda": est.multimode(numeros),
    }


if __name__ == "__main__":
    # Este exemplo só roda quando estatistica.py é executado diretamente.
    valores = [7, 8, 8, 9, 10]
    resultado = calcular_estatisticas(valores)

    print(f"Valores: {valores}")
    print(f"Média: {resultado['media']}")
    print(f"Mediana: {resultado['mediana']}")
    print(f"Moda: {resultado['moda']}")
