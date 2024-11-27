from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from laptop_business import Laptop_Business

laptop_pepito = Laptop("Lenovo","I7",32)
laptop_maria = Laptop("Lenovo","I7",32,600)
laptop_juanito = Laptop_Gaming("MSI","I7",4,"RTX 8GB")
laptop_jefe=Laptop_Business("Dell", "i5", 8, 424, 10)


print(laptop_jefe.realizar_diagnostico_sistema())
# print(laptop_pepito.__dict__)
# print(laptop_pepito.valor_final())
# print(laptop_pepito.valor_descuento(10))
print(laptop_juanito.costo)

print(laptop_juanito.realizar_diagnostico_sistema())

# for numero in range(1,1001):
#     Asus_laptop = Laptop.asus_laptop(numero)
#     print(Asus_laptop.__dict__)
#print(Laptop.comparar_costos(laptop_pepito,laptop_maria))
