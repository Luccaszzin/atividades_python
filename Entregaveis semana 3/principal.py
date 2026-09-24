#Arquivo principal: demonstra o uso dos módulos da Semana 03.

import calculadora as calc
import utilidades as util


def executar_exemplos():
    """Executa exemplos das funções criadas para a atividade."""
    print("--- Calculadora ---")
    print(f"2 + 3 = {calc.somar(2, 3)}")
    print(f"10 - 4 = {calc.subtrair(10, 4)}")
    print(f"6 × 7 = {calc.multiplicar(6, 7)}")
    print(f"10 ÷ 2 = {calc.dividir(10, 2)}")
    print(calc.dividir(10, 0))

    print("\n--- Utilidades ---")
    temperaturas = util.converter_temperatura(25)
    print(f"25 °C = {temperaturas['fahrenheit']} °F")
    print(f"25 °C = {temperaturas['kelvin']} K")

    senha = "Python2026"
    print(f"A senha '{senha}' é válida? {util.validar_senha(senha)}")
    total = util.calcular_total_caixa(10.50, 7.25, 2.00)
    print(f"Total do caixa: R$ {total:.2f}")

    ficha = util.criar_ficha_aluno(nome="Lucas", idade=20, curso="Python")
    print(f"Ficha do aluno: {ficha}")

    compras = ["arroz", "feijão"]
    nova_lista = util.adicionar_item_seguro(compras, "café")
    print(f"Lista original: {compras}")
    print(f"Nova lista: {nova_lista}")


# Este bloco só executa os exemplos ao rodar este arquivo diretamente.
if __name__ == "__main__":
    executar_exemplos()
