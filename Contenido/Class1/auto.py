class Auto:
    def __init__(self,marca, modelo, anio, kilometraje = 0):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje

    def mostrar_informacion(self):
        print("********************* Auto ********************")
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAño: {self.anio}\nKilometraje: {self.kilometraje} km")
    
    def actualizar_kilometraje(self, kilometraje):
        if self.kilometraje>=kilometraje:
            print("No se puede reducir el kilometraje, debajo del 0")
        else:
            self.kilometraje = kilometraje
    
    def  realizar_viaje(self, kilometros):
        if kilometros <= 0:
            print("No se puede aumentar el kilometraje La cantidad de kilómetros debe ser positiva")
        else:
            self.kilometraje +=kilometros

    def estado_auto(self):
        if self.kilometraje < 20000:
            print("Estoy como nuevo.")
        elif 20000 <= self.kilometraje <= 100000:
            print("Ya estoy usado.")
        else:
            print("¡Ya déjame descansar por favor!")

mi_auto = Auto("Toyota", "Corolla", 2020)
mi_auto.mostrar_informacion()

mi_auto.actualizar_kilometraje(500)
mi_auto.mostrar_informacion()

mi_auto.realizar_viaje(15000)
mi_auto.mostrar_informacion()

mi_auto.estado_auto()