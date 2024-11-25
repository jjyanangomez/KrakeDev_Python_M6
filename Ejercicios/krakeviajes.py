import random

ecuador = random.randint(10, 90)
colombia = random.randint(10, 100)
peru = random.randint(10, 120)

if ecuador >= 10 and ecuador <= 50:
    print(f"La Velocidad es {ecuador}: Buena velocidad en Zona Urbana de Ecuador")
elif ecuador >= 51 and ecuador <= 70:
    print(f"La Velocidad es {ecuador}: Buena velocidad en Zona Rural de Ecuador")
elif ecuador >= 71 and ecuador <= 90:
    print(f"La Velocidad es {ecuador}: Buena velocidad en Zona Perimetral de Ecuador")
else:
    print(f"La Velocidad es {ecuador}: Disminuye tu velocidad estas en Ecuador!!!")

if colombia >= 10 and colombia <= 30:
    print(f"La Velocidad es {colombia}: Buena velocidad en Zona Urbana de Colombia")
elif colombia >= 31 and colombia <= 80:
    print(f"La Velocidad es {colombia}: Buena velocidad en Zona Rural de Colombia")
elif colombia >= 81 and colombia <= 100:
    print(f"La Velocidad es {colombia}: Buena velocidad en Zona Perimetral de Colombia")
else:
    print(f"La Velocidad es {colombia}: Disminuye tu velocidad estas en Colombia!!!")

if peru >= 10 and peru <= 30:
    print(f"La Velocidad es {peru}: Buena velocidad en Zona Urbana de Peru")
elif peru >= 31 and peru <= 80:
    print(f"La Velocidad es {peru}: Buena velocidad en Zona Rural de Peru")
elif peru >= 81 and peru <= 100:
    print(f"La Velocidad es {peru}: Buena velocidad en Zona Perimetral de Peru")
else:
    print(f"La Velocidad es {peru}: Disminuye tu velocidad estas en Peru!!!")