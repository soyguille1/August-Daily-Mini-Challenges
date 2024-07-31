class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def describir(self):
        return f"Motor tipo {self.tipo} con {self.potencia} caballos de fuerza."

class Auto:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def describir_auto(self):
        descripcion_motor = self.motor.describir()
        return f"Auto marca {self.marca}, modelo {self.modelo}, con {descripcion_motor}"

motor_v8 = Motor("V8", 450)
mi_auto = Auto("Ford", "Mustang", motor_v8)
print(mi_auto.describir_auto())
