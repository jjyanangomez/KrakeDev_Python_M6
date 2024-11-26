from auto import Auto

# mi_auto = Auto("Toyota", "Corolla", 2020)
# mi_auto.mostrar_informacion()

# mi_auto.actualizar_kilometraje(500)
# mi_auto.mostrar_informacion()

# mi_auto.realizar_viaje(15000)
# mi_auto.mostrar_informacion()

# mi_auto.estado_auto()

mi_auto2 = Auto.instancia_Auto("Nose que poner") 
mi_auto3 = Auto.crear_auto_generico()

print("\nInformación del auto 2:")
mi_auto2.mostrar_informacion()
print("\nInformación del auto 3:")
mi_auto3.mostrar_informacion()

mi_auto2.kilometraje = 50000
mi_auto3.kilometraje = 50000

print(Auto.comparar_kilometraje(mi_auto2,mi_auto3))