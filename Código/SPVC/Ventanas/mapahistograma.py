import tkinter as tk
from PIL import ImageTk, Image
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os 

# Crear la ventana principal
ventana = tk.Tk()

# Establecer el tamaño de la ventana
ancho_ventana = 800
alto_ventana = 650

# Establecer el título de la ventana
ventana.title("Sistema de predicción del valor de casas")

# Obtener el ancho y alto de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana
x = (ancho_pantalla - ancho_ventana) // 2
y = (alto_pantalla - alto_ventana) // 2

# Establecer la posición y tamaño de la ventana
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

# Establecer el color de fondo azul oscuro
ventana.configure(bg="#030918")

# Título
titulo_label = tk.Label(ventana, text="HISTOGRAMA", font=("Arial", 20, "bold"), fg="white", bg="#030918")
titulo_label.pack(pady=10)

def abrir_ventana4():
    # Ruta del archivo a destruir
    archivo_a_destruir = "histograma_temporal.png"

    # Verificar si el archivo existe antes de destruirlo
    if os.path.exists(archivo_a_destruir):
        os.remove(archivo_a_destruir)
    ventana.withdraw()
    ruta_ventana4 = os.path.join("Ventanas", "ventana4.py")
    os.system(f"python {ruta_ventana4}")
    ventana.destroy()

boton_atras = tk.Button(ventana, text="Atras", font=("Arial", 16, "bold"), command=abrir_ventana4)
boton_atras.place(x=10, y=10)

# Cargar el dataset limpio en un DataFrame
dataset_path = "dataset_limpio.csv"  
df = pd.read_csv(dataset_path)

# Obtener los campos para los histogramas
campos = ["Precio", "Area"]
colores = ["blue", "green"]  # Colores para los histogramas
campo_actual = 0

def generar_histograma():
    campo = campos[campo_actual]
    color = colores[campo_actual]

    # Crear una nueva figura y ejes
    figure, ax = plt.subplots()

    # Generar el histograma del campo correspondiente
    n, bins, patches = ax.hist(df[campo], bins=10, color=color, edgecolor='black', alpha=0.7)  # Asignar color al histograma

    # Obtener las coordenadas del polígono de frecuencia
    heights = np.array([patch.get_height() for patch in patches])
    bin_centers = np.array([(bins[i] + bins[i+1]) / 2 for i in range(len(bins) - 1)])

    # Mostrar el polígono de frecuencia
    ax.plot(bin_centers, heights, color='red', linewidth=2)

    ax.set_xlabel(campo)
    ax.set_ylabel("Frecuencia")
    ax.set_title(f"Histograma de {campo}")
    ax.grid(True)

    # Guardar el histograma en una imagen temporal
    imagen_temporal = "histograma_temporal.png"
    plt.savefig(imagen_temporal)

    # Cargar la imagen temporal en el label de la ventana
    imagen = Image.open(imagen_temporal)
    imagen = imagen.resize((600, 400))
    imagen = ImageTk.PhotoImage(imagen)
    imagen_label.configure(image=imagen)
    imagen_label.image = imagen

def imagen_siguiente():
    global campo_actual
    campo_actual = (campo_actual + 1) % len(campos)
    generar_histograma()

def imagen_anterior():
    global campo_actual
    campo_actual = (campo_actual - 1) % len(campos)
    generar_histograma()

imagen_label = tk.Label(ventana)
imagen_label.pack()

# Generar el primer histograma
generar_histograma()

# Botones de navegación
boton_anterior = tk.Button(ventana, text="Anterior", font=("Arial", 16, "bold"), command=imagen_anterior)
boton_anterior.place(x=10, y=550)

boton_siguiente = tk.Button(ventana, text="Siguiente", font=("Arial", 16, "bold"), command=imagen_siguiente)
boton_siguiente.place(x=680, y=550)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()









