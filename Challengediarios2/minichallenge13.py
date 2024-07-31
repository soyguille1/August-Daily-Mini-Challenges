class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Has depositado {monto}. Saldo actual: {self.saldo}")
        else:
            print("El monto a depositar debe ser positivo.")

    def consultar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

def menu():
    cuenta = CuentaBancaria()
    while True:
        print("\n--- Menú ---")
        print("1. Depositar")
        print("2. Consultar Saldo")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            monto = float(input("Introduce el monto a depositar: "))
            cuenta.depositar(monto)
        elif opcion == '2':
            cuenta.consultar_saldo()
        elif opcion == '3':
            print("Gracias por usar el servicio bancario.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
