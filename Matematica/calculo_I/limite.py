class CalculadoraDeLimite:
    def __init__(self, funcao):
        self.funcao = funcao

    def calcular_limite(self, x0, h=1e-5):
        esquerda = self.funcao(x0 - h)
        direita = self.funcao(x0 + h)
        return (esquerda + direita)
                    
calc = CalculadoraDeLimite(lambda x: x**2)
print(calc.calcular_limite(2))