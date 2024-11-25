import informacion


contador = 0
while contador <= 0:
    print("/***************************************************************/")
    nombre= input("Ingresar el nombre: ")
    apellido= input("Ingresar el apellido: ")
    anio= int(input("Ingresar su año de nacimiento: "))

    informacion.agregar_nombre(nombre,apellido)
    informacion.agregar_edad(anio)

    result = input("Desea ingresar otra persona (si/no): ")
    if result =="no":
        contador=1

print("******* Lista de nombres *******")
informacion.lista_nombre()
print("******* Lista de edades *******")
informacion.lista_edades()
print("******* Paciente Mayor *******")
informacion.mayor()
print("******* Paciente Menor *******")
informacion.menor()


