from abc import ABC, abstractmethod


# Main class
class Calculadora():

    def calcular(self, valor1, valor2, operador):
        fabrica = OperacaoFabrica()
        calculo = fabrica.criar(operador)
        if (calculo):
            try:
                resultado = calculo.executar(valor1, valor2)
                return resultado
            except Exception:
                print({"InvalidInput": "Digite um número válido"})
                return False
        else:
            print({"InvalidInput": "Digite um operador valido(adicao, subtracao, divisao ou multiplicacao)"})
            return False


# Strategy/control class
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


# Abstract of Operators
class Operacao(ABC):

    @abstractmethod
    def executar(self, valor1, valor2):
        pass


# Operators


# Add
class Adicao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 + valor2


# Sub
class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 - valor2


# Div
class Divisao(Operacao):
    def executar(self, valor1, valor2):
        if (valor2 == 0):
            print({"ZeroDivisionError": "Divisao por 0"})
            return False
        return valor1/valor2


# Mult
class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 * valor2


# __________Tests
teste = Calculadora()
print(teste.calcular(2, 4, "adicao"))
print(teste.calcular(4, 2, "subtracao"))
print(teste.calcular(2, 4, "divisao"))
print(teste.calcular(2, 4, "multiplicacao"))
