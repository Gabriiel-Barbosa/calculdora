class Calculadora:
    def operacao(self, operacao, a, b):
        if operacao == 'soma':
            return a + b
        elif operacao == 'subtracao':
            return a - b
        elif operacao == 'multiplicacao':
            return a * b
        elif operacao == 'divisao':
            return a / b