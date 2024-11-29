import random
from laptop import Laptop


class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria, almacenamiento, duracion_bateria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento =almacenamiento
        self.duracion_bateria = duracion_bateria

    def __str__(self):
        return (f"Marca: {self.marca}\n"
            f"Procesador: {self.procesador}\n"
            f"Memoria: {self.memoria}\n"
            f"Almacenamieto: {self.almacenamiento}\n"
            f"Duración bateria: {self.duracion_bateria}\n"
            f"Costo: {self.costo}\n"
            f"Impuesto: {self.impuesto}\n")

    def realizar_diagnostico_sistema(self):
        resultado_diagnostico= super().realizar_diagnostico_sistema()
        resultado_diagnostico["Resultado almacenamiento "]={
            "Almacenamiento": "OK" if self.almacenamiento >= 256 else "Aumentar capacidad de almacenamiento",
            "Duracion Bateria": "OK" if self.duracion_bateria >= 8 else "Reemplazar batería (duración insuficiente)"
        }
        return resultado_diagnostico

  
    def verificar_conectividad(self):
        resultados_red={
            "Wi-Fi disponible": random.choice([True, False]),
            "Acceso a servidores empresariales": random.choice([True, False]),
            "Latencia de red aceptable": random.choice([True, False])
        }
        return resultados_red
    pass