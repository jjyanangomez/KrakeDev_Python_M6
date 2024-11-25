nombre_paciente=[]
edad =[]
def agregar_nombre(nombre, apellido):
    nombre_paciente.append(nombre+" "+apellido)

def agregar_edad(año_nacimiento, anio_actual=2024):
     edad_actual = anio_actual-año_nacimiento
     edad.append(edad_actual)

def lista_nombre():
    for name in nombre_paciente:
        print(name, end=", ")

def lista_edades():
    for i in edad:
        print(i, end=", ")

def mayor():
    mayor_edad = max(edad)
    paciente_mayor = nombre_paciente[edad.index(mayor_edad)]
    print(f"\n{paciente_mayor} con la edad de {mayor_edad} años es mayor a los demás pacientes.")
  

def menor():
    menor_edad = min(edad)
    paciente_menor = nombre_paciente[edad.index(menor_edad)]
    print(f"{paciente_menor} con la edad de {menor_edad} años es menor a los demás pacientes.")