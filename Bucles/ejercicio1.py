lista=[1,2,3,4,5,"Anthony","Pedro",1,2,3,4,7,7,"Anthony"]

elemento="Anthony"
for i in lista:
    #print(i)
    # Separar los elementos con una coma
    #print(i, end=", ")
    if elemento==i:
        print(f"El elemento {elemento} esta dentro de la lista")