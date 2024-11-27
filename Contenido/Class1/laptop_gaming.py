from laptop import Laptop

class Laptop_Gaming(Laptop):
    def __init__(self, marca, procesador, memoria,tarjeta_grafica, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.tarjeta_graf = tarjeta_grafica
    
    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_juego = self.realizar_diagnostico_juegos()
        resultado_diagnostico["Resultados juegos"]= resultado_juego
        return resultado_diagnostico
    
    def realizar_diagnostico_juegos(self):
        juegos=["Fortnite","COD","GTA","RE"]
        resultados = {}
        for juego in juegos:
            fp_base = 30
            if "RTX" in self.tarjeta_graf:
                fps = fp_base*3
            elif "GTX" in self.tarjeta_graf:
                fps = fp_base*2
            else:
                fps = fp_base
            resultados[juego] = f"{fps} FPS"
        return resultados




    pass