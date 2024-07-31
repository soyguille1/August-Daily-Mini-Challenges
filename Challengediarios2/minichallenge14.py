class Animal:
    def hacerSonido(self):
        print("El animal hace un sonido.")

class Perro(Animal):
    def hacerSonido(self):
        print("El perro ladra: ¡Guau, guau!")

def mostrarSonido(animal):
    animal.hacerSonido()

animal_generico = Animal()
mi_perro = Perro()

mostrarSonido(animal_generico)
mostrarSonido(mi_perro)
