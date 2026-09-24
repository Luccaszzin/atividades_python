"""Módulo que demonstra *args e **kwargs em um relatório."""


def relatorio(titulo, *linhas, **config):
    """Mostra um relatório formatado com linhas e configurações opcionais."""
    separador = config.get("separador", "-")
    largura = config.get("largura", 40)
    maiusculas = config.get("maiusculas", False)

    print(separador * largura)
    print(titulo.upper() if maiusculas else titulo)
    print(separador * largura)

    for linha in linhas:
        print(f"- {linha}")

    print(separador * largura)


if __name__ == "__main__":
    relatorio(
        "Relatório de vendas",
        "Janeiro: R$ 1.200",
        "Fevereiro: R$ 1.500",
        separador="=",
        largura=35,
        maiusculas=True,
    )
