class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def desplazarXY(self, dx, dy):
        self.x += dx
        self.y += dy

    def desplazarX(self, dx):
        self.x += dx

    def desplazarY(self, dy):
        self.y += dy

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, new_x):
        self.x = new_x

    def setY(self, new_y):
        self.y = new_y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def sonIguales(self, otro_punto):
        return self.x == otro_punto.x and self.y == otro_punto.y

    def copia(self):
        return Punto2D(self.x, self.y)

mi_punto = Punto2D(3, 4)
print("Coordenadas del punto:", mi_punto) 
