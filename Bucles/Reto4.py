datos=[]

cantidad = int(input("¿Cuántos datos desea ingresar?: "))

for i in range(cantidad):
    entrada = input(f"Ingrese el dato {i + 1}: ")

    if entrada.isdigit():
        datos.append(int(entrada))

    elif entrada.replace('.', '', 1).isdigit() and entrada.count('.') == 1:
        datos.append(float(entrada))

    else:
        datos.append(entrada)

print(f"Su lista es: <{datos}>")
