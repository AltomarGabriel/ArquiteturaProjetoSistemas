from abc import ABC, abstractmethod


class Calculadora():
    def calcular(self, valor1, valor2, operador):
        fabrica = OperacaoFabrica()
        calculo = fabrica.criar(operador)
        resultado = calculo.executar(valor1, valor2)
        return resultado


class OperacaoFabrica():
    def criar(self, operador):
        if (operador == 'adicao'):
            return Adicao()

        if (operador == 'subtracao'):
            return Subtracao()

        if (operador == 'divisao'):
            return Divisao()

        if (operador == 'multiplicacao'):
            return Multiplicacao()


class Operacao(ABC):

    @abstractmethod
    def executar(self, valor1, valor2):
        pass


class Adicao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 + valor2


class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 - valor2


class Divisao(Operacao):
    def executar(self, valor1, valor2):
        return valor1/valor2


class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 * valor2


# __________Testes
teste = Calculadora()
print(teste.calcular(2, 4, "adicao"))
print(teste.calcular(2, 4, "subtracao"))

"""
a = Adicao()
print(a.executar(2, 4))
a = Subtracao()
print(a.executar(2, 4))
a = Divisao()
print(a.executar(2, 4))
a = Multiplicacao()
print(a.executar(2, 4))
"""
