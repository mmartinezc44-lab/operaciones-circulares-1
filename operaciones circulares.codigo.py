class Generador:
    def __init__(self, id, potencia, estado):
        self.id = id
        self.potencia = potencia
        self.estado = estado
        self.siguiente = None


class ListaCircular:
    def __init__(self):
        self.cabeza = None

    # Insertar generador
    def insertar(self, id, potencia, estado):
        nuevo = Generador(id, potencia, estado)

        if self.cabeza is None:
            self.cabeza = nuevo
            nuevo.siguiente = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.siguiente = self.cabeza

        print("Generador agregado correctamente.")

    # Mostrar generadores
    def mostrar(self):
        if self.cabeza is None:
            print("No hay generadores registrados.")
            return

        actual = self.cabeza
        while True:
            print(f"ID: {actual.id} | Potencia: {actual.potencia} kW | Estado: {actual.estado}")
            actual = actual.siguiente
            if actual == self.cabeza:
                break

    # Buscar generador
    def buscar(self, id):
        if self.cabeza is None:
            print("Lista vacía.")
            return

        actual = self.cabeza
        while True:
            if actual.id == id:
                print("Generador encontrado:")
                print(f"ID: {actual.id} | Potencia: {actual.potencia} kW | Estado: {actual.estado}")
                return
            actual = actual.siguiente
            if actual == self.cabeza:
                break

        print("Generador no encontrado.")

    # Eliminar generador
    def eliminar(self, id):
        if self.cabeza is None:
            print("Lista vacía.")
            return

        actual = self.cabeza
        anterior = None

        while True:
            if actual.id == id:
                # Caso: solo un nodo
                if actual.siguiente == self.cabeza and anterior is None:
                    self.cabeza = None
                # Caso: eliminar cabeza
                elif actual == self.cabeza:
                    temp = self.cabeza
                    while temp.siguiente != self.cabeza:
                        temp = temp.siguiente
                    temp.siguiente = self.cabeza.siguiente
                    self.cabeza = self.cabeza.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                print("Generador eliminado correctamente.")
                return

            anterior = actual
            actual = actual.siguiente

            if actual == self.cabeza:
                break

        print("Generador no encontrado.")

    # Simular rotación de carga
    def simular_rotacion(self, vueltas):
        if self.cabeza is None:
            print("No hay generadores para simular.")
            return

        actual = self.cabeza
        print("\n--- Simulación de Rotación de Carga ---")
        for i in range(vueltas):
            print(f"Turno {i+1}: Generador {actual.id} suministra {actual.potencia} kW")
            actual = actual.siguiente


# ================== PROGRAMA PRINCIPAL ==================

lista = ListaCircular()

while True:
    print("\n===== SISTEMA DE GENERADORES =====")
    print("1. Insertar generador")
    print("2. Eliminar generador")
    print("3. Buscar generador")
    print("4. Mostrar generadores")
    print("5. Rotar turno de carga")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        id_gen = input("ID del generador: ")
        potencia = float(input("Potencia (kW): "))
        estado = input("Estado (Activo/Mantenimiento): ")
        lista.insertar(id_gen, potencia, estado)

    elif opcion == "2":
        id_gen = input("ID del generador a eliminar: ")
        lista.eliminar(id_gen)

    elif opcion == "3":
        id_gen = input("ID del generador a buscar: ")
        lista.buscar(id_gen)

    elif opcion == "4":
        lista.mostrar()

    elif opcion == "5":
        vueltas = int(input("¿Cuántos turnos desea simular?: "))
        lista.simular_rotacion(vueltas)

    elif opcion == "6":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")