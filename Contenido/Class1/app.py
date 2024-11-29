from laptop_gaming import Laptop_Gaming
import tkinter as tk
import tkinter as ttk

from PIL import Image,ImageTk
import random

class App:
    def __init__(self,root):
        self.root = root
        self.laptops = []
        self.imagenes = ["C:\\Users\\H P\\Desktop\\JuanJo\\Curso_KrakeDev\\Practicas\\Modulo_6_Python\\Contenido\\Class1\\img\\1.png",
                         "C:\\Users\\H P\\Desktop\\JuanJo\\Curso_KrakeDev\\Practicas\\Modulo_6_Python\\Contenido\\Class1\\img\\2.png",
                         "C:\\Users\\H P\\Desktop\\JuanJo\\Curso_KrakeDev\\Practicas\\Modulo_6_Python\\Contenido\\Class1\\img\\3.png",
                         "C:\\Users\\H P\\Desktop\\JuanJo\\Curso_KrakeDev\\Practicas\\Modulo_6_Python\\Contenido\\Class1\\img\\4.png",
                         "C:\\Users\\H P\\Desktop\\JuanJo\\Curso_KrakeDev\\Practicas\\Modulo_6_Python\\Contenido\\Class1\\img\\5.png"]
        
        self.setup_ui()

        root.title("Ingresar Datos")

    
    def setup_ui(self):
        ttk.Label(self.root, text="Marca").grid(row=0,column=0)
        self.marca = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.marca).grid(row=0,column=1)

        ttk.Label(self.root, text="Procesador").grid(row=1,column=0)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.procesador).grid(row=1,column=1)

        ttk.Label(self.root, text="Memoria").grid(row=2,column=0)
        self.memoria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.memoria).grid(row=2,column=1)

        ttk.Label(self.root, text="Tarjeta Gráfica").grid(row=3,column=0)
        self.tarjeta_graf = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.tarjeta_graf).grid(row=3,column=1)

        ttk.Label(self.root, text="Precio").grid(row=4,column=0)
        self.precio = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.precio).grid(row=4,column=1)

        ttk.Button(self.root, text="Agregar Laptop", command=self.agregar_laptop).grid(row=5,column=0)

        self.mostrar_laptops = tk.Text(self.root, height=10, width=50)
        self.mostrar_laptops.grid(row=6,column=0,columnspan=2)


        self.canva = tk.Canvas(self.root,height=200, width=200)
        self.canva.grid(row=1,column=3,rowspan=6)
        
        

    def mostrar_imagenes_aleatorias(self):
        imagenPath=random.choice(self.imagenes)
        imagen=Image.open(imagenPath)
        imagen=imagen.resize((200,200),Image.Resampling.LANCZOS)
        photo=ImageTk.PhotoImage(imagen)
        self.canva.create_image(0,0,anchor=tk.NW,image=photo)

        self.canva.image=photo


    def agregar_laptop(self):
        nueva_laptop = Laptop_Gaming(self.marca.get(), 
                                     self.procesador.get(), 
                                     self.memoria.get(), 
                                     self.tarjeta_graf.get(), 
                                     self.precio.get())
        self.laptops.append(nueva_laptop)
        self.mostrar_laptops.insert(tk.END, f"{nueva_laptop}")
        #for laptop in self.laptops:
        #    self.mostrar_laptops.insert(tk.END, f"{laptop}\n{'-' * 20}\n")
        self.mostrar_imagenes_aleatorias()
        pass

root = tk.Tk()
app = App(root)
root.mainloop()