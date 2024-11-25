planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano","Neptuno"]
# print(planetas[-3])
# #Imprimir desde venus hasta finalizar la lista
# print(planetas[1: ])
# print(len(planetas))

#Trabajar con una lista de numeros
gravedad_de_planeta=[0.378,0.907,1, 0.377, 2.36, 0.916,0.889,1.12]
peso_bus = 1234054 #Newtwon en la tierra

print(f"En la Tierra, un autobús de dos pisos pesa {peso_bus} N")
print(f"En Mercurio un autobus de dos pisos pesa {peso_bus*gravedad_de_planeta[0]} N")

print(f"Lo mas liviano que seria un autobus en el sistema solar es {peso_bus* min(gravedad_de_planeta)}")
print(f"Lo mas pesado que seria un autobus en el sistema solar es {peso_bus* max(gravedad_de_planeta)}")