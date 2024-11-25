frase = input("Ingrese la frase")
letra = input("Ingrese la letra")

contador = 0
for i in frase:
    if i==letra:
        contador +=1

print(f"La letra {letra} se repite {contador}")

#Simplificar la busqueda de letras
print(frase.count(letra))