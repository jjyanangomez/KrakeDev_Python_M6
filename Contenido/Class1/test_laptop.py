from laptop import Laptop

laptop_pepito = Laptop("Lenovo","I7",32)
laptop_maria = Laptop("Lenovo","I7",32,600)


# print(laptop_pepito.__dict__)
# print(laptop_pepito.valor_final())
# print(laptop_pepito.valor_descuento(10))

for numero in range(1,1001):
    Asus_laptop = Laptop.asus_laptop(numero)
    print(Asus_laptop.__dict__)
#print(Laptop.comparar_costos(laptop_pepito,laptop_maria))