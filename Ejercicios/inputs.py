nota_Tarea= float(input("Ingresar la nota de la tarea: "))
nota_Leccion= float(input("Ingresar la nota de la leccion: "))
nota_Examen= float(input("Ingresar la nota del examen: "))

total_promedio = (nota_Tarea + nota_Leccion + nota_Examen)/3

print(f"Promedio: {total_promedio}")