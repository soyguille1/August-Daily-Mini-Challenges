class Figura:
    def imprimir(self):
        print("Soy una figura genérica.")

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def imprimir(self):
        print(f"Soy un círculo con radio {self.radio}.")

figura_generica = Figura()
figura_generica.imprimir() 

mi_circulo = Circulo(5)
mi_circulo.imprimir() 
